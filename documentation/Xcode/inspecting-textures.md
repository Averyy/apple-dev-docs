# Inspecting textures

**Framework**: Xcode

Discover issues in your textures by examining their content.

#### Overview

The Metal debugger allows you to view the contents of a texture in the Texture viewer. First, flip the texture to the correct orientation and adjust the colors to ensure accuracy. Then, check for pixel issues like infinite values, not-a-number values, or any values that exceed the current EDR headroom of your display. Hover over pixels within the texture to inspect their values, then find any anomalies by selecting a pixel and comparing it with others. Finally, compare across mipmap levels to check for visual issues. For more information, see [`Inspecting the bound resources for a command`](inspecting-the-bound-resources-for-a-command.md) or [`Analyzing memory usage`](analyzing-memory-usage.md).

##### Navigate Your Texture

The Texture viewer contains several controls for interacting with and displaying your texture. If your texture contains multiple slices, such as [`MTLTextureType.type2DArray`](https://developer.apple.com/documentation/metal/mtltexturetype/type2darray), the controls in the title bar are disabled until you click a texture image. The active texture image has a system accent color border.

![A screenshot of the Texture viewer, which consists of a title bar, a canvas, and a control bar. It shows a texture with three slices, with the first texture slice selected.](/images/com.apple.Xcode/gputools-metal-debugger-tv-hero@2x.png)

Groups of texture slices that contain related content, such as the faces for a texture of type [`MTLTextureType.typeCube`](https://developer.apple.com/documentation/metal/mtltexturetype/typecube), are part of the same texture image.

##### Flip Your Texture

If your renderer is using a different coordinate system and your texture image is upside down or flipped horizontally, you can flip it to the correct orientation in the Texture viewer. Click the texture actions button, then choose Flip Horizontally or Flip Vertically. Xcode flips groups of related texture slices, such as cubemaps, as a whole, and it flips unrelated texture slices independently.

![A screenshot of the actions menu. The Flip Horizontally menu item is highlighted.](/images/com.apple.Xcode/gputools-metal-debugger-tv-flip@2x.png)

##### Configure Texture Rendering

Xcode automatically configures the color properties based on your texture, but you can configure them manually by clicking the Colors button in the title bar. You configure texture rendering on a per-texture-image basis. Follow these guidelines:

- Set the color space to the one that the device display uses. For example, use sRGB if you’re debugging an iPhone workload.
- If you’re using a display that supports extended dynamic range, you can enable the Extended Dynamic Range Content option to render the texture with extended range. When this option is enabled, Xcode draws hatching on any pixels containing values above your display EDR headroom. Consider lowering the brightness of your display to increase the available headroom.
- Xcode shows additional controls to manually configure rendering if you select Default (No color-match) as the color space. You can then configure the range of visible colors, channel swizzling, and whether the alpha is premultiplied.

![A screenshot of the Texture Image Color Options popover. It consists of controls for color space, tone mapping, and color sizzling.](/images/com.apple.Xcode/gputools-metal-debugger-tv-colors@2x.png)

##### View Texture Properties

You can view properties for the active texture image, such as width and height, by clicking the Info button in the title bar.

![A screenshot of the Texture Image Properties popover.](/images/com.apple.Xcode/gputools-metal-debugger-tv-properties@2x.png)

##### View Texture Issues

The Issues button in the title bar becomes active if your texture contains any pixels (or samples) with values that are infinite, are not-a-number, or exceed the current EDR headroom of your display.

You can click the Issues button to see more information, and then click the Jump button to focus on a pixel (or sample) causing the issue.

![A screenshot of the Issues popover indicating that there are pixels exceeding the display EDR headroom. There’s a button next to the message for jumping to one such pixel.](/images/com.apple.Xcode/gputools-metal-debugger-tv-issues@2x.png)

##### Inspect Select and Compare Pixel Values

Move the pointer over a pixel (or a sample if your texture is of type [`MTLTextureType.type2DMultisample`](https://developer.apple.com/documentation/metal/mtltexturetype/type2dmultisample) or [`MTLTextureType.type2DMultisampleArray`](https://developer.apple.com/documentation/metal/mtltexturetype/type2dmultisamplearray)) to inspect its value.

![A screenshot of the value inspector when the pointer is hovering over pixel 2077, 919.](/images/com.apple.Xcode/gputools-metal-debugger-tv-inspect-pixel@2x.png)

Then, you can select the pixel by clicking it. Alternatively, you can click and hold so that Xcode selects the pixel, zooms in, and immediately opens the value inspector.

You can also select a pixel using the coordinate input controls on the right of the control bar. Type in the coordinates for the pixel you want, such as `X: 100` and `Y: 100`. Depending on your texture configuration, Xcode may show additional controls.

![A screenshot of the control bar highlighting the coordinate input controls.](/images/com.apple.Xcode/gputools-metal-debugger-tv-selection@2x.png)

Click the Jump button in the control bar to zoom in to the selected pixel or sample. Xcode automatically focuses when you click the stepper to the right of each text field.

![A screenshot of the control bar highlighting the Jump button.](/images/com.apple.Xcode/gputools-metal-debugger-tv-selection-jump@2x.png)

You can also move the pointer over a different pixel (or sample) to compare the values. If the selected pixel is to the left of the pixel beneath the pointer, the values of the selected pixel appear on the left of the inspector. If it’s to the right, the values appear on the right. Xcode highlights the coordinates for the selected pixel in the inspector to show which values correspond to which pixel.

![A screenshot of the value inspector comparing the pixel values beneath the pointer and at the selection. The pointer is hovering over pixel 2080, 919, and the selection is at pixel 2094, 919.](/images/com.apple.Xcode/gputools-metal-debugger-tv-compare@2x.png)

If you open multiple Attachments viewers or Texture viewers, you can compare pixels across different textures. For information on configuring editors within your Xcode workspace, see [`Configuring the Xcode project window`](configuring-the-xcode-project-window.md).

##### Compare Mipmap Levels

By default, the Texture viewer shows all of your texture’s mipmap levels side by side. However, if you want to visually compare different mipmap levels, you can enable stacking. Click the texture actions button, and then choose Stack Mips.

![A screenshot of the Texture viewer showing a mipmapped cubemap texture. The actions menu is open and the Stack Mips menu item is highlighted.](/images/com.apple.Xcode/gputools-metal-debugger-tv-stack-mips@2x.png)

Drag the slice slider in the control bar to visually compare different mipmap levels.

![A screen recording of the Texture viewer visualizing the different mipmap levels of a texture as the user moves the pointer along the slider.](/images/com.apple.Xcode/gputools-metal-debugger-tv-scrub.gif)

> **Note**: By default, the Texture viewer stacks 3D textures, such as [`MTLTextureType.type3D`](https://developer.apple.com/documentation/metal/mtltexturetype/type3d), using the z-coordinate. You can disable stacking to see the depth slices side by side. If your 3D texture has multiple mipmap levels, you can choose either Stack Mips or Stack Z.

## See Also

- [Inspecting acceleration structures](inspecting-acceleration-structures.md)
  Reveal ray intersection bottlenecks by examining your acceleration structures.
- [Inspecting buffers](inspecting-buffers.md)
  Confirm your buffer formats by examining buffer content.
- [Inspecting pipeline states](inspecting-pipeline-states.md)
  Determine how your render and compute passes behave by examining their properties.
- [Inspecting sampler states](inspecting-sampler-states.md)
  Verify your sampler state configurations by examining their properties.
- [Inspecting shaders](inspecting-shaders.md)
  Improve your app’s shader performance by examining and editing your shaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/inspecting-textures)*