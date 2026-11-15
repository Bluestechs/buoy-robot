# Classroom buoy design

## Concept explorer revision (supersedes the earlier layout and palette below)

The primary experience is free exploration of an outdoor buoy concept beside a LEGO SPIKE dry equivalent. Both models use layered inline SVG with shaded faces, translucent hull, studs, circuit details, sensors, and moving components. Native part buttons supplement SVG keyboard hotspots. The page is always light, using blue-gray #e4eef4, navy #18374c, pale panels #d5e5ee, and primary blue #185f83.

Layout: two equally sized model figures above secondary simulation and discussion content, stacking below 800px. The original diagram remains hidden as the controller's state bridge. Grade prompts and the sourced prototype budget use disclosures.

Selecting either model pairs its highlight and opens Python or LEGO blocks by default according to the model. Details appear in the center column between the models, close with Escape, and return focus. The outside columns are wider than the text column. Isolated animation has a separate timer and does not mutate controller state. Reduced motion suppresses animation. All prices are prototype prices; outdoor solar and enclosure are excluded. Existing equipment and shared supplies are not double counted.

Implementation syntax: both inline scripts parse under Node. Root owns browser acceptance and screenshot verification; no accessibility conformance claim is made before that check.

## Purpose and audience

The part list uses bundled component photos with plain-language names and one-sentence jobs. Photos are prototype examples, not photos of the imagined outdoor device. Seven photo buttons retain their existing component mapping and selected state. Cards use an auto-fit grid with 145px minimum columns and 112px photo areas; images preserve their proportions. Photo source credits appear in the part dialog. Relevant acronyms and unfamiliar terms are explained in a visible definition list; a shared Word helper offers the full glossary. The wording targets a nine-year-old reader without changing the controller rules or code examples. All photos are embedded in the HTML for offline use.

Students in grades 5–7 freely explore an imagined outdoor buoy beside its dry LEGO SPIKE equivalent. Selecting a component explains its purpose, Python logic, visual programming blocks, prototype cost, and movement. No hardware or tested outdoor prototype is assumed.

## Visual system

Use local system sans-serif fonts only. Always use a muted light theme: background #e4eef4, ink #18374c, secondary ink #466479, control #d5e5ee, rule #91adbd, primary #185f83, primary ink #ffffff. Water blue #287ba4, signal green #267b6b, and colored-water orange #b6572b identify physical roles. Shaded SVG surfaces distinguish equipment materials. System dark appearance does not change these colors.

Type: 16px base, 18px classroom body, 20px subheading, 25px section heading, fluid 32–48px title. SVG labels are 12px in its 640-unit drawing, enlarged with the diagram. Space scale: 4, 8, 12, 16, 24, 32, 48px. Control radius 8px; stage radius 16px. Neutral rules and tonal surfaces, no shadows. Numerals are tabular.

## Layout

Layout: simulator - keep the diagram dominant above supporting lessons -> stack (https://github.com/changeroa/StyleGallery/blob/main/patterns/stacking/stack.md); scroll owner: document; anti-patterns: no nested scrolling, fixed heights, or visual reordering of keyboard controls.

The two models sit side by side above simulation controls, stacking below 800px. Picture cards provide alternative selection. Selection expands the main canvas to at most 1800px and changes the model row to three columns: outdoor model, details, LEGO model. Outside columns use 1.12fr each; the middle uses .9fr with a 320px minimum. Details have 28px padding and a viewport-bounded scroll area; the devices remain visible beside it during animation. Below 1050px the three sections stack in that same order with normal document scrolling and 24px padding. Closing details restores the two-model layout. No detail content floats over a device. Cards have 16px padding; code blocks and table cells also have explicit inner spacing.

## Screen contract

Primary interaction: select a component. The part dialog's primary action is **Animate this part**. Priorities: paired models; component explanation/code/cost; optional simulation and discussion. Preserve six scenarios, four manual inputs, seven part mappings, grade prompts, play/pause/reset, elapsed time and countdown. Prototype budget counts shared supplies once, separates optional purchases, and excludes conceptual outdoor solar/enclosure.

Left out: scores, quizzes with stored answers, network data, audio, external assets, decorative badges, and automatic fullscreen. Cloudiness does not establish algae. The output moves food-colored water; it does not demonstrate environmental treatment.

## Behavior and accessibility

Play advances one simulated second per 1000ms while the page is visible. Pause, scenario changes, reset, and page hiding stop its interval. Next step pauses playback before advancing once. Reset returns the current scenario to time zero and restores manual inputs to clear/clear/water present/run held. Changing grade resets only the explanation reveal. Controller interlocks and one-pulse-per-event rules stay unchanged.

Native controls and SVG buttons have visible keyboard focus. Selection highlights matching parts on both models. Enter/Space opens the labeled details region, Escape closes and restores focus. Hover/focus previews are paired. Code selector buttons use aria-pressed. Reduced-motion explanations remain readable without animation. Browser checks cover these behaviors; they are not a full WCAG certification.

## Motion

Part demonstrations have three labeled phases, each lasting 2.6 seconds. Both devices gain a large inline action close-up; the overview reduces in height so the close-up remains visible beside the center text. Close-ups use the same component artwork as the overview. Motions intentionally exaggerate signal travel, button travel, float level and marker distance; pump rollers rotate and directional flow shows water movement, while the LEGO motor turns an indicator. The optical demo switches between clear/light and cloudy/dark. The controller shows read, decide and command phases. Stop, replay, selecting another part, closing details and hiding the tab all cancel pending phase timers. Completion leaves the final close-up and caption visible, with a Replay button. Demonstrations never write controller inputs or time. Reduced motion disables movement and transitions while retaining all three captions and static before/after states.

The main diagrams use a 600×730 coordinate canvas with separate component zones and labels below each component. Signal routes run behind the artwork and away from labels. The LEGO illustration follows LEGO's official technical reference: a white face/yellow-sided Large Hub with a 5×5 light matrix, white/black two-eye Distance Sensor, white/black single-lens Color Sensor, and white/turquoise Medium Angular Motor with cross-axle output and Technic mounting holes. Hub-button detail views are named as Hub buttons, not separate devices. Reference: https://education.lego.com/en-us/product-resources/spike-prime/downloads/technical-specifications/

## Verification and gaps

Baseline: `.omo/evidence/before.png`, captured by the root QA owner before edits. Initial gaps: diagram constrained beside dense prose; no playback/reset/presentation; no grade-specific predictions; no separate pump countdown. Implementation addresses these gaps. Root owns actual browser verification, screenshot pairs, and accessibility verdict. WCAG 2.2 AA conformance is pending that verification; source inspection alone is not a pass.
