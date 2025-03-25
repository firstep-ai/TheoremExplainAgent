import requests

# 接口地址（请替换成你实际的接口 URL）
url = "http://localhost:8000/generate_mindmap_webpage"

# 请求参数，包含一个 "promote" 字段（值请根据你实际需求填写）
payload = {
    "prompt": """
    # Scene 1 Implementation Plan

    <SCENE_VISION_STORYBOARD_PLAN>
    [SCENE_VISION]
    1.  **Scene Overview**:
        - This scene, titled "Introduction to Equations," serves as the opening segment of our video. It introduces the concept of equations as statements of equality and the idea of using unknown variables to solve problems. The scene establishes foundational knowledge that will help viewers later work through the painting problem.
        - **Visual learning objectives for viewers:** 
            • Visualize the title with a Tex object placed at the top of the screen, clearly within a safe margin of 0.5 units from the top edge.
            • Introduce definitions and simple examples using Tex for general text and MathTex for algebraic expressions. For example, show the equation "x+2=5" and later transform it to "x=3" using MathTex objects.
            • Use a VGroup to collect related equation components ensuring a constant minimum spacing of 0.3 units between each element and all scene borders.
        - How Manim visuals & animations support learning:
            • The scene uses Tex and MathTex to present clear, uncluttered textual definitions and equations.
            • Animations such as Write, Create, and Transform are used to sequentially display the title, definitions, and example equations.
            • All objects are positioned using relative methods (e.g., .to_edge(), .next_to(), .shift()) with explicit enforcement of safe area margins (0.5 units) and a minimum spacing of 0.3 units between objects. 
            • Grouping with VGroup helps maintain spatial consistency thereby reinforcing the visual learning objective.
        - Key concepts to emphasize visually:
            • The utility of equations in solving problems.
            • How unknown variables (represented in MathTex) reveal answers through sequential logical steps.
            • The importance of clear spatial arrangement—maintaining safe area margins and at least 0.3 units spacing—to avoid visual clutter.
            • **Note:** Use MathTex for mathematical components and Tex for general, non-mathematical text.

    [STORYBOARD]
    1.  **Visual Flow & Pacing (Manim Animation Sequence)**:
        - Begin with a slow fade in of the scene title using Tex.
            • Visual Element: Tex object for the title "Introduction to Equations".
            • Positioning: Use .to_edge(UP, buff=0.5) to maintain the top safe area margin, and center horizontally relative to ORIGIN.
            • Animation: Use Write(run_time=2) to animate the title, ensuring a 0.3 unit spacing from the scene edges and from other elements that will appear below.
            • Wait(1) after the title appears to allow viewers to absorb the information.
        - Sub-scene 1: Introduce the definition of an equation.
            • Visual Element: A VGroup consisting of two Tex objects:
                ▪ Tex object: "Equation:" (in bold if desired) 
                ▪ Tex object: "A statement asserting the equality of two expressions."
            • Positioning: The VGroup is centered on screen (use .move_to(ORIGIN)) with a vertical arrangement and a minimum 0.3 unit spacing between the two text blocks.
            • Animation: Use FadeIn for the VGroup with run_time=2.
            • Ensure that the VGroup’s top element aligns at least 0.3 units below the bottom of the title, which is already positioned within the safe area.
            • Wait(1) after the definitions are visible.
        - Sub-scene 2: Showcase a simple algebraic example.
            • Visual Element: A VGroup comprising two MathTex objects:
                ▪ First MathTex: r"x+2=5" 
                ▪ Second MathTex: r"\Rightarrow x=3"
            • Positioning: Position the first MathTex below the definition VGroup using .next_to(definition_group, DOWN, buff=0.3). The second MathTex will be placed to the right of or below the first with relative positioning (e.g., .next_to(first_equation, RIGHT, buff=0.3)) to illustrate progression.
            • Animation:
                ▪ Use Write(run_time=2) to display the initial MathTex "x+2=5".
                ▪ Pause with Wait(1) to let viewers process the equation.
                ▪ Use Transform animation (run_time=2) from "x+2=5" to "x=3" (or display the transformation as an additional MathTex object appearing with a FadeIn) to show how solving the equation results in x=3.
            • Ensure all MathTex objects remain within the safe area margins and maintain at least 0.3 units spacing from all other objects.
            • Wait(1) after the transformation to cement the learning moment.
        - Transition Buffer: Use a Wait(1) following the final animation to provide visual breathing room before transitioning to the next scene in the overall video.

        - **Plugin Suggestion:** For smoother text animations, consider using the `manim_smooth_text` plugin if available, as it can provide enhanced Write and Transform animations that further emphasize the spatial dynamics of grouped text elements.
        
    2.  **Summary of Animation Pacing and Spatial Arrangement**:
        - All textual and mathematical elements (Tex and MathTex objects) are composed using relative positioning methods (.to_edge(), .move_to(), .next_to(), .shift()) to ensure adherence to safe area margins (0.5 units) and constant minimum spacing (0.3 units).
        - Each sub-scene is given a clear pause (via Wait() calls) for visual clarity.
        - Transitions between the title, definitions, and example equations are executed with smooth animations like Write, FadeIn, and Transform, with clear timing (typically 2 seconds per animation) to help reinforce the foundational concepts of equations before moving on to the subsequent painting problem.

    </SCENE_VISION_STORYBOARD_PLAN>

    <SCENE_TECHNICAL_IMPLEMENTATION_PLAN>
    0. **Dependencies**:
        - **Manim API Version**: Target the latest stable release of Manim Community Edition (e.g., v0.17.x).
        - **Allowed Imports**: 
            • from manim import *
            • import numpy as np
        - **Plugins**: 
            • (Optional) manim_smooth_text plugin (if available and desired for enhanced text animation smoothness).
            ### Plugin: manim_smooth_text – Used for its advanced Write and Transform animations that ensure smooth appearance of text within spatial constraints.

    1. **Manim Object Selection & Configuration (Text and Shapes)**:
        - Define all text and mathematical objects using:
            • Tex: For non-mathematical text such as scene titles and descriptions.
            • MathTex: For equations and mathematical expressions (e.g., r"x+2=5" and r"\Rightarrow x=3").
        - **Key Parameters**:
            • Scene Title ("Introduction to Equations"):
                - Object: Tex("Introduction to Equations")
                - Font Size: Use 28 (recommended for titles).
                - Positioning: Use .to_edge(UP, buff=0.5) to ensure the title remains within the safe area (0.5 units from the top edge), centered horizontally.
            • Definition VGroup:
                - Contains:
                    ▪ Tex("Equation:")
                    ▪ Tex("A statement asserting the equality of two expressions.")
                - Font Size: 24 (or adjusted if multi-line)
                - Arranged vertically (using VGroup.arrange with direction=DOWN, buff=0.3) to guarantee a minimum spacing of 0.3 units between text blocks.
                - Positioning: Centered at ORIGIN, but shifted so that its top edge lies at least 0.3 units below the bottom edge of the title.
            • Algebraic Example VGroup:
                - Contains:
                    ▪ MathTex("x+2=5")
                    ▪ MathTex(r"\Rightarrow x=3")
                - Font Size: 24
                - Arrangement:
                    ▪ The first MathTex is placed below the definition VGroup with .next_to(definition_group, DOWN, buff=0.3).
                    ▪ The second MathTex is positioned relative to the first; for example, using .next_to(first_equation, RIGHT, buff=0.3) or arranged vertically (.arrange) to illustrate transformation.
                - Ensure both remain within the safe margins horizontally and vertically.
        - **Text Bounding Box & Overflow Prevention**:
            • Utilize multi-line text if a text block exceeds typical horizontal span.
            • Use the .scale() method if necessary to adjust font sizes.
            • Confirm that every object’s bounding box is validated against a 0.5 unit margin from scene edges using relative positioning methods.

    2. **VGroup Structure & Hierarchy**:
        - Create a VGroup for each related set of objects:
            • title_group: Contains the title Tex object.
            • definition_group: Contains the two Tex objects for the equation definition.
            • example_group: Contains the MathTex objects for the algebraic example.
        - Each VGroup is constructed with an internal arrangement that enforces a minimum vertical/horizontal spacing (buff=0.3).
        - Example grouping:
            • definition_group = VGroup(Tex("Equation:"), Tex("A statement asserting the equality of two expressions.")).arrange(DOWN, buff=0.3)
            • example_group = VGroup(MathTex("x+2=5"), MathTex(r"\Rightarrow x=3")).arrange(DOWN, buff=0.3)
        - Document the grouping purpose in inline comments for clarity and future reusability.

    3. **Spatial Positioning Strategy**:
        - Use exclusively relative positioning methods:
            • The title is positioned with .to_edge(UP, buff=0.5) ensuring a 0.5 unit distance from the top.
            • definition_group uses .next_to(title, DOWN, buff=0.3) ensuring at least 0.3 units spacing from the title’s bottom edge.
            • example_group is positioned via .next_to(definition_group, DOWN, buff=0.3) so it follows immediately below the definition.
            • If the algebraic transformation is shown as an alternate object (or via Transform animation), ensure the transformed object is either aligned or placed relative to the original to maintain spacing.
        - Verify that each object's bounding box remains inside the safe area (0.5 units margin on all sides) by using relative measures from scene borders (e.g., scene.frame, ORIGIN adjustments) rather than absolute coordinates.
        - Insert visual checkpoints (comments) in the code to assert that the width/height of text boxes does not exceed scene limits.
        - Example of relative positioning code:
            • title.to_edge(UP, buff=0.5)
            • definition_group.next_to(title, DOWN, buff=0.3)
            • example_group.next_to(definition_group, DOWN, buff=0.3)
        - Always maintain a minimum spacing of 0.3 units between adjacent text objects to avoid overlap.

    4. **Animation Methods & Object Lifecycle Management**:
        - **Animation Sequences**:
            • Title Animation:
                - Use Write(title, run_time=2) to slowly display the title.
                - Follow with self.wait(1).
            • Definition Group Animation:
                - Use FadeIn(definition_group, run_time=2) to animate the introduction of definitions.
                - Follow with self.wait(1) for absorption time.
            • Algebraic Example Animation:
                - Initially, use Write(example_group[0], run_time=2) for the "x+2=5" MathTex object.
                - Insert self.wait(1) to let viewers process.
                - Use Transform(example_group[0], example_group[1], run_time=2) to illustrate the transformation or alternatively, FadeIn an additional MathTex object for r"\Rightarrow x=3".
                - Wait(1) after transformation.
        - All animations include explicit Wait() calls between steps to enforce pacing and allow the viewer to visually process each sub-scene.
        - Use documented Manim animation methods (e.g., Create, FadeIn, Write, Transform) to ensure each object’s lifecycle is clearly managed (appearance and subsequent removal if needed).

    5. **Code Structure & Reusability**:
        - Structure the code into modular sections:
            • Section for imports and dependency configuration.
            • Section defining all object creation (title, definition_group, example_group).
            • Section detailing positional arrangements with inline comments verifying safe area margins and minimum spacing.
            • Section for the animation sequence within the main construct() method.
        - Use helper functions if similar objects need to be re-created (e.g., def create_text_group(text_list, arrangement=DOWN, buff=0.3): ...).
        - Ensure inline comments refer to the spatial constraint requirements, clarifying that:
            • All objects begin within 0.5 unit margins.
            • Each adjacent object is spaced at least 0.3 units apart.
        - Maintain modularity for easier maintenance and potential reuse in later scenes.

    ***Mandatory Safety Checks***:
        - Verify that every object’s position remains within a 0.5 unit margin from all scene edges.
        - Double-check that the bounding boxes of all Tex/MathTex objects have at least 0.3 units spacing from one another (using .next_to with buff=0.3).
        - Insert Wait() calls between major animation steps to ensure transitions do not clash.
        - Validate that any transformation or scaling of a text object (especially multi-line objects) does not breach the safe area limits.

    </SCENE_TECHNICAL_IMPLEMENTATION_PLAN>

    <SCENE_ANIMATION_NARRATION_PLAN>

    [ANIMATION_STRATEGY]
    1. **Pedagogical Animation Plan:**
        - **Title Introduction (VGroup Concept):**
            • Animation: We start with a Tex object for the title "Introduction to Equations" positioned using .to_edge(UP, buff=0.5). 
            • Animation Type: Write with run_time = 2 seconds.
            • Pedagogical Rationale: The slow reveal of the title within the safe area immediately informs the viewer of the topic and reinforces the visual hierarchy. The 0.5 unit buffer ensures clarity and separation from the edges, creating a professional and engaging opening.
        - **Definition VGroup Presentation:**
            • Construction: Create a VGroup containing two Tex objects:
                - "Equation:" (optionally bold)
                - "A statement asserting the equality of two expressions."
            Arranged vertically with a .arrange(DOWN, buff=0.3) ensuring a minimum spacing of 0.3 units.
            • Positioning: The VGroup is centered at ORIGIN and shifted so that its top is at least 0.3 units below the title’s bottom edge.
            • Animation: FadeIn with run_time = 2 seconds.
            • Pedagogical Rationale: This fade-in highlights the definition in a calm yet noticeable manner. It draws the learner’s focus to the core concept by grouping related text and using the minimum spacing rule to avoid clutter.
        - **Algebraic Example Group with Transformation:**
            • Construction: Build a VGroup with two MathTex objects:
                - First MathTex: "x+2=5" 
                - Second MathTex: r"\Rightarrow x=3"
            Arrange these objects vertically or with a relative transformation using .next_to() ensuring 0.3 units spacing.
            • Positioning: Place the first MathTex immediately below the definition VGroup with .next_to(definition_group, DOWN, buff=0.3), ensuring safe area margins on all sides.
            • Animation Sequence:
                - Write the first MathTex ("x+2=5") with run_time = 2 seconds.
                - Insert a Wait(1) to let the learner process the equation.
                - Either:
                        ▪ Use Transform (run_time = 2 seconds) to morph "x+2=5" into "x=3", or 
                        ▪ FadeIn the second MathTex r"\Rightarrow x=3" next to the first (with correct relative positioning).
                - Insert another Wait(1) post-transformation.
            • Pedagogical Rationale: This sequence visually demonstrates the process of solving an equation. The transformation shows a procedural step-by-step approach while the pauses give the learner extra time to internalize the changes.
        - **VGroup Transition Coordination and Spatial Integrity:**
            • All VGroups and individual objects are animated sequentially using methods like Write, FadeIn, and Transform in a Succession.
            • Each transition maintains a constant minimum spacing of 0.3 units between objects and does not encroach beyond the safe area margin of 0.5 units.
            • Pedagogical Rationale: The coordinated animations guide the viewer’s attention from the title to the definition and then to the example, creating a logical progression and ensuring messages are not lost due to visual clutter.

    2. **Scene Flow - Pedagogical Pacing and Clarity:**
        - **Overall Animation Sequence:**
            - Begin with the title animation (Write title) → Wait(1) → FadeIn definition VGroup (introducing what an equation is) → Wait(1) → Write the algebraic example ("x+2=5") → Wait(1) → Transform to ("x=3") → Wait(1).
            - Each step adheres to the prescribed spatial constraints (safe margins of 0.5 units, 0.3 units minimum between objects).
            - This carefully staged progression helps viewers develop an understanding of equations as equalities and prepares them for the more complex painting problem later in the video.
        - **Transition Buffers for Pedagogical Pauses:**
            - Insert Wait(1) between major steps (after title, after definitions, after the initial equation, after transformation).
            - Pedagogical Reasoning: These pauses provide time for absorption and reflection, ensuring that learners have momentary cognitive breaks before moving on to subsequent information.
        - **Coordination of Timing with Narration:**
            - The narration is synchronized so that key phrases align with the appearance and transformation of each object.
            - Animation cues (like the start of the Write of the title or the Transform of the equation) are precisely matched with narration cues to reinforce the lesson as it unfolds.
            - This synchronization enhances retention and understanding of the material as visual change is coupled with verbal explanation.

    [NARRATION]
    - **Pedagogical Narration Script:**
        "Welcome to Scene 1: Introduction to Equations. Today, we begin by exploring one of the foundational tools in mathematics—equations. (Cue: As the title 'Introduction to Equations' writes onto the screen, pause for 2 seconds.) 
        
        "An equation simply states that two expressions are equal. Here, you'll see the definition appearing right before your eyes. Notice how we group related information together; this grouping helps to manage the complexity of new ideas by breaking them down into digestible parts." (Cue: As the definition VGroup fades in over 2 seconds, wait 1 second.)

        "Now, let's look at a simple algebraic example. Consider the equation x plus 2 equals 5. (Cue: The math expression 'x+2=5' is written slowly on the screen over 2 seconds.) 
        
        "Take a moment to think about what that tells us. If we solve for the unknown value, we discover the simple truth that x equals 3." (Cue: Wait 1 second, then perform a smooth transformation to display 'x=3' over 2 seconds. Wait another 1 second for processing.)

        "Do you notice how the step-by-step transformation helps clarify the relationship between the elements in the equation? Each animation is purposefully timed and arranged—maintaining a clean visual layout with a 0.5 unit margin from the edges and at least 0.3 units between each piece of information—to create a rich learning environment. 

        "Understanding these fundamental operations is essential, not only for solving equations but also for applying this logic to more complex real-world problems, like the painting challenge we'll explore next. Let's take a brief pause before diving deeper into our problem-solving journey." (Cue: Use a short pause as the final Wait(1) concludes.)

    - **Narration Sync - Pedagogical Alignment:**
        • The narration explicitly signals when an animation begins—such as 'as the title writes' or 'watch the transformation'—to help the viewer connect the spoken explanation with the visual cue.
        • Each wait period in the animation is matched with a natural speaking pause in the narration, ensuring that learners have enough time to visually process and mentally grasp the new concept.
        • By synchronizing narration with the creation, transformation, and grouping of text, we ensure that every learning moment is fully supported by both audio and visual cues, maximizing engagement and retention.

    </SCENE_ANIMATION_NARRATION_PLAN>




    # Scene 2 Implementation Plan

    <SCENE_VISION_STORYBOARD_PLAN>
    [SCENE_VISION]
    1.  **Scene Overview**:
        - Scene Story: This scene introduces the painting problem where Tom begins painting a 100-foot fence from the West at 5 ft/hr until Huck joins from the East at 8 ft/hr after 2 hours. After 2 hours of joint work, Tom leaves and Huck completes the remaining work. The key takeaway is to set up the problem with clear visual cues that link the abstract rate problem to a real-world scenario using a fence, icons, and equations.
        - Visual learning objectives for viewers: 
            - Represent the 100-foot fence using a horizontal thin rectangle created with Manim’s Rectangle (as a Shape).
            - Display Tom and Huck using simple Manim objects such as Circle (for icons) with attached Tex labels (e.g., Tex("Tom"), Tex("Huck")).  
            - Represent the rates and times using MathTex objects. For example, include MathTex expressions like r"5\ \text{ft/hr}", r"8\ \text{ft/hr}", and r"2\ \text{hrs}".
            - Use a VGroup to maintain minimum spacing (0.3 units) between the fence, the icons, and any labels or equation groups.
        - How Manim visuals & animations support learning: 
            - Animate the creation of the fence (Rectangle) placed centrally between safe margins (0.5 units from scene edges).
            - Use relative positioning methods (e.g., .next_to(), .align_to(), .shift()) to position Tom’s icon at the left (West) end and Huck’s icon at the right (East) end of the fence.
            - Animate the icons with Create and FadeIn effects while ensuring that no two objects violate the 0.3 units minimum spacing constraint.
            - Introduce the key numerical elements (rate labels and time durations) with MathTex and group them using VGroup for clearer spatial control.
            - All elements are animated with transitions (e.g., Wait(), Transform(), FadeOut) with careful timing (run_time parameters) to maintain clear pacing.

    [STORYBOARD]
    1.  **Visual Flow & Pacing (Manim Animation Sequence)**:
        - Begin with a brief Title display using Tex "Problem Setup" centered at the top within the safe margin, then use Wait(1) before proceeding.
        - **Sub-scene 1: Introduce the Fence**
            - Visual Element: A long, thin Rectangle to represent the 100-foot fence.
            - Animation Sequence:
                a. Create the Rectangle using Create(animation) centered horizontally with its width spanning nearly the full scene width while leaving a 0.5 unit margin on left and right. Use .to_edge(LEFT, buff=0.5) and .to_edge(RIGHT, buff=0.5) indirectly by relative positioning.
                b. Place small evenly spaced markers along the rectangle’s length using small Line segments (or Dots) if needed.
                c. Run_time: 2 seconds.
                d. Ensure that the rectangle and markers follow the safe area margin and maintain a minimum separation of 0.3 units from any subsequent icon placements.
                e. Wait(1) after creation.
        - **Sub-scene 2: Position Tom and Huck**
            - Visual Element: Two Circle icons with attached Tex labels ("Tom" and "Huck").
            - Animation Sequence:
                a. Create Tom’s icon first:
                    - Use Circle() for Tom.
                    - Attach a Tex label "Tom" below or next to the circle using .next_to() with a buff of 0.3 units.
                    - Position Tom’s icon relative to the west end of the Rectangle by aligning Tom’s icon with the Rectangle’s left edge (using .align_to(fence, LEFT)) and then shifting it upward slightly for clarity.
                b. Create Huck’s icon similarly:
                    - Use Circle() with Tex label "Huck".
                    - Position Huck’s icon relative to the east end of the Rectangle by aligning with the Rectangle’s right edge (using .align_to(fence, RIGHT)) and shifting.
                c. Use Create animations for the icons (run_time: 1.5 seconds each) ensuring a 0.3 unit gap is maintained between the icons and the fence.
                d. Wait(1) once both are in place.
        - **Sub-scene 3: Illustrate the Painting Process**
            - Visual Element: Arrows and MathTex expressions.
            - Animation Sequence:
                a. For Tom (starting painting from the West end):
                    - Create an Arrow (using Arrow or Line with an arrow tip) pointing rightward along the fence. Use .next_to(Tom_icon, RIGHT, buff=0.3) ensuring the arrow remains inside the safe area.
                    - Overlay a MathTex expression r"5\ \text{ft/hr}" above or beside the arrow using .next_to(arrow, UP, buff=0.3).
                    - Animate arrow creation via Create(arrow, run_time=1) and Write(rate_label, run_time=1).
                    - Wait(1).
                b. For Huck (joining 2 hours later, from the East end):
                    - Animate Huck’s arrow starting from the east end pointing left along the fence. Position using .next_to(Huck_icon, LEFT, buff=0.3).
                    - Attach a MathTex expression r"8\ \text{ft/hr}" using .next_to(arrow, UP, buff=0.3).
                    - Use Create(arrow) and Write(rate_label) with run_time 1.
                    - Wait(1).
                c. Display a MathTex group (using VGroup) summarizing "2 hrs" for the solo work and the subsequent "2 hrs" for joint work. Position this group above the fence, centered relative to the fence’s ORIGIN, ensuring a 0.3 unit clearance from the fence.
                d. Wait(1).
        - **Sub-scene 4: Transition to the Problem Question**
            - Visual Element: A Tex label with the question "How many more hours will Huck work than Tom?" shown at the bottom within safe area margins.
            - Animation Sequence:
                a. Use FadeIn(Tex(...)) for the question text, positioned using .to_edge(DOWN, buff=0.5) and ensuring a minimum gap of 0.3 units from the fence.
                b. Run_time: 1.5 seconds.
                c. Wait(2) to allow viewers to read the question.
        - Transition: Use Wait() calls (1-2 seconds) between sub-scenes to ensure visual clarity and smooth pacing.

    Note:
    - All objects (fence, icons, arrows, labels, and equations) are positioned using relative positioning methods (e.g., .next_to(), .align_to(), .shift()) relative to ORIGIN or to other objects, with a strict adherence to the 0.5 unit safe margins and 0.3 unit minimum spacing.
    - **Plugin Suggestion:** Consider using the "manim-safetensors" plugin (if available) for advanced relative positioning helpers to guarantee margin constraints.
    </SCENE_VISION_STORYBOARD_PLAN>

    <SCENE_TECHNICAL_IMPLEMENTATION_PLAN>
    0. **Dependencies**:
        - **Manim API Version**: Targeting the latest stable release of Manim Community Edition.
        - **Allowed Imports**: Import from "manim" and "numpy". No external assets will be used. An optional plugin "manim-safetensors" is referenced (see note below) to assist with advanced relative positioning:
            ### Plugin: manim-safetensors - This plugin is suggested to ensure automatic adherence to safe area margins and minimum spacing, though core Manim relative methods (next_to, align_to, shift) are fully capable if used with care.
        
    1. **Manim Object Selection & Configuration (Text and Shapes)**:
        - Objects used:
            • Title: Tex("Problem Setup")
                - Font size: 28
            • Fence: Rectangle (long, thin) representing the 100-foot fence.
                - Dimensions calculated relative to scene width leaving 0.5 unit margin on left/right, and with a modest height so that it is clearly visible.
            • Markers: Optional small Lines or Dots along the fence with minimum spacing 0.3 units apart.
            • Icons:
                - Tom’s icon: Circle() with attached Tex("Tom").
                    - Tex label positioned using .next_to() with buff=0.3 units.
                - Huck’s icon: Circle() with attached Tex("Huck").
                    - Tex label positioned using .next_to() with buff=0.3 units.
            • Arrows:
                - Tom’s arrow: Arrow pointing right (from Tom’s icon) along the fence using Arrow() with buff=0.3.
                - Huck’s arrow: Arrow pointing left (from Huck’s icon) along the fence using Arrow() with buff=0.3.
            • Math Equations:
                - MathTex expressions: r"5\ \text{ft/hr}" and r"8\ \text{ft/hr}" for rates.
                - Additional MathTex for time durations, e.g., r"2\ \text{hrs}".
                - All MathTex objects are used for formula expressions (font size: ~24 recommended).
        - All objects are configured to be within safe area margins (0.5 units from scene edges) and maintain at least a 0.3 unit spacing edge-to-edge to avoid any bounding-box overflow.

    2. **VGroup Structure & Hierarchy**:
        - Group objects into VGroups for efficient spatial management:
            • fence_group: Contains the Rectangle and any markers placed on it.
            • icon_group: Contains Tom’s and Huck’s icons (each comprising a Circle and its attached Tex label). They are separately created, then added into a VGroup ensuring at least 0.3 unit spacing.
            • arrow_group: Contains arrows for Tom’s and Huck’s painting directions along with their corresponding MathTex rate labels.
            • time_group: A VGroup compiling MathTex expressions for "2 hrs" labels.
        - Each VGroup is aligned centrally where needed using .arrange() with a buff of 0.3 units.

    3. **Spatial Positioning Strategy**:
        - Positioning uses exclusively relative methods (next_to, align_to, shift):
            • Title: Placed at the top center using .to_edge(UP, buff=0.5) while ensuring safe margin.
            • Fence (Rectangle): Centered horizontally with its left and right edges exactly 0.5 units away from the scene edges.
                - Use .to_edge(LEFT, buff=0.5) and .to_edge(RIGHT, buff=0.5) indirectly through relative scaling.
            • Tom’s Icon:
                - Positioned relative to the left edge of the fence using .align_to(fence, LEFT) then shifted upward slightly.
                - The attached Tex label "Tom" uses .next_to(Tom_icon, DOWN, buff=0.3) to ensure readability.
            • Huck’s Icon:
                - Aligned to the right edge of the fence using .align_to(fence, RIGHT) then shifted upward.
                - Its Tex label "Huck" positioned similarly using .next_to(Huck_icon, DOWN, buff=0.3).
            • Arrows:
                - Tom’s arrow: Positioned using .next_to(Tom_icon, RIGHT, buff=0.3) and adjusted to run parallel to the fence.
                - Huck’s arrow: Positioned using .next_to(Huck_icon, LEFT, buff=0.3).
                - Rate labels (MathTex for "5 ft/hr" and "8 ft/hr") attached using .next_to(arrow, UP, buff=0.3). 
            • Time Group:
                - Positioned as a VGroup above the fence using .next_to(fence, UP, buff=0.3) and centered relative to the fence’s origin.
            • Question Text:
                - A Tex label "How many more hours will Huck work than Tom?" is placed at the bottom within safe margins using .to_edge(DOWN, buff=0.5) ensuring at least a 0.3 unit gap from the fence.
        - Special precautions are included to safeguard text bounding boxes, especially for multi-line Tex expressions. Relative positioning using buffers avoids any overflow beyond the safe area.

    4. **Animation Methods & Object Lifecycle Management**:
        - Animation Sequence:
            • Title:
                - Animate using Write(title, run_time=1) and hold with Wait(1).
            • Sub-scene 1: Introduce the Fence
                - Animate Rectangle creation with Create(fence, run_time=2).
                - Optionally animate small markers using Create/Draw for each marker.
                - Follow with Wait(1).
            • Sub-scene 2: Position Tom and Huck Icons:
                - Animate Tom’s icon creation with Create(Tom_icon, run_time=1.5).
                - Simultaneously attach Tex("Tom") using Write(label, run_time=1.5).
                - Repeat for Huck’s icon, ensuring 0.3 unit spacing from the fence.
                - Wait(1) after placement.
            • Sub-scene 3: Illustrate the Painting Process:
                - For Tom:
                    - Create Tom’s arrow with Create(arrow, run_time=1).
                    - Write MathTex("5\\ \\text{ft/hr}") using Write(rate_label, run_time=1).
                    - Wait(1).
                - For Huck:
                    - Create Huck’s arrow (pointing left) with Create(arrow, run_time=1).
                    - Write MathTex("8\\ \\text{ft/hr}") beside the arrow.
                    - Wait(1).
                - Display the time_group using Write or FadeIn with run_time=1.
                - Wait(1) after displaying.
            • Sub-scene 4: Transition to the Problem Question:
                - Animate Tex("How many more hours will Huck work than Tom?") with FadeIn (run_time=1.5).
                - Wait(2) to allow the audience lead time to read.
        - All animations include Wait() calls between sub-scenes to ensure clear pacing and to respect the minimum spacing and safe margin constraints.

    5. **Code Structure & Reusability**:
        - Code Organization:
            • Define helper functions to create icons (create_icon(label_text, position_reference)) to ensure consistency.
            • Create separate functions for:
                - build_fence(): Returns the Rectangle (and optional markers) positioned relative to safe area margins.
                - build_icon(): Creates and returns a Circle with an attached Tex label.
                - build_arrow_with_label(): Constructs an Arrow and positions an adjacent MathTex rate label.
            • The main construct() method sequences the sub-scenes with inline comments documenting each stage, referencing the spatial constraints used.
        - Inline comments and function headers will reference Manim documentation methods (e.g., next_to, align_to) and plugin documentation if "manim-safetensors" is employed.

    ***Mandatory Safety Checks***:
        - Safe Area Enforcement: All objects are positioned with reference to scene edges using .to_edge() and relative methods to guarantee a 0.5 unit margin.
        - Minimum Spacing Validation: Buffers (buff=0.3) are consistently applied via .next_to() and .arrange() to maintain at least 0.3 unit spacing between objects.
        - Transition Buffers: Use explicit Wait() calls (1-2 seconds) to separate each animation step and sub-scene.
        - Text Bounding Box: All Tex and MathTex objects are sized appropriately based on content (titles at 28; labels/formulas at 24) and are positioned using relative methods to prevent any overflow from the safe area.

    </SCENE_TECHNICAL_IMPLEMENTATION_PLAN>

    <SCENE_ANIMATION_NARRATION_PLAN>

    [ANIMATION_STRATEGY]
    1. **Pedagogical Animation Plan:**
    - Overall, the scene is divided into four pedagogical sub-sections: 
        a. Title and problem introduction,
        b. Introducing the fence,
        c. Positioning Tom and Huck,
        d. Illustrating the painting process and stating the problem question.
    - **Parent VGroup Transitions:**
        • A VGroup (named fence_group) is used to hold the fence Rectangle and its markers. It is created using Create(fence_group, run_time=2) while ensuring the fence spans the scene horizontally with 0.5 unit safe margins. This grouping highlights the physical framework of the problem, helping learners visualize the entire 100-foot fence as a base for all calculations.
        • A VGroup (named icon_group) contains Tom’s and Huck’s icons (each created as a Circle with an attached Tex label). They are sequentially animated with Create for the Circles and Write for the labels. The icons are aligned relative to the fence’s left and right edges by using .align_to() and .next_to() with a buff of 0.3 units. This grouping draws the learner’s attention to the starting positions.
        • A VGroup (named arrow_group) is created for the painting arrows and the attached MathTex rate labels. The arrows for Tom (pointing right) and Huck (pointing left) are animated using Create(arrow, run_time=1) with their corresponding rate MathTex (e.g., "5 ft/hr" and "8 ft/hr") written with Write(rate_label, run_time=1). The pedagogical rationale is to clearly map the rates to the respective icons, emphasizing how direction and rate are key to solving the problem.
        • A separate VGroup (named time_group) is used to group MathTex expressions for time durations ("2 hrs" for solo and joint work). It is positioned using next_to(fence, UP, buff=0.3) and animated with a FadeIn (run_time=1). This visual grouping reinforces the timeline of events.
    - **Element Animations within VGroups:**
        • Title: The title "Problem Setup" is centered at the top with Write(title, run_time=1). This immediately informs viewers of the scene’s focus.
        • Fence: The fence Rectangle is drawn with Create(fence, run_time=2) ensuring its width extends nearly to the scene edges (maintaining 0.5 unit margin). Small markers (using Dots or small Lines) can be created on the fence with spacing at least 0.3 units apart to further solidify the concept of the 100-foot measure.
        • Tom’s Icon: Created with Create(Tom_icon, run_time=1.5) and its label appears adjacent (via Write(label, run_time=1.5)). The icon is aligned to the left edge of the fence (using .align_to(fence, LEFT)) and is shifted slightly upward to avoid overlap. This helps viewers associate the left (West) side with Tom.
        • Huck’s Icon: Similarly, Huck’s icon is created with Create(Huck_icon, run_time=1.5) next to the right edge (using .align_to(fence, RIGHT)) and shifted upward. Minimum spacing of 0.3 units is maintained between the icon and the fence. This symmetric placement visually contrasts the starting points.
        • Arrows and Rate Labels:
            - Tom’s Arrow: An Arrow is created with Create(arrow, run_time=1) originating from Tom’s icon and extending rightward along the fence, with the MathTex "5 ft/hr" placed above it using .next_to(arrow, UP, buff=0.3). This animation reinforces how Tom’s solo rate is applied.
            - Huck’s Arrow: In the same manner, an arrow is drawn from Huck’s icon pointing left with Create(arrow, run_time=1) and labelled with "8 ft/hr" via Write(rate_label, run_time=1). This clearly shows Huck’s counter-direction and his higher painting rate.
        • Time Labels: A VGroup containing MathTex expressions for "2 hrs" (one for the initial solo painting phase and one for the joint painting phase) is arranged above the fence. It is animated via Write or FadeIn (run_time=1) to help students follow the timeline.
        • Final Problem Question: A Tex label stating "How many more hours will Huck work than Tom?" is faded in at the bottom using FadeIn (run_time=1.5), ensuring it sits within the bottom 0.5 unit safe margin, with at least 0.3 units spacing from the fence.
    - **Pedagogical Rationale for Transitions:**
        • The sequential transitions (using Wait() calls of 1–2 seconds between each sub-section) give learners time to absorb each visual element before introducing new ones.
        • Parent VGroup transitions (e.g., shifting the entire icon_group or arrow_group into position) guide the viewer's focus onto the parts of the diagram where the key mathematical relationships are being established.
        • Each Create and Write animation is carefully timed (run_time values between 1 and 2 seconds) and coordinated so that viewers can logically link the text and visual elements, creating a predictable flow that reinforces the real-world application of equations.

    2. **Scene Flow - Pedagogical Pacing and Clarity:**
    - **Overall Animation Sequence:**
        a. The scene begins with the title "Problem Setup" appearing at the top, immediately orienting the learner to the subject.
        b. Next, the fence is introduced using a horizontally centered Rectangle; markers are added to emphasize its 100-foot length.
        c. Then, Tom’s and Huck’s icons are placed at the respective West and East ends of the fence, with their labels clearly indicating their roles.
        d. The painting process is illustrated by animating arrows along the fence with corresponding rate labels, immediately followed by time duration MathTex expressions placed above the fence.
        e. Finally, the question "How many more hours will Huck work than Tom?" is displayed at the bottom, transitioning the learner into thinking about the problem.
    - **Transition Buffers for Pedagogical Pauses:**
        • A Wait(1) is inserted after the title animation to allow initial orientation.
        • After the fence is drawn, a Wait(1) gives time for learners to appreciate the real-world context.
        • Once each icon is displayed, a brief Wait(1) ensures that learners see the starting positions clearly before proceeding.
        • After each arrow (for Tom and Huck) and their rate labels, Wait(1) is used to let students process the rates in context.
        • A final Wait(2) after the appearance of the problem question allows learners to re-read and internalize the question.
        • These timed pauses are explicitly chosen to provide learners with processing time, ensuring that each visual element is fully absorbed before introducing new information.
    - **Coordination of Animation Timing with Narration:**
        • The narration script refers explicitly to when the title appears, when the fence is drawn, and when the icons and arrows animate. This synchronization ensures that as the lecturer explains each concept step-by-step, the visual cues are perfectly aligned.
        • For example, when discussing Tom’s work rate, the narration will prompt the viewer’s attention to the arrow extending from Tom’s icon and the "5 ft/hr" label, facilitated by the corresponding animation (run_time=1).
        • The narration indicates a pause (via a narrative cue such as “Take a moment to notice…”) that exactly coincides with the Wait(1) calls, reinforcing the pedagogical rhythm.

    [NARRATION]
    - **Pedagogical Narration Script:**
    "Welcome to Scene 2 – Problem Setup. In this scene, we are going to explore a real-world problem where two characters, Tom and Huck, work together to paint a 100-foot fence. 
    
    [At the moment the title 'Problem Setup' appears at the top (run_time: 1 second, Wait: 1 second)]
    'Notice the title up top sets the stage—this problem is all about applying equations to real situations.'
    
    [As the fence is drawn in (run_time: 2 seconds, followed by a Wait: 1 second)]
    'Here we have the fence, a clear representation of 100 feet, horizontally aligned across our screen. Think of these 100 feet as the total work that needs to be done, our starting point for setting up the equation.'
    
    [When Tom’s icon is created on the left and Huck’s on the right (each with run_time: 1.5 seconds, with subsequent Wait: 1 second)]
    'Observe the two painters positioned at opposite ends: Tom starts at the West end, and two hours into painting, Huck joins him at the East end. Their starting positions play a crucial role in how we set up our equations to solve the problem.'
    
    [As Tom’s arrow appears (run_time: 1 second) with the “5 ft/hr” label and followed by a Wait(1)]
    'Tom begins his work at a steady pace of 5 feet per hour, symbolized by the arrow moving towards the right. This rate is fundamental to calculating how quickly he covers the fence.'
    
    [When Huck’s arrow is introduced (run_time: 1 second) with the “8 ft/hr” label and followed by a Wait(1)]
    'Two hours later, Huck starts painting from the other end at an increased pace of 8 feet per hour. Notice how the arrow from his icon points left, indicating his approach to meet Tom’s progress from the opposite side.'
    
    [As the time duration MathTex expressions '2 hrs' appear above the fence (run_time: 1, Wait: 1)]
    'Along the top, we see the duration labels that frame each phase of work. These time markers help us break down the problem: first, Tom works alone for 2 hours, and then both work together for another 2 hours before Tom steps away.'
    
    [When the final problem question is faded in at the bottom (run_time: 1.5 seconds, Wait: 2 seconds)]
    'Now, here’s a critical question for you: How many more hours will Huck work than Tom once Tom leaves? Reflect on the rates, the timings, and the portions of the fence each has painted to answer this. Take a moment to process this before we dive further into solving it.'
    
    'Building on what we’ve just visualized, keep these details in mind as they will be key when we set up and solve the equations in the next scene. Let’s now transition to breaking down the equations step by step in the upcoming segment.'
    
    - **Narration Sync - Pedagogical Alignment:**
    • The narration precisely cues the viewer to each visual element as it appears. For example, when the narrator mentions 'Tom begins his work at a steady pace of 5 feet per hour,' the arrow with the "5 ft/hr" label has just been created, ensuring that audio and visuals reinforce each other.
    • The Wait() calls (1–2 seconds) after each key animation act as a pause, allowing learners to fully digest the visual before new concepts are introduced.
    • By explicitly referencing the positions (e.g., 'West end for Tom' and 'East end for Huck') and timing labels, the narration drives home the connection between the real-world scenario and the abstract representation of equations.
    • This tight coordination ensures that each mathematical concept is introduced only after the corresponding visual is clearly established, maximizing comprehension and retention.

    </SCENE_ANIMATION_NARRATION_PLAN>



    # Scene 3 Implementation Plan

    <SCENE_VISION_STORYBOARD_PLAN>
    [SCENE_VISION]
    1.  Scene Overview:
        - Story: In this scene “Constructing Equations,” we break the painting problem into two logically distinct segments – Tom’s initial work and the combined work with Huck – and then model the remaining work with an unknown variable. The scene emphasizes forming accurate equations from verbal descriptions.
        - Key takeaway: Viewers learn to translate a word problem into a set of equations using clearly arranged visual steps. This scene illustrates how time segments and painting rates are modeled mathematically.
        - Visual learning objectives:
            • Visualize each equation step using MathTex objects.
            • Group related equations with VGroup to maintain clarity and enforce a minimum spacing of 0.3 units between groups.
            • Create a split-panel layout with left-side equation groups and right-side diagram illustrations (using shapes like Line and Arrow) to represent the fence and painting progress.
            • Use Tex sparingly for labels like “Tom’s progress” and “Huck’s progress” positioned above their respective sections.
        - How visuals & animations support learning:
            • Use MathTex for equations ensuring each component is created with the Write animation.
            • Group equations using VGroup for unified movement and to ensure 0.3 units spacing from each other, and align them starting at the safe area margin (0.5 units from the left).
            • Illustrate the fence by drawing a long line (representing 100 feet) with Arrow objects to indicate starting points at West and East ends.
            • Position the diagram on the right side with at least 0.3 units separation from the equations, ensuring both reside within the 0.5 unit safe margins on all sides.
            • If available, a plugin such as “manim_vector_plugin” could be used for enhanced arrow drawing; however core Manim objects (Line, Arrow) suffice.

    [STORYBOARD]
    1. Visual Flow & Pacing (Manim Animation Sequence):
        - Overall sequence: Start by displaying the title (using Tex) and a brief outline label “Constructing Equations” at the top center (within safe margins). Then split the scene into two vertical panels using a VGroup: 
                • Left Panel: Equations laid out vertically.
                • Right Panel: A simplified fence diagram with directional arrows.
        - Ensure all objects maintain at least 0.3 units spacing between each other and from the 0.5 unit safe zone.

        - Sub-scene 1: Introducing Tom’s Progress
            • Visual Element: MathTex equation representing Tom’s work (e.g., "5 \\text{ feet/hr} \\times 2 \\text{ hr} = 10 \\text{ ft}") created using MathTex and grouped in a VGroup.
            • Animation Sequence:
                    ▸ Create the MathTex equation with Write animation (run_time=2.0) and position it aligned to the left margin (use .to_edge(LEFT, buff=0.5)) while ensuring a vertical gap of 0.3 units from any top elements.
                    ▸ Add a Tex label “Tom’s progress” right above the equation using Write and align it to the equation with a .next_to() method with a buffer of 0.3 units.
                    ▸ On the right panel, simultaneously FadeIn a Line to represent the fence (drawn horizontally) with Arrow objects at the West end to illustrate Tom’s starting point, ensuring the entire diagram is shifted to be within the safe area and at least 0.3 units from the equation panel.
                    ▸ Pause with a Wait(1) call for clarity.

        - Sub-scene 2: Introducing Combined Progress and Huck’s Involvement
            • Visual Element: Display a new MathTex equation for the progress during the combined work: e.g., 
                "5\\cdot2 + (5+8)\\cdot2" (representing Tom’s and Huck’s combined work) along with a variable term "x" representing extra hours Huck worked.
            • Animation Sequence:
                    ▸ Use Transform to morph the previous MathTex into the new combined equation, or FadeOut the old group and Write the new VGroup of equations. The VGroup groups separate equations: one for Tom’s solo work on the left and one for Huck’s additional work expressed as an unknown.
                    ▸ Position the new VGroup of equations below the first group with a .next_to() call (with buffer 0.3) to maintain vertical spacing.
                    ▸ Add a Tex label “Huck’s progress” just above the new equation group.
                    ▸ On the right panel, update the fence diagram: add an Arrow from the East end (using Arrow objects) showing Huck’s starting position and another arrow along the fence to indicate the overlapping work. Use FadeIn and Create animations (run_time=2) for these elements, ensuring they remain at least 0.3 units from the equations.
                    ▸ Pause with Wait(1) to allow viewers to absorb the changes.
            • Emphasize spatial clarity by ensuring both equation sections and the diagram switch positions gradually (using Shift or Transform animations) and that all safe area and spacing requirements (0.5 unit margins, 0.3 unit gaps) are respected.

        - Sub-scene 3: Final Connection and Transition
            • Visual Element: Highlight the final equation modeling “how many more hours Huck works than Tom.”
            • Animation Sequence:
                    ▸ Use a Circumscribe animation on the variable part of the equation (e.g., the "x" term) to draw attention.
                    ▸ Optionally, display a brief Tex explanation (e.g., "x = extra hours Huck works") below the equation using Write, ensuring a 0.3 unit gap from the equation.
                    ▸ Conclude with a slow zoom-out (if desired) to show both equation groups and the diagram in proper alignment within the safe margins.
                    ▸ End with a Wait(2) to allow the viewer to review all elements.

        - Transition Buffers: Use Wait(1) calls between sub-scenes to ensure smooth visual pacing.
        - All object positions use relative positioning methods such as .to_edge(), .next_to(), and .shift() based on the ORIGIN and safe area boundaries (0.5 units). Horizontal and vertical buffers are set to a minimum of 0.3 units to avoid any overlap.
    </SCENE_VISION_STORYBOARD_PLAN>

    <SCENE_TECHNICAL_IMPLEMENTATION_PLAN>
    0. **Dependencies**:
        - **Manim API Version**: Target the latest stable release of Manim Community Edition.
        - **Allowed Imports**: 
            • manim  
            • numpy  
            • (Optional) Any established and documented Manim plugin (e.g., manim_vector_plugin) if advanced arrow drawing is required.
        - **Plugin Justification**: If using a plugin (e.g., manim_vector_plugin), include a comment such as:
            ### Plugin: manim_vector_plugin - Provides enhanced arrow and vector drawing capabilities beyond core Manim.

    1. **Manim Object Selection & Configuration (Text and Shapes)**:
        - **Mathematical Expressions & Equations**:
            • Use MathTex for all equations to ensure proper LaTeX formatting.  
                Example: MathTex("5\\,\\text{ft/hr} \\times 2\\,\\text{hr} = 10\\,\\text{ft}")
            • Use Tex for non-mathematical labels and titles.  
                Example: Tex("Tom's progress")
        - **Shapes & Diagrams**:
            • Use Line for drawing the fence.
            • Use Arrow to indicate starting points (one at the West end for Tom, one at the East end for Huck) and directional painting progress.
        - **Text Configuration**:
            • Title text (if needed) with font size ~28.
            • Side labels and formulas with font size ~24 (or slightly smaller for longer expressions).
            • Ensure bounding boxes for all text and equations remain within safe area margins (0.5 units from edges).
            • Use multi-line layout and relative positioning with .next_to() when text length might risk overflow, ensuring a buffer of at least 0.3 units.
        - **Safe Area Enforcement**:
            • All objects are initially positioned using .to_edge(LEFT) or .to_edge(RIGHT) with a buff=0.5.
            • Subsequent objects use .next_to() with buff=0.3 to ensure no text bounding box overflow.

    2. **VGroup Structure & Hierarchy**:
        - **Equation Groups**:
            • Create one VGroup for Tom’s progress (e.g., label and equation for solo work).
            • Create a second VGroup for the combined work including Huck’s involvement.  
            • These groups help maintain a minimum inter-object spacing of 0.3 units vertically.
        - **Diagram Grouping**:
            • A separate VGroup is used for the fence diagram and its arrows.
        - **Grouping Purpose**:
            • "formula_group": Contains all MathTex equations.
            • "diagram_group": Contains visuals (Line and Arrow objects) for the fence.
        - **Positioning within VGroups**:
            • Set the left VGroup to align to the safe left margin (0.5 units) and place the right VGroup (the diagram) with at least 0.3 units spacing from the left group, both within the scene’s safe areas.

    3. **Spatial Positioning Strategy**:
        - **Relative Positioning Methods**:
            • Use .to_edge(), .next_to(), .align_to(), and .shift() exclusively.
        - **Layout Specification**:
            • Top-center: A Tex title displaying “Constructing Equations” within safe margins.
            • Left Panel (Equation Area):
                    - First, position the "Tom's progress" label and corresponding MathTex (e.g., "5 \\text{ft/hr} \\times 2 \\text{hr} = 10 \\text{ft}") using .to_edge(LEFT, buff=0.5).
                    - Place the "Tom's progress" label above its equation using .next_to() with buff=0.3.
            • Vertical Spacing: After the first VGroup, place the combined work group (with the transformed equation "5\\cdot2 + (5+8)\\cdot2 \\; + \\; x") below, again using .next_to() with a buff=0.3.
            • Right Panel (Diagram Area):
                    - Draw a horizontal Line to represent the 100 ft fence within safe margins.
                    - Place Arrow objects at both ends:
                        • West side arrow for Tom’s starting position.
                        • East side arrow for Huck’s starting position (added in sub-scene 2).
                    - Ensure the entire diagram is shifted relative to the left panel so that there is at least 0.3 units spacing between the panels.
        - **Text Bounding Box & Overflow Prevention**:
            • Use relative positioning and check bounding box dimensions.
            • For longer text or multi-line equations, split the content by adding line breaks and using Tex/multi-line MathTex to prevent horizontal overflow.

    4. **Animation Methods & Object Lifecycle Management**:
        - **Animation Sequences**:
            • Sub-scene 1 (Tom’s progress):
                    - Animate MathTex equation with Write(animation, run_time=2.0).
                    - Animate label ("Tom's progress") with Write immediately above the equation.
                    - Simultaneously, FadeIn a Line (fence) and create Arrow (Tom’s starting point on the left) using Create (run_time=2).
                    - Include a Wait(1) call after these animations.
            • Sub-scene 2 (Combined Progress with Huck’s involvement):
                    - Transform the existing MathTex into a new one, or FadeOut the previous VGroup and Write the new combined equation VGroup that includes both Tom’s and Huck’s work ("5\\cdot2 + (5+8)\\cdot2 + x").  
                    - Position the new group below the previous one with .next_to(buff=0.3).
                    - Animate the addition of a "Huck's progress" label above the new group.
                    - Update the diagram by FadeIn additional Arrow(s) at the East end and along the fence to denote overlapping work; use Create animations (run_time=2).
                    - Include a Wait(1) call.
            • Sub-scene 3 (Final Connection and Transition):
                    - Highlight the variable "x" in the equation using a Circumscribe animation.
                    - Optionally, add a Tex explanation (e.g., "x = extra hours Huck works") below the equation using Write with a .next_to(buff=0.3).
                    - Conclude with a slow zoom-out using self.play(self.camera.frame.animate.scale(0.9)) ensuring all elements are still within safe margins.
                    - End the scene with Wait(2) for final review.
        - **Transition Buffers**:
            • Insert explicit Wait(1) calls between sub-scenes to ensure viewers have time to absorb each step.
        - **Lifecycle Management**:
            • Each new scene element overlaps minimally by using relative shifting and grouping.
            • FadeOut methods are used to remove old groups when transforming to new equations to prevent clutter.

    5. **Code Structure & Reusability**:
        - **Modular Functions**:
            • Create helper functions (e.g., create_equation_group(label_text, math_expr)) to generate the VGroups for equations with proper spacing.
            • Similarly, create a function for constructing the fence diagram (e.g., create_fence_diagram()) that returns a VGroup containing the Line and Arrow objects.
        - **Organization**:
            • Begin with dependency imports and configuration (including font size constants and safe margin definitions).
            • Define individual object creation segments followed by animation sequences in the main construct() method.
            • Insert inline comments that reference the Manim Documentation for each function (e.g., usage of .to_edge(), .next_to(), Write, Create, etc.).
        - **Reusability Consideration**:
            • Ensure that all relative positioning parameters (buff values such as 0.5 and 0.3) are defined as constants or passed as parameters so adjustments can be efficiently made.
            • Reuse VGroup structures to animate grouped elements together.
        
    ***Mandatory Safety Checks***:
        - Verify that every text, MathTex, and shape remains at least 0.5 units from scene edges and that no two objects’ bounding boxes are closer than 0.3 units.
        - Check bounding boxes for multi-line text objects to guarantee no overflow occurs.
        - Confirm that every transition (Write, Transform, FadeIn, Create, etc.) includes a safe transition buffer (Wait(1)) to avoid sudden changes.
    </SCENE_TECHNICAL_IMPLEMENTATION_PLAN>

    <SCENE_ANIMATION_NARRATION_PLAN>

    [ANIMATION_STRATEGY]
    1. **Pedagogical Animation Plan:**
        - **Parent VGroup Transitions:**
            • We begin by creating two primary VGroups: one for the left panel (equation groups) and one for the right panel (fence diagram). Both groups are anchored by safe margins (0.5 units from scene edges) and respect a 0.3 unit inter-object spacing.
            • In Sub-scene 1, the "Tom’s progress" VGroup is shifted into view using a Write animation for its label (Tex: "Tom’s progress") and accompanying MathTex equation ("5\\,\\text{ft/hr} \\times 2\\,\\text{hr} = 10\\,\\text{ft}") with run_time=2.0. Simultaneously, the fence diagram group on the right is FadeIn-ed (run_time=2.0) starting with a horizontal Line (representing the 100 ft fence) and an Arrow at the West end. 
                - Pedagogical Rationale: This coordinated entrance draws the viewer’s attention to both the verbal explanation and its visual counterpart, reinforcing the concept of rate and time.
            • In Sub-scene 2, the original VGroup for Tom’s solo work is either transformed or faded out and replaced by a combined progress VGroup that features the new MathTex expression ("5\\cdot2 + (5+8)\\cdot2 + x"). This group is introduced below the initial group using a .next_to() call (buffer=0.3) and a new label ("Huck’s progress"). The corresponding diagram is updated with an additional Arrow at the East end (representing Huck’s start) and an overlapping Arrow indicating the joint work section.
                - Pedagogical Rationale: The transformation of the equation group visually communicates a shift in the problem’s phase and introduces an unknown (x), prompting students to think about how extra work time is modeled.
            • In Sub-scene 3, a Circumscribe animation highlights the "x" in the equation to focus attention on the unknown. A separate Tex explanation ("x = extra hours Huck works") is written below the equation, and finally, a slow camera zoom-out (using self.camera.frame.animate.scale(0.9), run_time=2.0) reaffirms the spatial organization.
                - Pedagogical Rationale: Highlighting “x” encourages active thinking about the unknown variable and reinforces the step of translating a word problem into a mathematical model.

        - **Element Animations within VGroups and for Individual Mobjects:**
            • For each MathTex or Tex element:
                - Use Write animations (run_time=2.0) to sequentially reveal equations and text, ensuring a clear breakup of complex information.
                - Transition from one equation group to the next using FadeOut/FadeIn or Transform animations (each run_time=2.0) to maintain continuity.
                - The diagram elements (Line and Arrow objects) are rendered using Create and FadeIn (each run_time=2.0) and strategically shifted to maintain at least 0.3 units gap from the equation panel.
            • Synchronization of these animations is achieved via AnimationGroup and Succession:
                - For instance, the simultaneous entry of the left and right panels in Sub-scene 1 is handled by an AnimationGroup. A Wait(1) call immediately follows to ensure pedagogical processing before the next step.
                - In Sub-scene 2, after the transformation, another Wait(1) call allows viewers to grasp the changes before proceeding.
            • **Pedagogical Purpose:** Each element’s entrance, transformation, or highlight is timed to break down the problem step-by-step. This approach minimizes cognitive overload by focusing on one aspect of the problem at a time, making sure that equations and diagrams support the understanding of the underlying process.

    2. **Scene Flow - Pedagogical Pacing and Clarity:**
        - **Overall Animation Sequence, Spatial Progression for Learning:**
            • The scene is divided into three clearly demarcated sub-scenes:
                1. Introducing Tom’s initial progress using his work rate and time.
                2. Introducing the combined progress where Huck joins, thus extending the equation with an unknown “x.”
                3. Final highlighting of the unknown “x” and connecting it to the question asked in the problem.
            • The left panel consistently houses the equations/labels while the right panel holds the fence diagram. Their relative positioning (with a buffer of 0.3 units between panels and 0.5 units from edges) guides the viewer to correlate the numeric progress with the spatial progress along the fence.
        - **Transition Buffers for Pedagogical Pauses:**
            • Wait(1) is inserted after the completion of each sub-scene:
                - After the "Tom’s progress" entry to allow processing of the initial rate calculation.
                - Again after the "Combined progress" update to let viewers internalize the combined work rate and the appearance of the unknown.
            • These pauses provide intentional moments for reflection, reinforcing the learning objectives.
        - **Coordination of Animation Timing with Narration:**
            • The narration script cues the start of each animation sequence. For example, while the narrator explains Tom’s individual work, the corresponding equation and diagram are animated simultaneously.
            • Animation timings (run_time details and wait buffers) are intentionally set to coincide with narration points, ensuring that viewers see the visual representation exactly when the verbal explanation emphasizes it.
            • This close synchronization reinforces the pedagogical flow and ensures that the visual and verbal learning channels are integrated effectively.

    [NARRATION]
    - **Pedagogical Narration Script:**
        "In Scene 3, we’ll explore how to construct equations directly from the problem details. 
        [At 0:00] 'Let’s begin with Tom’s initial progress. Notice that Tom paints at a rate of 5 feet per hour. Over 2 hours, he covers 10 feet of the fence, as shown by this equation.' 
        [As the equation "5 ft/hr × 2 hr = 10 ft" is written on the left, and the corresponding portion of the fence is highlighted with an arrow from the West end on the right panel, use a gentle tone to guide attention.]
        [Pause for 1 second]
        'Now, as we progress into the next phase, Huck joins Tom from the opposite end. Here, we model their combined efforts: while Tom continues at 5 feet per hour, Huck adds 8 feet per hour. Over the two hours of their joint work, you can see how this is represented by adding the distances they cover together – essentially, 5+8 multiplied by 2.'
        [During this narration, the original equation transforms smoothly into “5·2 + (5+8)·2 + x” where the extra term “x” represents the additional hours Huck had to paint after Tom leaves. Simultaneously, the diagram on the right updates: an additional arrow appears at the East end marking Huck’s starting point, and an overlapping arrow emphasizes the combined painting section.]
        [Pause for 1 second]
        'The variable, x, now captures the extra hours Huck works beyond Tom’s time. Notice how highlighting this term with a circumscribe animation draws your attention – this visually reinforces the concept of an unknown that we solve for later.'
        [As the circumscribe animation occurs, display the Tex explanation “x = extra hours Huck works” just below the equations.]
        [Pause for 2 seconds]
        'By constructing and transforming these equations step-by-step, we translate a real-world task into a clear mathematical model. This methodical approach helps us understand how each phase of the problem contributes to finding the answer. Now, let's reflect on this process as we prepare to solve for x in the next part of our video.'
        [Conclude with a subtle zoom-out to encapsulate the entire scene, reinforcing the spatial clarity before moving on.]"

    - **Narration Sync - Pedagogical Alignment:**
        • The narration script is synchronized with the on-screen animations:
            - The initial explanation starts as soon as Tom’s equation and arrow appear, ensuring that what is being said is immediately supported by visual content.
            - At the moment the equation transforms (indicating Huck’s involvement), the narration explicitly mentions 'combined efforts' and 'extra hours', prompting viewers to associate the visual change with the conceptual shift.
            - The circumscribe animation on “x” aligns perfectly with the narration that emphasizes the unknown—this ensures that the eye is drawn to the critical part of the equation.
            - Wait timers (1 second between each major animation sequence and 2 seconds at the end) allow learners to pause, digest the information, and focus fully on the conceptual takeaway.
        • Overall, the synchronized pairing of animation cues with the detailed explanation creates an engaging and cohesive audiovisual teaching experience, guiding viewers step-by-step through the development of the equations and reinforcing the underlying mathematical concepts.

    </SCENE_ANIMATION_NARRATION_PLAN>


    # Scene 4 Implementation Plan

    <SCENE_VISION_STORYBOARD_PLAN>
    [SCENE_VISION]
    1.  **Scene Overview**:
        - This scene, titled "Solving Equations," walks the viewer step-by-step through the algebra needed to determine how many more hours Huck works than Tom. The scene explains—in a clear, sequential manner—how the partial work amounts (given in feet painted) are summed, simplified, and solved for the unknown extra hours that Huck works.
        - **Visual learning objectives for viewers:** 
            • Visualize each algebraic equation using Manim’s MathTex objects.
            • Use VGroup to sequentially arrange the equations with a minimum spacing of 0.3 units between each, all contained within safe area margins of 0.5 units.
            • Emphasize the transition from the original work-sum equation to the isolated variable step, and finally to the numerical answer.
            • Example: Use MathTex for expressions like r"10 + 26 + 8x = 100", and Tex for brief labels if needed.
        - How Manim visuals & animations support learning:
            • MathTex objects are grouped in a VGroup for clear, linear progression.
            • Animations such as Write and Transform highlight each algebraic transition.
            • Relative positioning methods (e.g., .next_to(), .align_to(), .shift()) ensure all objects respect the 0.5 unit safe area margins and maintain at least 0.3 units spacing from each other.
        - Key concepts to emphasize visually:
            • Equation construction (combining separate contributions from painting segments).
            • Isolation of the variable and algebraic manipulation.
            • Direct comparison of total working times for Tom and Huck, culminating in the difference of 6 hours.
            • All objects are positioned relative to ORIGIN or previously created objects, ensuring compliance with spatial constraints.

    [STORYBOARD]
    1.  **Visual Flow & Pacing (Manim Animation Sequence)**:
        - The scene opens with a centered MathTex title “Solving Equations” using Write animation at the top of the safe area. It then transitions to a series of algebraic steps laid out sequentially in a VGroup.
        - **Sub-scene Breakdown**:
            • Sub-scene 1: Displaying the Combined Work Equation
                - Visual Element: A MathTex object showing the equation for the painted fence:
                    • Equation: r"5\cdot2 \;+\;(5+8)\cdot2 \;+\;8x \;=\;100"
                - **Animation Sequence:**
                    - Use Write(animation, run_time=2) to display this MathTex at the ORIGIN, ensuring it is centered within the safe area.
                    - Position this equation relative to the title, shifting it downward with a .next_to() call while maintaining a spacing of at least 0.3 units.
                - Ensure the MathTex object remains at least 0.5 units from the left/right and top/bottom scene edges.
            • Sub-scene 2: Simplifying the Equation
                - Visual Element: Replace the initial equation with a simplified version using Transform:
                    • Simplified form: r"10 \;+\;26 \;+\;8x \;=\;100"
                - **Animation Sequence:**
                    - Apply a Transform animation (run_time=2) on the existing MathTex object to transition smoothly to the simplified equation.
                    - Maintain the same relative position and spacing.
            • Sub-scene 3: Isolating the Variable
                - Visual Element: A new MathTex equation showing the subtraction step:
                    • Equation: r"8x \;=\;100\;-\;(10+26)"
                - **Animation Sequence:**
                    - Use FadeIn (run_time=1.5) for this new MathTex, positioning it below the previous equation via .next_to() with 0.3 units spacing.
                    - Immediately, transform this to r"8x \;=\;64" using a Transform animation (run_time=1.5).
            • Sub-scene 4: Solving for x and Comparing Work Times
                - Visual Element: Introduce a MathTex object displaying the solution r"x \;=\;8".
                - **Animation Sequence:**
                    - Use Write (run_time=1.5) for writing the equation.
                    - Position this equation below the previous ones with the required 0.3 unit spacing.
                - Next, display two side-by-side MathTex objects (grouped in a VGroup):
                    • Left: r"\text{Tom's Hours} = 2+2 = 4"
                    • Right: r"\text{Huck's Hours} = 2+8 = 10"
                - **Animation Sequence:**
                    - Use FadeIn for each MathTex, and position them relative to the solution (using .next_to() and .align_to()) ensuring both stay within the safe margins and maintain 0.3 unit spacing.
                    - Finally, emphasize the conclusion with a MathTex object showing r"10 - 4 = 6" (Huck works 6 hours more than Tom) that appears below the previous pair.
                    - Use a Circumscribe or Highlight animation (run_time=1) on the result to draw attention.
        - Between each sub-scene, insert Wait() times (approximately 1 second) to allow users to absorb the information and to clearly separate each animation segment.
        - **Plugin Suggestion:** Consider using the manim-sliding-window plugin (if available) to smoothly shift the VGroup of equations upward as new equations are appended, ensuring smooth transitions within the safe areas.

    2.  **Ensuring Compliance with Spatial Constraints:**
        - All MathTex objects are positioned using relative methods (e.g., .next_to(), .to_corner(), .align_to()) ensuring they remain at least 0.5 units from scene edges.
        - A minimum spacing of 0.3 units is maintained between all MathTex objects and other elements as specified by measuring edge-to-edge distances.
        - The use of a VGroup for sequential equations helps automatically enforce uniform spacing and alignment while respecting the safe area margins.

    </SCENE_VISION_STORYBOARD_PLAN>

    <SCENE_TECHNICAL_IMPLEMENTATION_PLAN>
    0. **Dependencies**:
        - **Manim API Version**: Latest stable Manim Community Edition.
        - **Allowed Imports**: 
            • from manim import *
            • import numpy as np
            • (Optional) A plugin such as manim-sliding-window (if available) for advanced VGroup animations.
        - **Notes**: No external assets are used. All objects and animations follow Manim’s documented API.

    1. **Manim Object Selection & Configuration (Text and Shapes)**:
        - Objects Used:
            • MathTex: For mathematical equations; for example, MathTex(r"5\cdot2 \;+\;(5+8)\cdot2 \;+\;8x \;=\;100").
            • Tex: For non-mathematical title text such as "Solving Equations" (font size recommended 28).
        - Key Parameters:
            • Font sizes: Title in 28; equations in 24.
            • Colors and stroke defaults as provided by the Manim style.
        - Text Considerations:
            • Only use MathTex for equations (ensuring the LaTeX syntax is correct) and Tex for regular text.
            • All text objects must be sized and formatted so that multi-line equations do not exceed boundaries.
        - Safe Area & Spacing Enforcement:
            • Every object is initialized within safe area margins (minimum 0.5 units from screen edges).
            • When positioning multiple objects, a minimum buff of 0.3 units is maintained between bounding boxes to prevent overflow or overlap.

    2. **VGroup Structure & Hierarchy**:
        - Create a main VGroup, e.g., "formula_group", to hold all sequential equations.
        - Structure:
            • Title Group: Contains the “Solving Equations” title (positioned at the top within safe margins).
            • Equation VGroup: Contains all MathTex objects formed sequentially.
                    - Sub-group for initial equation.
                    - Subsequent groups or individual MathTex objects for each algebraic step.
            • Side-by-side Comparison Group: Contains Tom’s and Huck’s working-hour equations as sub-VGroup.
            • Final Result: A separate MathTex for the equation r"10 - 4 = 6" (with emphasis animation).
        - Each VGroup uses .arrange() or .next_to() with buff=0.3 units to maintain clear spacing.

    3. **Spatial Positioning Strategy**:
        - General Placement:
            • Title: Centered at the top of the safe area. Positioned relative to ORIGIN and shifted downward ensuring a top-margin of ≥0.5 units.
            • Initial Equation (Sub-scene 1): Positioned below the title using .next_to(title, DOWN, buff=0.3) ensuring left/right margins ≥0.5.
            • Subsequent equations (Sub-scenes 2, 3, 4): Each MathTex is positioned using .next_to(previous_equation, DOWN, buff=0.3).
            • Side-by-side equations (Tom/Huck work times): Positioned next to each other using .next_to() with a horizontal buff of 0.3 and aligned so both remain within left/right safe margins.
            • Final result equation ("10 - 4 = 6"): Placed below the side-by-side group with buff=0.3.
        - Detailed Relative Positioning:
            • All positioning is done relative to either ORIGIN or previously defined objects (e.g., title or previous equation).
            • Use .align_to() where necessary to ensure horizontal alignment.
            • All objects are explicitly checked for bounding box overflow. For multi-line equations, the width is controlled via font size and relative positioning.
        - Example Diagram (Text-Based Sketch):
            • Top Edge (≥0.5 units) : [Title]
            • Title → (0.3 units down) → [Equation 1]
            • [Equation 1] → (0.3 units down) → [Equation 2]
            • [Equation 2] → (0.3 units down) → [Equation 3]
            • [Equation 3] → (0.3 units down) → [Equation 4]
            • [Equation 4] → (0.3 units down) → [Side-by-side Comparison Group]
            • [Comparison Group] → (0.3 units down) → [Final Result Equation]
            • Bottom Edge (≥0.5 units)
            
    4. **Animation Methods & Object Lifecycle Management**:
        - Animation Sequence for Each Sub-Scene:
            • Sub-scene 1: 
                - Use Write(run_time=2) to animate the title "Solving Equations".
                - Then Write(run_time=2) for the initial MathTex: r"5\cdot2 \;+\;(5+8)\cdot2 \;+\;8x \;=\;100".
                - Follow with a Wait(1) to allow absorption.
            • Sub-scene 2:
                - Transform the initial equation to the simplified form: r"10 \;+\;26 \;+\;8x \;=\;100" using Transform(run_time=2).
                - Wait(1) after the transition.
            • Sub-scene 3:
                - FadeIn(run_time=1.5) a new MathTex below the simplified equation showing r"8x \;=\;100\;-\;(10+26)".
                - Immediately Transform it to r"8x \;=\;64" with Transform(run_time=1.5).
                - Wait(1) to observe the change.
            • Sub-scene 4:
                - Write(run_time=1.5) a new MathTex r"x \;=\;8", placed below the previous equations.
                - Then create a side-by-side VGroup with two MathTex objects:
                        • Left: r"\text{Tom's Hours} = 2+2 = 4"
                        • Right: r"\text{Huck's Hours} = 2+8 = 10"
                    Position using .next_to() and .align_to() ensuring 0.3 units spacing.
                - Wait(1)
                - Finally, Write or FadeIn a MathTex r"10 - 4 = 6" below these groups, then apply a Highlight or Circumscribe animation (run_time=1) to emphasize the conclusion.
                - Wait(1) to conclude the scene.
        - Lifecycle Management:
            • Use Wait() calls (≈1 second) between sub-scene animations for transition buffers.
            • All additions and removals (if needed later) are handled using FadeOut or Uncreate to maintain a clear scene.

    5. **Code Structure & Reusability**:
        - Modular Functions:
            • Define a function to create and return a MathTex object with safe margin checks.
            • Define a function to position objects relative to a reference and ensure minimum buff of 0.3 units.
            • Group animations into functions for each sub-scene to keep the main construct() method organized.
        - Code Organization:
            • Section 0: Dependencies and import statements.
            • Section 1: Object creation functions (for title, equations, side-by-side grouping).
            • Section 2: Scene construct method containing sequential VGroup creation and animations.
            • Inline comments will justify each positioning and animation decision referencing Manim’s documentation.
        - Reusability:
            • The functions and VGroup structures chosen here are easily adaptable for other scenes requiring sequential equation display and transformation animations.

    ***Mandatory Safety Checks***:
        - Safe Area Enforcement:
            • Each object is initially created relative to the ORIGIN or safe edges; before adding to scene, each object's bounding box is verified to lie within a 0.5 unit margin of all edges.
        - Minimum Spacing Validation:
            • Every use of .next_to() or .arrange() includes buff settings (≥0.3 units), ensuring that no two objects overlap.
        - Transition Buffers:
            • Explicit Wait() calls are inserted between sub-scene animations (minimum 1 second) to give the viewer time to process the information.
        - Plugin Check (if manim-sliding-window is used):
            • Include a comment: 
                    ### Plugin: manim-sliding-window - Used to smoothly transition the VGroup upward as new equations appear, ensuring that all animated elements stay within the safe area.
            
    </SCENE_TECHNICAL_IMPLEMENTATION_PLAN>

    <SCENE_ANIMATION_NARRATION_PLAN>

    [ANIMATION_STRATEGY]
    1. **Pedagogical Animation Plan:**
        - **Parent VGroup Transitions:**
            • Create a main VGroup (named "formula_group") that will hold all equation MathTex objects.
            • Initially, the title “Solving Equations” is written at the top of the safe area (ensuring 0.5 unit margins) using the Write animation (run_time=2). This immediately orients the viewer to the topic.
            • As new equations are added, use the manim-sliding-window plugin (or equivalently, a Shift animation with run_time=1) to slightly shift the entire VGroup upward. This maintains a clear spatial arrangement and steady flow, while ensuring that all elements remain within the safe area and are evenly spaced (minimum 0.3 units apart). Pedagogically, this draws attention to the evolving equation sequence and reinforces the idea of building upon previous steps.
        
        - **Element Animations within VGroups and for Individual Mobjects:**
            • Sub-scene 1: 
                - Display the initial work-sum equation using MathTex: "5\cdot2 \;+\;(5+8)\cdot2 \;+\;8x \;=\;100".  
                - Use Write(animation, run_time=2) to draw it on the screen. This visual introduction helps establish the complete equation representing the problem.
                - Position it using .next_to(title, DOWN, buff=0.3), ensuring safe-area and spacing constraints.
            • Sub-scene 2:
                - Use Transform (run_time=2) on the initial equation to simplify it to "10 \;+\;26 \;+\;8x \;=\;100".  
                - Pedagogical rationale: This illustrates the process of combining constants, breaking down the problem into manageable parts.
                - A Wait(1) follows to allow the learner to absorb the transition.
            • Sub-scene 3:
                - FadeIn (run_time=1.5) a new MathTex object below the simplified form, showing "8x \;=\;100\;-\;(10+26)".  
                - Immediately follow with a Transform (run_time=1.5) to reveal "8x \;=\;64".  
                - This step-by-step approach reinforces the isolation of the variable through subtraction.
            • Sub-scene 4:
                - Write (run_time=1.5) a new MathTex object presenting "x \;=\;8" positioned below the previous equations.  
                - Next, two side-by-side MathTex objects are introduced:
                        · Left: "\text{Tom's Hours} = 2+2 = 4"
                        · Right: "\text{Huck's Hours} = 2+8 = 10"
                - Use FadeIn for each (run_time=1.5) and position them using .next_to() and .align_to() ensuring at least 0.3 units spacing horizontally and safe margins on the sides.
                - Finally, write a concluding MathTex "10 - 4 = 6" beneath the pair using Write (run_time=1.5) and apply a Circumscribe or Highlight (run_time=1) to emphasize the result.  
                - Pedagogically, these steps highlight the parallel calculations of working hours and stress the final key comparison.
        
        - **Coordination Between Element Animations and VGroup Transitions:**
            • After each sub-scene, a Wait(1) is inserted to let learners process the presented algebraic manipulation.
            • All transitions (Write, Transform, FadeIn, Circumscribe) are coordinated so that once a learner hears the narration guiding through the algebraic steps, the corresponding visual update happens in synchrony. This careful synchronization ensures that attention is drawn to both the incremental buildup of the equation and its eventual solution.

    2. **Scene Flow - Pedagogical Pacing and Clarity:**
        - **Overall Animation Sequence and Spatial Progression for Learning:**
            • The scene begins with the clear, centered title "Solving Equations" at the top (≥0.5 units from the top edge).
            • Sub-scene 1 introduces the full work equation centered below the title.
            • Sub-scene 2 uses a Transform animation to simplify the equation, visually connecting numerical simplification from "5·2+(5+8)·2+8x=100" to "10+26+8x=100".
            • Sub-scene 3 demonstrates isolating the variable "x" by adding a new equation below the previous one; this deliberate vertical stacking helps reinforce the sequential nature of the solution.
            • Sub-scene 4 finalizes the solution with "x=8", then shifts focus to comparing working hours for Tom and Huck side-by-side, and concludes with the key result "10 - 4 = 6".
            • Throughout, all MathTex objects are arranged using a VGroup with a buff of 0.3 units between each, ensuring clarity, structure, and no crowding of the safe area (0.5 unit margins).
        - **Transition Buffers for Pedagogical Pauses:**
            • After displaying each algebraic transformation, a Wait(1) call is utilized. This deliberate pause serves to give viewers time to mentally process the mathematical operations before proceeding.
            • These pauses are essential to reinforce each teaching point, allowing time for reflection and ensuring comprehension before the next sub-step is animated.
        - **Coordination Between Animation Timing and Narration:**
            • The narration begins with an explanation of the problem setup, then progressively guides the viewer through each algebraic step as the corresponding animation plays.
            • Narration cues (e.g., “Observe how we simplify the constants…”) are synchronized to start just as the Transform or FadeIn animations begin. This coincidence reinforces both visual and auditory memory, maximizing comprehension.
            • The final explanation that “Huck works 6 more hours than Tom” is emphasized not just by the text, but by the Highlight animation on “10 - 4 = 6”, clearly linking the narrated summary with the visual conclusion.

    [NARRATION]
    - **Pedagogical Narration Script:**
        • Opening (at start, as the title appears):
            "Welcome to Scene 4: Solving Equations. In this segment, we will break down the steps to solve our equation that represents the work done by Tom and Huck. Notice how every component of the problem is represented as a term in our equation."
        • As the initial equation "5·2 + (5+8)·2 + 8x = 100" is written:
            "Let’s look at our complete equation. Tom paints for 2 hours at 5 feet per hour, then both boys work together for another 2 hours adding their combined rates, and finally, Huck continues painting by himself for x hours at 8 feet per hour. All these contributions perfectly add up to painting the entire 100-foot fence."
        • Transition to Sub-scene 2 (during the Transform to "10 + 26 + 8x = 100"):
            "Now, by simplifying the numbers—2 hours at 5 feet per hour becomes 10 feet, and the two working together for 2 hours gives us 26 feet—we rewrite the equation as 10 plus 26 plus 8x equals 100. This simplification sets the stage for isolating the unknown."
        • When the new equation "8x = 100 - (10+26)" is faded in:
            "Next, to isolate the variable x, we subtract the total fixed work from 100. Here, subtracting 36 from 100 leaves us with 64 feet that need to be painted by Huck alone."
        • As the equation transforms to "8x = 64":
            "This transformation clearly shows that the remaining 64 feet are painted at a rate of 8 feet per hour."
        • When "x = 8" appears:
            "Dividing both sides by 8, we find that x equals 8. In other words, Huck paints alone for 8 hours after Tom leaves."
        • During the side-by-side display of Tom's and Huck's working hours:
            "Now, let’s compare the total working hours. Tom paints for 2 hours before Huck joins and an additional 2 hours alongside him, which totals 4 hours. Huck, on the other hand, works the initial 2 hours together and then continues for another 8 hours on his own, meaning he works 10 hours in total."
        • When "10 - 4 = 6" is emphasized:
            "Subtracting Tom's hours from Huck's gives us the final answer: Huck works 6 hours more than Tom. Notice how each step built on the previous one, leading us confidently to the conclusion."
        • Concluding the scene:
            "In summary, by carefully isolating our variable and breaking down the equation, we have both simplified the problem and clarified the difference in work times between Tom and Huck. Let's carry this process forward as we move into the next part of our analysis."
        
    - **Narration Sync - Pedagogical Alignment:**
        • The narration begins exactly as the title appears and is paced so that each mathematical transformation is described as its corresponding animation plays.
        • For example, the “Write” of the initial equation is accompanied immediately by a statement that introduces the terms. A one-second Wait follows so the learner can absorb the concept, during which the audio briefly pauses before transitioning.
        • As the Transform animation simplifies the equation, the narration highlights the arithmetic simplification, then similarly pauses before proceeding.
        • The final comparison using side-by-side equations is narrated in sync with the FadeIn of the two equations, ensuring that when we display “10 - 4 = 6,” the spoken explanation reinforces the highlighted conclusion.
        • By coordinating narration cues with the timing of each animation (using run_time values and explicit Wait() calls), the viewer’s attention is continually guided to the key learning points, creating an integrated audiovisual learning experience that maximizes understanding and retention.

    </SCENE_ANIMATION_NARRATION_PLAN>




    # Scene 5 Implementation Plan

    <SCENE_VISION_STORYBOARD_PLAN>
    [SCENE_VISION]
    1. **Scene Overview**:
        - This scene, titled "Final Answer", recapitulates the problem’s key steps and clearly displays the final result: that Huck worked 6 more hours than Tom. It plays a summarizing role in the overall narrative, reinforcing the effectiveness of using equations to model real-life problems.
        - Visual learning objectives for viewers:
            • Use Manim’s MathTex objects to display mathematical expressions (e.g., "5 ft/hr", "8 ft/hr", "10 hrs", "4 hrs") and final numerical comparisons.
            • Use Tex objects for short labels and explanation text (e.g., "Tom", "Huck", "Final Answer").
            • Integrate simple Shapes (like a Rectangle for a summary box) and a VGroup to gather timeline or diagram elements.
            • **Plugin Suggestion:** Consider using the `manim-slides` plugin if smooth transitions between grouped visuals are desired.
        - How Manim visuals & animations support learning:
            • The final answer will be shown in a central summary box (using a Rectangle with a Tex label) arranged within 0.5 unit safe margins.
            • Supporting visuals such as a simplified timeline or a paint diagram on a linear fence (using Lines and VGroups) will be positioned around the summary box with a minimum spacing of 0.3 units.
            • Use relative positioning (e.g., .move_to(ORIGIN), .next_to(), .shift()) to ensure all objects comfortably reside within the safe area.
        - Key concepts to emphasize visually include:
            • The application of linear equations to real-life problems.
            • Clear spatial layout: the timeline diagram and summary box remain separate with at least 0.3 units spacing.
            • Use MathTex for equations and numerical expressions, and Tex for labels like "Final Answer" for clarity.

    [STORYBOARD]
    1. **Visual Flow & Pacing (Manim Animation Sequence)**:
        - Begin with a brief recap of the problem using a VGroup containing compact Tex labels ("Tom paints", "Huck joins") and key numbers. These texts are arranged near the top of the scene, away from the safe margins (at least 0.5 units from the edge) and with a minimum 0.3 unit spacing between them.
        - Next, create a simplified timeline/diagram:
            • Visual Element: A horizontal Line representing the 100 ft fence (drawn with Line). Place this Line centered horizontally using .move_to(ORIGIN) but shifted slightly downward to allow text above.
            • Add markers (using small Dot objects or short Lines) at the West and East ends, labeled "W" and "E" with Tex objects.
            • Animate the progression: Use Create animations (run_time=2 seconds) to draw the line and markers. Position labels relative to the line endpoints using .next_to() with a spacing of 0.3 units.
        - Introduce a central summary box:
            • Visual Element: A Rectangle with a Tex label inside it that reads, "Final Answer: Huck worked 6 more hours than Tom."
            • The Rectangle is created using Manim’s Rectangle class. Its size is chosen such that it lies entirely within the safe area (0.5 unit margin all around). Use .move_to(ORIGIN) to center the summary box.
            • Inside, use a VGroup to group the Tex label and a MathTex expression (if desired, e.g., "10 - 4 = 6") ensuring a minimum internal spacing of 0.3 units.
            • Animate the appearance with a FadeIn (run_time=1.5 seconds).
        - Ensure supporting visuals (timeline and diagram elements) are repositioned relative to the central box:
            • Position the timeline diagram above or below the summary box with .next_to(summary_box, UP) or .next_to(summary_box, DOWN) ensuring a spacing of at least 0.3 units.
            • Alternatively, a summary bullet list of steps can be placed to one side (e.g., to the left, using .next_to(summary_box, LEFT, buff=0.3)) to explain briefly the step-by-step calculation.
        - Visual Transitions:
            • After each key visual appears, insert a Wait() (about 1 second) to let viewers absorb the information.
            • Use Transform animations if necessary to change intermediate expressions into the final summary (e.g., transforming a multi-step equation into the final numeric answer).
        - Final Step:
            • Conclude with a slow ZoomOut (run_time=2 seconds) showing all elements together, reinforcing spatial hierarchy and summarizing the session.
            • All elements must remain within the safe margins (0.5 units) throughout the animation, and maintain a minimum spacing of 0.3 units between any two objects.

    2. **Sub-scene Breakdown**:
        a. Sub-scene 1 – Recap of Problem Essentials:
            - Visual Element: A VGroup containing short Tex labels (e.g., "Tom: 5 ft/hr, 4 hrs", "Huck: 8 ft/hr, 10 hrs") arranged at the top-center.
            - Animation Sequence: Use Write animations (each with run_time=1 second) to sequentially display these labels ensuring a minimum spacing of 0.3 units from each other and 0.5 units from the top edge.
            - Positioning: Align the VGroup .next_to(ORIGIN, UP, buff=0.5).
        b. Sub-scene 2 – Timeline Diagram of the Fence:
            - Visual Element: A horizontal Line representing the fence (with markers at West and East ends) using the Line and Dot classes.
            - Animation Sequence: Use Create to draw the fence line and markers. Position the endpoints’ labels ("W" and "E") using .next_to() with a buff of 0.3 units.
            - Positioning: Place the diagram below the text recap, ensuring 0.3 units spacing between the VGroup and this diagram.
        c. Sub-scene 3 – Final Summary Box:
            - Visual Element: A Rectangle (for the summary box) with a centered VGroup that includes a Tex label ("Final Answer:") above a MathTex expression (e.g., "6") or a combined expression like "10 - 4 = 6" if desired.
            - Animation Sequence: Use FadeIn on the rectangle and Write on the text and MathTex, each with a run_time of 1.5 seconds. Then, use a Circumscribe animation around the final answer for emphasis.
            - Positioning: Center the summary box at ORIGIN, and ensure that all surrounding supporting visuals are at least 0.3 units away from it. The summary box must also stay within the safe area (0.5 unit margin from scene edges).

    </SCENE_VISION_STORYBOARD_PLAN>

    <SCENE_TECHNICAL_IMPLEMENTATION_PLAN>
    0. **Dependencies**:
        - **Manim API Version**: Latest stable release of Manim Community Edition.
        - **Allowed Imports**: 
            • From the core: "from manim import *", "import numpy as np"
            • No external assets are used.
        - **Plugin Usage**: 
            • None required for this scene.
            
    1. **Manim Object Selection & Configuration (Text and Shapes)**:
        - Text Objects:
            • Use MathTex for mathematical expressions (e.g., MathTex("10-4=6") or MathTex("6")).
            • Use Tex for non-mathematical labels and explanations (e.g., Tex("Final Answer:"), Tex("Tom: 5 ft/hr, 4 hrs"), Tex("Huck: 8 ft/hr, 10 hrs"), Tex("W"), Tex("E")).
            • Font sizes:
                - Title or central label (e.g., "Final Answer:") recommended at 28.
                - Side labels or formulas at 24, ensuring multi-line text is adjusted to avoid overflow.
        - Shape Objects:
            • Rectangle: For the summary box centered at ORIGIN. Its dimensions must be chosen so that no part of the rectangle (including its contained text) extends beyond 0.5 units from any scene edge.
            • Line: For the representation of the 100 ft fence. Must be centered horizontally by using .move_to(ORIGIN) then shifted downward to leave room for text above.
            • Dot or short Line: As markers at each end of the fence.
        - Key Parameters:
            • All text and shapes are configured with a clear stroke or fill color to enhance contrast.
            • Ensure that the bounding boxes of all text objects are computed such that there is no risk of overflowing the safe area (0.5 units margin). Additional padding is configured with relative positioning buffers.
        
    2. **VGroup Structure & Hierarchy**:
        - Create a VGroup for the Recap Text:
            • Contains Tex objects "Tom: 5 ft/hr, 4 hrs" and "Huck: 8 ft/hr, 10 hrs".
            • Arrange using .arrange(direction=RIGHT, buff=0.3), then position relative to the top safe margin (using .next_to(ORIGIN, UP, buff=0.5)).
        - Create a VGroup for the Timeline Diagram:
            • Contains the horizontal Line representing the fence, and markers (Dot objects or short Lines) for the West ("W") and East ("E") endpoints.
            • Position the markers using .next_to() with a buff of 0.3 relative to the ends of the Line.
        - Create a VGroup for the Summary Box Content:
            • Contains a Tex label ("Final Answer:") and a MathTex expression (either "6" or "10-4=6") arranged vertically with at least 0.3 units internal spacing.
            • This VGroup is then centered inside the Rectangle.
            
    3. **Spatial Positioning Strategy**:
        - All positioning is done using relative methods:
            • Recap Text VGroup: Positioned using .next_to(ORIGIN, UP, buff=0.5) to maintain the top safe margin.
            • Timeline Diagram:
                - Center the fence Line at ORIGIN but shift it downward (e.g., .shift(DOWN * 1)) ensuring it stays within the lower safe margin.
                - Position end markers ("W" and "E") relative to the fence endpoints using .next_to(..., buff=0.3).
                - Ensure there is at least 0.3 units spacing between the recap VGroup and the timeline.
            • Summary Box:
                - Centered at ORIGIN using .move_to(ORIGIN) and sized to fully reside within the 0.5 unit safe margin.
                - Ensure that supporting visuals (timeline diagram or recap text) remain at least 0.3 units away from the summary box. For example, if the timeline is below the box, use .next_to(summary_box, DOWN, buff=0.3).
        - Special Measures to Prevent Text Overflow:
            • When setting up Tex or MathTex objects, account for their bounding box sizes by testing with .get_width() and .get_height(), and if necessary adjust the appropriate scale so no object crosses the safe margin.
            • Multi-line text is explicitly arranged within VGroups to guarantee the required spacing.
        
    4. **Animation Methods & Object Lifecycle Management**:
        - Animation Sequence:
            a. Sub-scene 1 – Recap of Problem Essentials:
                • Animate VGroup of recap texts using Write animation (each with run_time=1 second).
                • Insert a Wait(1) after the texts fully appear.
            b. Sub-scene 2 – Timeline Diagram:
                • Animate the fence Line and markers with Create (run_time=2 seconds).
                • Animate the addition of labels "W" and "E" using Write with run_time=1 second. Ensure labels use .next_to() with buff=0.3.
                • Insert a Wait(1) to allow absorption of the timeline.
            c. Sub-scene 3 – Final Summary Box:
                • Create a Rectangle (using Rectangle) for the summary box and position a nested VGroup (Tex and MathTex) at its center.
                • Animate the Rectangle with FadeIn (run_time=1.5 seconds) and the text with Write (run_time=1.5 seconds).
                • Optionally, use a Circumscribe animation on the final answer element for emphasis.
            d. Final Transition:
                • After all key elements are on screen, use a slow ZoomOut (run_time=2 seconds) to show the complete layout.
        - Transition buffers (Wait() calls) of at least 1 second are used between sub-scenes to maintain clarity.
        
    5. **Code Structure & Reusability**:
        - Organize the code into logical sections:
            • Dependency imports and documentation.
            • Object definitions (for Tex, MathTex, Shapes, and VGroups).
            • Sequential layout: First construct sub-scene VGroups (recap, timeline, summary box) then position them relative to each other.
            • The main construct() method should call sub-methods such as create_recap_text(), create_timeline_diagram(), and create_summary_box() to promote reusability.
        - Inline Comments:
            • Each section includes inline comments referencing Manim documentation (e.g., use of .next_to(), .shift(), .arrange) and notes on how safe area margins and minimum spacing buffers (0.5 and 0.3 units respectively) have been enforced.
            • Comments warn about potential overlapping text issues and document the checks performed using methods like .get_width() if required.
        
    ***Mandatory Safety Checks***:
        - Safe Area Enforcement: 
            • All objects are initially positioned relative to ORIGIN or safe margins (using .next_to(ORIGIN, UP/DOWN/LEFT/RIGHT, buff=0.5)) ensuring they remain within the 0.5 unit margin.
        - Minimum Spacing Validation:
            • Use relative positioning with a buff of at least 0.3 units between any two objects (e.g., recap VGroup and timeline, timeline and summary box).
        - Transition Buffers:
            • Insert explicit Wait() calls (≥1 second) between animation stages.
            
    </SCENE_TECHNICAL_IMPLEMENTATION_PLAN>

    <SCENE_ANIMATION_NARRATION_PLAN>

    [ANIMATION_STRATEGY]
    1. **Pedagogical Animation Plan:**
        - **Parent VGroup transitions:**
            • Create a Recap VGroup containing two Tex objects: "Tom: 5 ft/hr, 4 hrs" and "Huck: 8 ft/hr, 10 hrs". Arrange these using .arrange(direction=RIGHT, buff=0.3) and position them .next_to(ORIGIN, UP, buff=0.5). 
                - Animation: Use Write() for each Tex with run_time=1 second. 
                - Pedagogical rationale: This gradual display draws focus to the essential information and reinforces the connection to the information covered in earlier scenes.
            • Group the timeline diagram elements (fence line, endpoint markers "W" and "E") into a VGroup. Position this group immediately below the recap text with a spacing of 0.3 units.
                - Animation: Use Create() for the fence line with run_time=2 seconds, then Write() for the endpoint labels with run_time=1 second each.
                - Pedagogical rationale: The step-by-step appearance of the timeline helps learners visualize the spatial arrangement of the problem, reinforcing the application of linear equations.
            • Prepare a Summary Box VGroup that contains a Rectangle (the summary box) and a nested VGroup with a Tex label ("Final Answer:") and a MathTex expression (e.g., "10-4=6" or simply "6"). Center this box at ORIGIN ensuring all safe margins (0.5 units) are respected.
                - Animation: Use FadeIn() for the Rectangle with run_time=1.5 seconds and Write() for the nested text with run_time=1.5 seconds. Add a Circumscribe() animation on the final answer element for emphasis.
                - Pedagogical rationale: The summary box isolates the final concept and clearly signals that the problem has been solved, guiding the learner’s focus to the result.

        - **Element animations within VGroups and for individual Mobjects:**
            • For each textual element inside the Recap VGroup and Timeline Diagram, use Write() animations to sequentially introduce the key information. This fragmentation aids in preventing information overload and facilitates step-by-step understanding.
            • For the Summary Box:
                - FadeIn() is used to gently draw attention to the conclusion without abrupt changes.
                - The nested VGroup’s elements (Tex and MathTex) are timed to appear concurrently with the FadeIn to emphasize the final computation.
            • **Synchronization Details:**
                - The Recap VGroup appears first (total run_time ≈ 2 seconds), followed by a Wait(1 second) for comprehension.
                - Immediately afterwards, the Timeline Diagram is drawn (approximately 3 seconds total for line and markers) with another Wait(1 second).
                - Then, the Summary Box is animated into view (approximately 1.5–1.5 seconds for FadeIn and Write) with an additional highlight via Circumscribe (run_time=1 second).
                - Finally, a slow ZoomOut (run_time=2 seconds) reveals all elements together, reinforcing the spatial hierarchy and summarizing the session.
            • All elements are positioned using relative methods (.move_to(), .next_to(), .arrange()) to guarantee the objects remain within the safe margins (0.5 units) and with at least 0.3 units spacing.

    2. **Scene Flow - Pedagogical Pacing and Clarity:**
        - **Overall animation sequence, spatial progression for learning:**
            • Sub-scene 1 – Recap of Problem Essentials:
                - Recap VGroup appears at the top center to remind the viewer of the rates and hours worked by Tom and Huck. The clear separation of this information (using minimum 0.3 units spacing among texts and 0.5 units from the scene edge) prepares the learner for the spatial diagram.
            • Sub-scene 2 – Timeline Diagram of the Fence:
                - The horizontal Line representing the fence is centered (shifted slightly downward) with markers on both ends labeled "W" and "E". This diagram reinforces the physical setting and correlates with the abstract numerical data.
            • Sub-scene 3 – Final Summary Box:
                - The summary box featuring the final answer ("Final Answer: 10-4=6") is centered. This visual consolidation makes it easy to derive and remember the result.
            • Final Transition:
                - A slow ZoomOut brings together all elements to consolidate the learning and showcase the complete solution layout.
        - **Transition buffers for pedagogical pauses:**
            • A Wait(1 second) is inserted after the Recap VGroup and after the Timeline Diagram animations, providing necessary pauses for the viewer to absorb the information.
            • These pauses are crucial to avoid cognitive overload and reinforce stepwise understanding.
        - **Coordinate animation timing with narration for engagement and comprehension:**
            • The narration script will include timing cues that match the start and end of these animations, ensuring that as each new visual element appears, the narration highlights its significance and connection to the key learning objectives.
            • For example, the narrator will mention key phrases like “now notice how the fence is drawn…” exactly as the Timeline Diagram appears.

    [NARRATION]
    - **Pedagogical Narration Script:**

        "Now, building on our previous work, let’s bring everything together for the final answer. [Cue: As the Recap VGroup begins to appear, run_time: 2 sec]
        
        Here we see a quick review: Tom painted at 5 feet per hour for 4 hours, while Huck painted at 8 feet per hour over a total of 10 hours. This recap helps us remember the essential rates and times involved.
        
        [Wait 1 second]
        
        Next, observe the visual representation of the fence — a 100-foot line stretched between West and East, with markers ‘W’ and ‘E’ marking the endpoints. Notice how the line is drawn slowly, mirroring the steady progress of our calculation. [Cue: The Timeline Diagram appears with the horizontal line and markers over 3 sec]
        
        This diagram isn’t just a picture; it symbolizes the problem setup, illustrating the physical distance that was methodically divided by the work of each painter.
        
        [Wait 1 second]
        
        Now, the moment of clarity: our Final Answer. In this summary box, centered just before you, we state the conclusion — Huck worked 6 more hours than Tom. [Cue: The summary box fades in with the Tex and MathTex animations (run_time: 1.5 sec each) and is highlighted by a Circumscribe animation]
        
        By isolating this final result in a neatly framed box, we underline the core concept: using equations to solve real-life problems leads us to clear, verifiable answers. Notice the step-by-step breakdown — from the rates, through the timeline, to the computed difference — which reinforces your understanding of how to solve linear equations.
        
        [Wait 1 second]
        
        Finally, let’s zoom out to view the entire solution layout. This zoom out is not just a visual treat but a summary of our process: starting with individual contributions, visualizing progress, and concluding with the elegant solution. [Cue: Perform a slow ZoomOut for about 2 seconds]
        
        As we conclude Scene 5, remember that every step we took, every pause and animation, was designed to make the learning process both intuitive and memorable. Let’s carry this understanding forward as we move to our next segment."
        
    - **Narration Sync - Pedagogical Alignment:**
        • The narrator’s cues are directly linked with the start and completion of each animation segment. When the recap texts appear, the narration reiterates the key numbers; as the timeline diagram is drawn, the narration explains its relevance; and when the summary box animates in, the narrator emphasizes the final lesson.
        • By synchronizing Wait() pauses with narration segments, learners are given time to reflect on the details. This coordination ensures that the auditory explanation and visual elements reinforce each other, maximizing both engagement and retention.

    </SCENE_ANIMATION_NARRATION_PLAN>
"""
}

# 如果需要请求头（如 Content-Type、Authorization），请设置
headers = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer YOUR_TOKEN"  # 如有需要
}

# 发起 POST 请求
response = requests.post(url, json=payload, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 保存为图片文件（例如 output.png）
    with open("output.html", "wb") as f:
        f.write(response.content)
    print("网页已成功保存为 output.html")
else:
    print(f"请求失败，状态码: {response.status_code}")
    print("返回内容:", response.text)