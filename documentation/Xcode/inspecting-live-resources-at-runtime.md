# Inspecting live resources at runtime

**Framework**: Xcode

Validate your resources by viewing the contents of your textures and buffers while debugging your Metal app.

#### Overview

You can preview contents of textures and buffers while debugging your app in Xcode by pausing on a breakpoint, inspecting a variable that references the resource, and then clicking the Preview button. This is one quick way to validate that your resources have the correct contents while debugging at runtime.

> ❗ **Important**: If you disable GPU Frame Capture, you can’t inspect resource content while your app is running. See [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md) to learn how to reenable it.

If you disable GPU Frame Capture, you can’t inspect resource content while your app is running. See [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md) to learn how to reenable it.

##### Inspect Your Textures and Buffers

First, pause the app inside a scope that contains a variable referencing the resource. You can achieve this by setting a breakpoint on a line that references the resource. To set a breakpoint, click the line number to the left of the source editor. The example below shows a breakpoint for the line where `_skyMap` is bound to the render encoder:

![A screenshot of Xcode’s source editor, highlighting a line of code with a breakpoint.](https://docs-assets.developer.apple.com/published/f33f01dc549725c850875379bfa880f1/gputools-quick-look-set-breakpoint%402x.png)

Then, when yor app pauses at the breakpoint, move the pointer over the variable referencing the resource to reveal the Value inspector.

![A screenshot of the source editor, breaking at a line of code with a breakpoint. The variable underscore sky map is highlighted.](https://docs-assets.developer.apple.com/published/24adafad63942811b270bcf3df4145c2/gputools-quick-look-hit-breakpoint%402x.png)

Finally, click the Preview button to show the contents of the resource.

![A screenshot of the Preview popover showing the contents of the variable underscore sky map.](https://docs-assets.developer.apple.com/published/25eff4f8f589d29d1b0b63e375b2cf18/gputools-quick-look-preview%402x.png)

If the resource is a texture and has multiple slices, like the sky map above, you can drag the slider at the bottom of the Preview popover to see each slice. If the resource has any unexpected values, you can investigate further with the Metal debugger (see [`Investigating visual artifacts`](investigating-visual-artifacts.md)).

## See Also

- [Validating your app’s Metal API usage](validating-your-apps-metal-api-usage.md)
  Catch runtime issues in your Metal app using API Validation.
- [Validating your app’s Metal shader usage](validating-your-apps-metal-shader-usage.md)
  Catch common shader runtime issues using Shader Validation while your app is running.
- [Monitoring your Metal app’s graphics performance](monitoring-your-metal-apps-graphics-performance.md)
  Catch performance issues using the Metal Performance HUD while your app is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/inspecting-live-resources-at-runtime)*