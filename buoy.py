"""Run the tabletop buoy with simulated inputs or a Raspberry Pi 3."""

import argparse
from contextlib import ExitStack
from dataclasses import dataclass, replace
from time import monotonic, sleep
from typing import Optional


PULSE_SECONDS = 2.0
POLL_SECONDS = 0.05

# BCM GPIO numbers, not the physical pin positions.
PUMP_PIN = 17
FORECAST_PIN = 27
FLOAT_PIN = 22
RUN_PIN = 23


@dataclass(frozen=True)
class Readings:
    heavy_rain: bool = False
    cloudy: bool = False
    tank_ok: bool = True
    run_held: bool = True


class Controller:
    """Allow one short pulse per event while the tank and run switch allow it."""

    def __init__(self):
        self.stop_at: Optional[float] = None
        self.event_used = False

    def step(self, now: float, readings: Readings):
        event = readings.heavy_rain or readings.cloudy
        if self.stop_at is not None:
            if not readings.tank_ok or not readings.run_held:
                self.stop_at = None
                return False, "Pulse stopped: tank low or run button released"
            if now >= self.stop_at:
                self.stop_at = None
                return False, "Pulse complete"
            return True, "Pumping demo water"

        if not event:
            self.event_used = False
            return False, "Watching: no storm or cloudy sample"
        if not readings.tank_ok:
            return False, "Blocked: tank low or float switch open"
        if not readings.run_held:
            return False, "Blocked: hold the run button"
        if self.event_used:
            return False, "Waiting for both triggers to clear"

        self.event_used = True
        self.stop_at = now + PULSE_SECONDS
        return True, "Pulse started: moving demo water"


def simulate():
    storm = Readings(heavy_rain=True)
    cloudy = Readings(cloudy=True)
    scenarios = [
        ("Clear water", Readings()),
        ("Run button released", Readings(heavy_rain=True, run_held=False)),
        ("Heavy rain only", storm),
        ("Storm continues", storm),
        ("Two seconds later", storm),
        ("Storm still present", storm),
        ("Storm clears", Readings()),
        ("Cloudy sample only", cloudy),
        ("Tank level drops", Readings(cloudy=True, tank_ok=False)),
        ("Tank refilled, sample still cloudy", cloudy),
        ("Sample clears", Readings()),
        ("Another cloudy sample", cloudy),
        ("Run button released mid-pulse", Readings(cloudy=True, run_held=False)),
    ]
    controller = Controller()
    for now, (label, readings) in enumerate(scenarios):
        pump_on, message = controller.step(now, readings)
        output = " ON" if pump_on else "OFF"
        print(f"{now:2}s  {output}  {label:<35} {message}")


def simulate_interactively():
    controller = Controller()
    readings = Readings()
    now = 0
    inputs = {
        "rain": "heavy_rain",
        "cloudy": "cloudy",
        "tank": "tank_ok",
        "run": "run_held",
    }
    print("Toggle an input with rain, cloudy, tank, or run.")
    print("Press Enter or type step to advance 1 second. Type quit to leave.")

    while True:
        print(
            f"Inputs | Rain: {'heavy' if readings.heavy_rain else 'clear'}"
            f" | Sample: {'cloudy' if readings.cloudy else 'clear'}"
            f" | Tank: {'OK' if readings.tank_ok else 'low'}"
            f" | Run: {'held' if readings.run_held else 'released'}"
        )
        try:
            command = input(f"{now:2}s > ").strip().lower()
        except EOFError:
            print()
            return

        if command == "quit":
            return
        if command in inputs:
            field = inputs[command]
            readings = replace(readings, **{field: not getattr(readings, field)})
        elif command in ("", "step"):
            now += 1
            pump_on, message = controller.step(now, readings)
            print(f"Pump {'ON' if pump_on else 'OFF'} | {message}")
        else:
            print("Use rain, cloudy, tank, run, step, or quit.")


def read_light():
    from gpiozero import MCP3008

    with MCP3008(channel=0) as sensor:
        while True:
            print(f"Light reading: {sensor.value:.3f}", flush=True)
            sleep(0.5)


def run_on_pi(light_threshold: float):
    from gpiozero import Button, MCP3008, OutputDevice

    controller = Controller()
    with ExitStack() as devices:
        pump = devices.enter_context(OutputDevice(PUMP_PIN, initial_value=False))
        forecast = devices.enter_context(Button(FORECAST_PIN, pull_up=True))
        float_switch = devices.enter_context(Button(FLOAT_PIN, pull_up=True))
        run_button = devices.enter_context(Button(RUN_PIN, pull_up=True))
        light = devices.enter_context(MCP3008(channel=0))
        last_message = None

        try:
            while True:
                readings = Readings(
                    heavy_rain=forecast.is_pressed,
                    cloudy=light.value < light_threshold,
                    tank_ok=float_switch.is_pressed,
                    run_held=run_button.is_pressed,
                )
                pump_on, message = controller.step(monotonic(), readings)
                if pump_on:
                    pump.on()
                else:
                    pump.off()
                if message != last_message:
                    print(message, flush=True)
                    last_message = message
                sleep(POLL_SECONDS)
        finally:
            pump.off()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simulate", action="store_true", help="walk through sample events")
    mode.add_argument(
        "--interactive", action="store_true", help="set simulated inputs and step the controller"
    )
    mode.add_argument("--read-light", action="store_true", help="print optical readings")
    mode.add_argument("--gpio", action="store_true", help="use the wired tabletop buoy")
    parser.add_argument("--light-threshold", type=float, help="calibrated value in (0, 1)")
    args = parser.parse_args()

    if args.gpio and (
        args.light_threshold is None or not 0 < args.light_threshold < 1
    ):
        parser.error("--gpio requires --light-threshold between 0 and 1")

    try:
        if args.simulate:
            simulate()
        elif args.interactive:
            simulate_interactively()
        elif args.read_light:
            read_light()
        else:
            run_on_pi(args.light_threshold)
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
