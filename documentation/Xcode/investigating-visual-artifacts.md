# Investigating visual artifacts

**Framework**: Xcode

Discover, diagnose, and fix visual artifacts in your app with the Metal debugger.

#### Overview

If you notice any visual artifacts while running your app, you can use the Metal debugger to find and investigate problematic pixels. First, configure your build to include shader source code (see [`Building your project with embedded shader sources`](building-your-project-with-embedded-shader-sources.md)). Then, take a frame capture of your app when you notice the visual artifact that you want to debug (see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md)).

After you have a frame capture, use the Debug navigator to find the draw command that contains the visual artifact, and use the Attachments viewer to find the pixel with the issue. Debug the pixel to launch the shader debugger, then step through your shader source code and inspect variable values until you discover the problem. Then, edit the shader source and reload the shader to verify your fix.

##### Skim Through Render Attachments in the Debug Navigator

In the Metal debugger, navigate to a draw command that has the issue. As you move your pointer over rows in the Debug navigator on the left, the Metal debugger shows a preview of the first attachment. You can use this to quickly find any draw commands that warrant further inspection.

![A screenshot of Xcode’s Debug navigator showing the popover that appears when the pointer hovers over any command in the list.](https://docs-assets.developer.apple.com/published/f67eaf84f86c4a56d11934e66b88301a/gputools-metal-debugger-sdp-navigator-hover%402x.png)

You also can filter the navigator to show only markers and commands so it’s easier to compare draw commands.

![A screenshot of Xcode’s Debug navigator highlighting the button to show only markers and commands.](https://docs-assets.developer.apple.com/published/17e510aedfabd9d52d9de607f21bf95e/gputools-metal-debugger-sdp-navigator-filter%402x.png)

When you find the problematic draw command, click it to select it. The Metal debugger automatically shows your attachments in the assistant editor on the right.

![A screenshot of the Metal debugger showing the Bound Resources viewer and the Attachments viewer side by side for a draw command.](https://docs-assets.developer.apple.com/published/a641476d9c43fa2dbe12b43fe8da0a96/gputools-metal-debugger-sdp-select%402x.png)

##### Inspect Attachments for a Draw Command

Use the Attachments viewer to find any problematic pixels. You can scroll to zoom in, and drag to pan. For more information on the Attachments viewer, see [`Inspecting the attachments of a draw command`](inspecting-the-attachments-of-a-draw-command.md).

![A screenshot of the Metal debugger showing the Attachments viewer with the value inspector when the pointer is hovering over pixel 721, 815. The Debug button is highlighted.](https://docs-assets.developer.apple.com/published/a6550c1fa4b7508ab1e3178123985143/gputools-metal-debugger-sdp-zoom-pixel%402x.png)

Click the problematic pixel to select it, and then click the Debug button.

If the problematic pixel isn’t inside a debuggable region, it has a nongreen selection indicator (as with the blue indicator in the screenshot below). This means that the draw command didn’t write to that pixel and, therefore, you can’t debug it. Because the Attachments viewer remembers your zoom and position, you can quickly step through different draw commands in the Debug navigator to find the right one.

![A screenshot of the Metal debugger’s Attachments viewer where the selected pixel falls outside the debuggable region for a draw command.](https://docs-assets.developer.apple.com/published/030fcd2e4f75f5166819eef6092403c9/gputools-metal-debugger-sdp-no-debug%402x.png)

##### Debug Your Fragment Shader

The shader debugger displays the shader source in the Shader editor (see [`Inspecting shaders`](inspecting-shaders.md)). The call tree on the left shows each executed line in your shader. The values of the variables appear to the right of each shader line in the shader source code. For example, in the screenshot below, you can see that the `in` variable has a value containing `721.5`, `815.5`, and so forth.

![A screenshot of the Metal debugger showing the Shader editor and the Attachments viewer side by side. The Debug navigator displays the region of interest and the call tree.](https://docs-assets.developer.apple.com/published/39a534a281d2c1a6fba72fbb3703942b/gputools-metal-debugger-sdp-debug%402x.png)

Step through your shader source code and inspect variable values until you discover the problem. Make changes to the shader source code, and then click the Reload Shaders button in the debug bar to refresh the variable values, along with the attachments.

![A screenshot of the Reload Shaders button in the debug bar.](https://docs-assets.developer.apple.com/published/3772f6e2fc52fa9d8f2252a384c418df/gputools-metal-debugger-se-reload%402x.png)

If you still see visual artifacts, continue editing the shader and reloading it as needed until you solve the problem.

> ❗ **Important**: Changes to your shader source code exist only within the Metal debugger. Your original shader source code doesn’t change.
If your shader results look correct after reloading the shader, make sure that you copy your changes to your original shader source code.

Changes to your shader source code exist only within the Metal debugger. Your original shader source code doesn’t change.
If your shader results look correct after reloading the shader, make sure that you copy your changes to your original shader source code.

To learn more, see [`Debugging the shaders within a draw command or compute dispatch`](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md).

## See Also

- [Capturing a Metal workload in Xcode](capturing-a-metal-workload-in-xcode.md)
  Analyze your app’s performance by configuring your project to use the Metal debugger.
- [Capturing a Metal workload programmatically](capturing-a-metal-workload-programmatically.md)
  Analyze your app’s performance by invoking Metal’s frame capture.
- [Replaying a GPU trace file](replaying-a-gpu-trace-file.md)
  Debug and profile your app’s performance using a GPU trace file in the Metal debugger.
- [Optimizing GPU performance](optimizing-gpu-performance.md)
  Find and address performance bottlenecks using the Metal debugger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/investigating-visual-artifacts)*