# Inspecting the attachments of a draw command

**Framework**: Xcode

Discover attachment issues by inspecting individual pixels and samples.

#### Overview

The Metal debugger allows you to view the contents of render attachments with the Attachments viewer. You can inspect individual pixels (or samples) and debug them with the shader debugger. For more information, see [`Inspecting the bound resources for a command`](inspecting-the-bound-resources-for-a-command.md).

##### Inspect Your Attachments

The Attachments viewer contains several controls you can use to interact with and display your attachments. Each visible attachment has its own viewer and title bar, which contains attachment-specific controls. The control bar at the bottom of the Attachments viewer contains controls that operate on all of the attachments simultaneously.

![A screenshot of the Attachments viewer.](https://docs-assets.developer.apple.com/published/588b92c9ec3e839b49b555eec427c17b/gputools-metal-debugger-av-attachments-hero%402x.png)

##### Flip Your Attachments

If your renderer is using a different coordinate system and your attachment is upside down or flipped horizontally, you can flip it to the correct orientation in the Attachments viewer. Click the attachment actions button, then choose Flip Horizontally or Flip Vertically.

![A screenshot of the actions menu for an attachment. The Flip Horizontally menu item is highlighted.](https://docs-assets.developer.apple.com/published/953c6850a97d2ba36668d3176a012e3b/gputools-metal-debugger-av-flip%402x.png)

##### Configure Visible Attachments

You can configure visible attachments using the preview controls on the left of the control bar. To hide or show an attachment, move your pointer over the attachment preview and click to toggle its visibility.

Xcode updates the previews for the hidden attachments too, so you can see at a glance whether they contain anything interesting.

![A screenshot of the control to show and hide attachments.](https://docs-assets.developer.apple.com/published/5a0620cfd26dcd7a793c60156c2e95c2/gputools-metal-debugger-av-attachments-visible%402x.png)

##### Toggle Overlay Visibility

To hide overlays, such as the fluorescent green outline, click the attachment and then click a selected overlay to deselect it.

![A screenshot of the context menu for an attachment. The outline overlay option is enabled and highlighted.](https://docs-assets.developer.apple.com/published/399d002bc3aa4e109f5c615e2fc584fe/gputools-metal-debugger-av-outline-disable%402x.png)

##### Configure Attachment Rendering

Xcode automatically configures the color properties based on your encoder and attachment, but you can configure them manually by clicking the Colors button in the attachment-specific controls. Follow these guidelines:

- Use the same color space that you use for rendering. Xcode automatically configures it to the [`colorspace`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer/colorspace) property that your app sets on the [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer). If you don’t set this property, configure the color space in the Attachments viewer to the one that the device display uses.
For example, use sRGB if you’re debugging an iPhone workload.
- If you’re using a display that supports extended dynamic range, you can enable the Extended Dynamic Range Content option to render the attachment with extended range. When this option is enabled, Xcode draws hatching on any pixels containing values above your display EDR headroom. Lower the brightness of your display to increase the available headroom.
- Xcode shows additional controls to manually configure rendering if you select Default (No color-match) as the color space. You can then configure the range of visible colors, channel swizzling, and whether the alpha is premultiplied.

![A screenshot of the Texture Image Color Options popover. It consists of controls for color space, tone mapping, and color sizzling.](https://docs-assets.developer.apple.com/published/56d386690aed71e9fc0d068abea525f7/gputools-metal-debugger-av-colors%402x.png)

##### View Attachment Properties

You can view properties for an attachment, such as texture width and height, by clicking the Info button in the attachment-specific controls.

![A screenshot of the Texture Image Properties popover.](https://docs-assets.developer.apple.com/published/5f62eb3df2478b1d20c147ec13106f32/gputools-metal-debugger-av-properties%402x.png)

##### View Attachment Issues

The Issues button in the attachment-specific controls becomes active if your attachment contains any pixels (or samples) with values that are infinite, are not-a-number, or exceed the current EDR headroom of your display. For example, if you accidently divide by `0` in your fragment shader, Xcode draws hatching on any incorrect pixels (or samples).

You can click the Issues button to see more information, and then click the Jump button to focus on a pixel (or sample) causing the issue.

![A screenshot of the Issues popover showing that there are pixels exceeding the display EDR headroom. A button appears next to the message for jumping to one such pixel.](https://docs-assets.developer.apple.com/published/3f768ba5ee6f58d9c61519bc12d4bb0f/gputools-metal-debugger-av-issues%402x.png)

##### Inspect Pixel Values

Move the pointer over a pixel or sample to inspect its value.

![A screenshot of the value inspector when the pointer is hovering over a pixel.](https://docs-assets.developer.apple.com/published/e851563aeb33dfb72f91d1d485baf7d3/gputools-metal-debugger-av-inspect-pixel%402x.png)

##### Inspect Select and Compare Pixel Values

Move the pointer over a pixel (or sample if your render pass does multisample antialiasing) to inspect its value.

Then, you can select the pixel by clicking it. Alternatively, you can click and hold so that Xcode selects the pixel, zooms in, and immediately opens the value inspector.

You can also select a pixel using the coordinate input controls on the right of the control bar. Type in the coordinates for the pixel you want, such as `X: 100` and `Y: 100`. Depending on your texture configuration, Xcode may show additional controls, such as the sample index.

![A screenshot of the control bar highlighting the coordinate input controls.](https://docs-assets.developer.apple.com/published/65094c24c991cd75d62168e2a1a1b22f/gputools-metal-debugger-av-selection%402x.png)

If the selected pixel is inside a debuggable region, the coordinates are highlighted in green (see “Debug a pixel” below). If the selected pixel is outside of such a region, Xcode highlights it using your system accent color instead.

Click the Jump button in the control bar to zoom in to the selected pixel or sample. Xcode automatically focuses when you click the stepper to the right of each text field.

![A screenshot of the control bar highlighting the Jump button.](https://docs-assets.developer.apple.com/published/a1602e8352aa88fd5b382e6d3cd9f035/gputools-metal-debugger-av-selection-jump%402x.png)

You can also move the pointer over a different pixel (or sample) to compare the values. If the selected pixel is to the left of the pixel beneath the pointer, the values of the selected pixel appear on the left of the inspector. If it’s to the right, the values appear on the right. Xcode highlights the coordinates for the selected pixel in the inspector to show which values correspond to which pixel.

If you open multiple Attachment viewers or Texture viewers, you can compare pixels across different textures. For more information, see [`Inspecting textures`](inspecting-textures.md). For more information on configuring editors within your Xcode workspace, see [`Configuring the Xcode project window`](configuring-the-xcode-project-window.md).

![A screenshot of the value inspector comparing the pixel values beneath the pointer and at the selection. The pointer is hovering over pixel 1221, 1030, and the selection is at pixel 1229, 1030.](https://docs-assets.developer.apple.com/published/8aabff67717d10db2bdad23b235c5a66/gputools-metal-debugger-av-compare%402x.png)

##### Debug a Pixel

Xcode outlines any regions affected by the current draw command with a fluorescent green overlay. If you notice pixels (or samples) with unexpected values inside these regions, select them and then click the Debug button on the right of the control bar to begin debugging the fragment shader. Xcode automatically opens your fragment shader source code with detailed thread execution history for the pixel. For more information on debugging shaders, see [`Debugging the shaders within a draw command or compute dispatch`](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md).

![A screenshot of the Attachments viewer. The Debug button in the control bar is highlighted.](https://docs-assets.developer.apple.com/published/94d65b40fa4bf636285adbd4e78f3699/gputools-metal-debugger-av-debug-2%402x.png)

## See Also

- [Inspecting the bound resources for a command](inspecting-the-bound-resources-for-a-command.md)
  Discover issues by examining the bound resources at any point in an encoder.
- [Inspecting the geometry of a draw command](inspecting-the-geometry-of-a-draw-command.md)
  Find problems in your app’s vertex, object, or mesh function by examining the current geometry.
- [Debugging the shaders within a draw command or compute dispatch](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md)
  Identify and fix problematic shaders in your app using the shader debugger.
- [Analyzing draw command and compute dispatch performance with GPU counters](analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.md)
  Identify issues within your frame capture by examining performance counters.
- [Analyzing draw command and compute dispatch performance with pipeline statistics](analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.md)
  Identify issues within your frame capture by examining pipeline statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/inspecting-the-attachments-of-a-draw-command)*