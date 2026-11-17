# Classroom buoy design

## Concept explorer revision (supersedes the earlier layout and palette below)

The primary experience is free exploration of an outdoor buoy concept beside a LEGO SPIKE dry equivalent. Both models use layered inline SVG with shaded faces, translucent hull, studs, circuit details, sensors, and moving components. Native part buttons supplement SVG keyboard hotspots. The page is always light, using blue-gray #e4eef4, navy #18374c, pale panels #d5e5ee, and primary blue #185f83.

Layout for ages 7–10: the homepage starts with the kids' complete proposal and attribution, followed by an **In their plan, but not in a model yet** band that quotes the kids' own words for the concepts with no model or prototype: the farm levee, the lake boat with beneficial bacteria, the two tanks with a one-way valve, the side sprayer, and the water filter. Three themes then follow in document order: the two models with same-job comparisons, the simulator, then **Meet the parts**. The earlier **Be the weather** prediction game was removed. The four manual switches control rain, cloudy water, water level and run permission. The original diagram remains hidden as the controller's state bridge. Python, costs and the prototype budget use mentor disclosures. Scenario presets and grade 5–7 discussion prompts were removed.

The seven model parts name the kids' part each stand-in represents: antenna and transmitter (button stand-in), solar and battery, small CPU, two tanks and one-way valve (float stand-in), pump and sprayer (motor stand-in), bottom water sensor (light stand-in), plus the hold-to-run button marked as an added safety rule not in the kids' plan. The LEGO model spec in the README uses the same mapping.

Selecting either model pairs its highlight and opens Python or LEGO blocks by default according to the model. Details appear in the center column between the models, close with Escape, and return focus. The outside columns are wider than the text column. Isolated animation has a separate timer and does not mutate controller state. Reduced motion suppresses animation. All prices are prototype prices; outdoor solar and enclosure are excluded. Existing equipment and shared supplies are not double counted.

Implementation syntax: both inline scripts parse under Node. Root owns browser acceptance and screenshot verification; no accessibility conformance claim is made before that check.

## Purpose and audience

The site is static and multi-page: `demo.html` holds the paired models, part dialog, and simulator; `parts.html` is the parts catalog; `images/` holds the shared component photos as ordinary files. **Meet the parts** is an invitation strip on the explorer linking to the catalog. Select a model component to open its details in the center dialog. Photo source credits appear in the part dialog and catalog. Relevant acronyms and unfamiliar terms are explained in the part dialog; a shared Word helper offers the full glossary in the catalog. The opening wording targets ages 7–10 without changing the controller rules or mentor code examples. Hosting is public GitHub Pages; no server-side code, credentials, or build step.

Ages 7–10 freely explore an imagined outdoor buoy beside its dry LEGO SPIKE equivalent. Selecting a component gives a short plain-language job, a LEGO equivalent and a moving demonstration. Full explanations, Python logic, visual programming blocks and prototype costs stay in the mentor section. No hardware or tested outdoor prototype is assumed.

The homepage credits the kids and presents their problem statement and proposed solutions in their own words, with spelling-only correction. It distinguishes the proposed outdoor idea from the tabletop and dry LEGO visualization. `solution.html` redirects to the homepage's kids'-idea section, and the parts catalog links to the same section.

## Visual system

Use local system sans-serif fonts only. Always use a muted light theme: background #e4eef4, ink #18374c, secondary ink #466479, control #d5e5ee, rule #91adbd, primary #185f83, primary ink #ffffff. Water blue #287ba4, signal green #267b6b, and colored-water orange #b6572b identify physical roles. Shaded SVG surfaces distinguish equipment materials. System dark appearance does not change these colors.

Type: 16px base, 18px classroom body, 20px subheading, 25px section heading, fluid 32–48px title. SVG labels are 12px in its 640-unit drawing, enlarged with the diagram. Space scale: 4, 8, 12, 16, 24, 32, 48px. Control radius 8px; stage radius 16px. Neutral rules and tonal surfaces, no shadows. Numerals are tabular.

## Layout

Layout: simulator - keep the diagram dominant above supporting lessons -> stack (https://github.com/changeroa/StyleGallery/blob/main/patterns/stacking/stack.md); scroll owner: document; anti-patterns: no nested scrolling, fixed heights, or visual reordering of keyboard controls.

The two models sit side by side above simulation controls, stacking below 800px. Picture cards provide alternative selection. Selection expands the main canvas to at most 1800px and changes the model row to three columns: outdoor model, details, LEGO model. Outside columns use 1.12fr each; the middle uses .9fr with a 320px minimum. Details have 28px padding and a viewport-bounded scroll area; the devices remain visible beside it during animation. Below 1050px the three sections stack in that same order with normal document scrolling and 24px padding. Closing details restores the two-model layout. No detail content floats over a device. Cards have 16px padding; code blocks and table cells also have explicit inner spacing.

## Screen contract

Primary interaction: select a component. The part dialog's primary action is **Animate this part**. Priorities: paired models; component explanation/code/cost; optional simulation. Preserve four manual inputs, seven part mappings, play/pause/reset, elapsed time and countdown. Scenario presets and grade prompts were removed. Prototype budget counts shared supplies once, separates optional purchases, and excludes conceptual outdoor solar/enclosure.

Left out: scores, quizzes with stored answers, network data, audio, external assets, decorative badges, and automatic fullscreen. Cloudiness does not establish algae. The output moves food-colored water; it does not demonstrate environmental treatment.

## Behavior and accessibility

Selecting any of the seven components marks the clicked model's part with a pronounced green outline and pale green fill, and its counterpart with blue. Roles reverse when clicking the other model. Picture cards start from the outdoor model. A visible “Same job” sentence names the shared concept, and figure captions say “Selected” or “Same job” so color is not the only cue. The dotted connector joins the outline edges, exits toward the nearest outside edge of each diagram, and uses reserved gutters and a blank rail above the center column. Stacked layouts use an outside vertical gutter. The noninteractive connector tracks resizing, scroll/sticky positions, and animation close-up layout changes. Closing details removes the mapping. Green/blue highlights are an explicit user-requested exception to the default quiet selection styling.

Play advances one simulated second per 1000ms while the page is visible. Pause, reset, and page hiding stop its interval. Next step pauses playback before advancing once. Reset returns time to zero and restores manual inputs to clear/clear/water present/run held. Controller interlocks and one-pulse-per-event rules stay unchanged.

Native controls and SVG buttons have visible keyboard focus. Selection highlights matching parts on both models. Enter/Space opens the labeled details region, Escape closes and restores focus. Hover/focus previews are paired. Code selector buttons use aria-pressed. Reduced-motion explanations remain readable without animation. Browser checks cover these behaviors; they are not a full WCAG certification.

## Motion

Part demonstrations have three labeled phases, each lasting 2.6 seconds. Both devices gain a large inline action close-up; the overview reduces in height so the close-up remains visible beside the center text. Close-ups use the same component artwork as the overview. Motions intentionally exaggerate signal travel, button travel, float level and marker distance; pump rollers rotate and directional flow shows water movement, while the LEGO motor turns an indicator. The optical demo switches between clear/light and cloudy/dark. The controller shows read, decide and command phases. Stop, replay, selecting another part, closing details and hiding the tab all cancel pending phase timers. Completion leaves the final close-up and caption visible, with a Replay button. Demonstrations never write controller inputs or time. Reduced motion disables movement and transitions while retaining all three captions and static before/after states.

The main diagrams use a 600×730 coordinate canvas with separate component zones and labels below each component. Signal routes run behind the artwork and away from labels. The LEGO illustration follows LEGO's official technical reference: a white face/yellow-sided Large Hub with a 5×5 light matrix, white/black two-eye Distance Sensor, white/black single-lens Color Sensor, and white/turquoise Medium Angular Motor with cross-axle output and Technic mounting holes. Hub-button detail views are named as Hub buttons, not separate devices. Reference: https://education.lego.com/en-us/product-resources/spike-prime/downloads/technical-specifications/

## Verification and gaps

Baseline: `.omo/evidence/before.png`, captured by the root QA owner before edits. Initial gaps: diagram constrained beside dense prose; no playback/reset/presentation; no grade-specific predictions; no separate pump countdown. Implementation addresses these gaps. Root owns actual browser verification, screenshot pairs, and accessibility verdict. WCAG 2.2 AA conformance is pending that verification; source inspection alone is not a pass.
