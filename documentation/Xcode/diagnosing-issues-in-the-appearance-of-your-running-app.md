# Diagnosing issues in the appearance of a running app

**Framework**: Xcode

Inspect your running app to investigate issues in the appearance and placement of the content it displays.

#### Overview

At times your app’s content may appear to be missing, out of place, or have an appearance that is incorrect. To identify and diagnose the cause of these issues, attach the debugger, reproduce the error, and then narrow down its root cause by inspecting changes in your interface, the code that is executing, and the state of variables. If you configure a scheme’s run action for debugging by using the Debug executable checkbox in Info settings, the app will attach to the debugger automatically when the app uses the scheme. To attach the debugger to a process that is already running, choose Debug → Attach to Process, and select your app’s process from the list.

Temporarily override system settings to control your app’s appearance and reveal problems that only occur when these settings are in effect, understand layout issues by visualize your views in stacked layers, and debug content in immersive space by adding visual overlays.

##### Adjust System Configurations to Identify Their Impact on Your Views

Some visual issues only arise when you configure the system using specific environmental settings. Xcode provides environmental overrides when targeting iOS, iPadOS, macOS, and tvOS apps to help you debug these issue. Use these environmental overrides to change the interface style, dynamic text size, and to induce the effects of other accessibility options, so you can understand the effect of these changes on the layout and visual appearance of your views.

To enable one or more of these overrides, click the Environment Overrides button on Xcode’s debugging toolbar, toggle the switch next to the override category, and configure the controls under the category heading.

![Xcode debugger toolbar displaying the Environmental Overrides popup menu with toggle switches to the right of each override type. Appearance is at the top with options below it for dark appearance and light appearance, Dyanmic Type is bleow that with a slider bar currently set at XXX Large, and Accessibility is at the bottom with options that include things such as Increase Contrast, Reduce Motion, and Smart Invert.](https://docs-assets.developer.apple.com/published/fc8815bbdf67290ee67e8a470c914dee/diagnosing-issues-with-your-visual-content-1%402x.png)

##### Resolve Issues in the Layout of Your Uikit and Swiftui Views

Use the View debugger, available when targeting iOS, iPadOS, macOS, tvOS, and watchOS apps, to diagnose the reasons an item in your user interface is in the wrong position or is the wrong size. Set a breakpoint in your app after it presents the view, for example, in a `viewDidAppear:` method, then click the Debug View Hierarchy button in the debug bar when the debugger pauses on your breakpoint. Alternatively, just click the Debug View Hierarchy button after your app presents the view.

The debugger displays a 3D rendering of the current view on the canvas in the center, with a representation of the view hierarchy in the Debug navigator. Drag the view in any direction to see a 3D representation of the current view stack, and use the controls at the bottom of the canvas to adjust the views and the spacing between them.

![Xcode displaying the view debugger, rotated to see a three dimensional representation of the view stack. The view debugger shows a selected UILabel that extends to the leading and trailing edges of the view and is truncating text, with the four constraints for the view highlighted.](https://docs-assets.developer.apple.com/published/ecbf24fb595b4cbde72f4c251adbe821/diagnosing-issues-with-your-visual-content-2%402x.png)

Click to select a view in either the visual rendering or the view hierarchy in the Debug navigator, then inspect details in the Object inspector or Size inspector. Resolve your layout issue according to the type of layout:

##### Understand the Relationships Between Objects in a Immersive Space

For visionOS apps with content in an immersive space, it’s often helpful to see a visual representation of coordinate axes, bounding boxes, and other information that is normally invisible. Xcode’s debugging tools include options to display this information in Simulator or on a device. Use them to ensure that your entities are located where you expect, and interacting with each other and the surroundings the way you anticipate. For example, if an entity isn’t responding to events, enable Collision Shapes to confirm the presence of one, required for event handling, and indicate its boundary.

![A macOS display with an Xcode window on the left and Simulator window on the right. Xcode's debugger toolbar displays the Visualizations popup menu which includes options for enabling visualizations for Anchoring, Axes, Bounds, Collisions Shapes and Axes, Occlusion Mesh, and Surfaces, with Collisions Shapes and Axes and Surfaces selected. Simulator displays an immersive experience that includes an interactive 3D globe on the left and 2D window on the right. Outlines appear around each entity to indicate their collision shape, colored arrows indicate axes, and border lines and diagonals mark surfaces.](https://docs-assets.developer.apple.com/published/2a039c7552540f4ccabf20a318d85561/diagnosing-issues-in-the-appearance-of-a-running-app-1%402x.png)

To annotate your content with an overlay, click the Debug Visualizations button on Xcode’s debugging toolbar and select one or more of the options:

> **Note**: The Anchoring, Axes, and Bounds options apply to the entities for the app you are debugging while the Collision Shapes & Axes option applies to all entities in Shared Space. The Occlusion Mesh and Surfaces options apply to objects the system detects in your surroundings.

## See Also

- [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)
  Identify runtime crashes and undefined behaviors in your app during testing using Xcode’s sanitizer tools.
- [Analyzing HTTP traffic with Instruments](../Foundation/analyzing-http-traffic-with-instruments.md)
  Measure HTTP-based network performance and usage of your apps.
- [Detecting when your app contacts domains that may be profiling users](detecting-when-your-app-contacts-domains-that-may-be-profiling-users.md)
  Use Instruments to assess whether your app or its third-party SDKs connect to domains that may profile users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/diagnosing-issues-in-the-appearance-of-your-running-app)*