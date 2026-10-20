# Inspecting sampler states

**Framework**: Xcode  
**Role**: Article

Verify your sampler state configurations by examining their properties.

#### Overview

The Metal debugger allows you to inspect a sampler state with the Sampler State viewer. After opening a sampler state, you can view its associated properties and preview the sampling behavior. For more information, see [Inspecting the bound resources for a command](./inspecting-the-bound-resources-for-a-command.md) or [Analyzing memory usage](./analyzing-memory-usage.md).

##### Navigate your sampler state

The Sampler State viewer shows the properties of your sampler state on the left (as configured by [`MTLSamplerDescriptor`](../Metal/mtlsamplerdescriptor.md)) and a preview on the right. The preview illustrates how pixels in a texture appear when using your sampler state.

![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-edge address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-outline@2x.png)

The square region in the center of the preview corresponds to UV coordinates within the range of `0.0` to `1.0`.

![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-edge address mode. The region in bounds is highlighted.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-outline-green@2x.png)

You can use the preview to quickly verify the configuration for your sampler state. For example, if you want a texture to mirror, but it’s drawing a constant value instead, you can check the sampler state. In the screenshot below, the sampler state is configured to clamp to a border color that’s opaque black, rather than using mirror repeat as the address mode:

![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-border address mode. The border color is opaque black.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-nearest-clamp-border-black-plus-overview@2x.png)

##### Try various combinations

The properties you configure when creating a sampler state determine how a texture looks when sampling it. The properties related to filtering control how pixels combine when the sample footprint is either larger or smaller than a pixel, or when it’s between mipmap levels. The address mode determines the texture coordinate at each pixel when a read falls outside the bounds of a texture. You can try using different combinations of filtering and addressing modes until you achieve your desired look.

| Properties | Preview |
| --- | --- |
| [`MTLSamplerMinMagFilter.nearest`](../Metal/mtlsamplerminmagfilter/nearest.md), [`MTLSamplerAddressMode.clampToEdge`](../Metal/mtlsampleraddressmode/clamptoedge.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-edge address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-nearest-clamp@2x.png) |
| [`MTLSamplerMinMagFilter.nearest`](../Metal/mtlsamplerminmagfilter/nearest.md), [`MTLSamplerAddressMode.mirrorClampToEdge`](../Metal/mtlsampleraddressmode/mirrorclamptoedge.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and mirror-clamp-to-edge address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-nearest-mirror-clamp@2x.png) |
| [`MTLSamplerMinMagFilter.nearest`](../Metal/mtlsamplerminmagfilter/nearest.md), [`MTLSamplerAddressMode.repeat`](../Metal/mtlsampleraddressmode/repeat.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and repeat address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-nearest-repeat@2x.png) |
| [`MTLSamplerMinMagFilter.nearest`](../Metal/mtlsamplerminmagfilter/nearest.md), [`MTLSamplerAddressMode.mirrorRepeat`](../Metal/mtlsampleraddressmode/mirrorrepeat.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and mirror-repeat address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-nearest-mirror@2x.png) |
| [`MTLSamplerMinMagFilter.nearest`](../Metal/mtlsamplerminmagfilter/nearest.md), [`MTLSamplerAddressMode.clampToZero`](../Metal/mtlsampleraddressmode/clamptozero.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-zero address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-nearest-zero@2x.png) |
| [`MTLSamplerMinMagFilter.nearest`](../Metal/mtlsamplerminmagfilter/nearest.md), [`MTLSamplerAddressMode.clampToBorderColor`](../Metal/mtlsampleraddressmode/clamptobordercolor.md), [`MTLSamplerBorderColor.opaqueBlack`](../Metal/mtlsamplerbordercolor/opaqueblack.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-border address mode. The border color is opaque black.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-nearest-clamp-border-black@2x.png) |
| [`MTLSamplerMinMagFilter.nearest`](../Metal/mtlsamplerminmagfilter/nearest.md), [`MTLSamplerAddressMode.clampToBorderColor`](../Metal/mtlsampleraddressmode/clamptobordercolor.md), [`MTLSamplerBorderColor.opaqueWhite`](../Metal/mtlsamplerbordercolor/opaquewhite.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-border address mode. The border color is opaque white.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-nearest-clamp-border-white@2x.png) |
| [`MTLSamplerMinMagFilter.nearest`](../Metal/mtlsamplerminmagfilter/nearest.md), [`MTLSamplerAddressMode.clampToBorderColor`](../Metal/mtlsampleraddressmode/clamptobordercolor.md), [`MTLSamplerBorderColor.transparentBlack`](../Metal/mtlsamplerbordercolor/transparentblack.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-border address mode. The border color is transparent black.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-nearest-clamp-border-transparent@2x.png) |
| [`MTLSamplerMinMagFilter.linear`](../Metal/mtlsamplerminmagfilter/linear.md), [`MTLSamplerAddressMode.clampToEdge`](../Metal/mtlsampleraddressmode/clamptoedge.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-edge address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-linear-clamp@2x.png) |
| [`MTLSamplerMinMagFilter.linear`](../Metal/mtlsamplerminmagfilter/linear.md), [`MTLSamplerAddressMode.clampToEdge`](../Metal/mtlsampleraddressmode/clamptoedge.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and mirror-clamp-to-edge address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-linear-mirror-clamp@2x.png) |
| [`MTLSamplerMinMagFilter.linear`](../Metal/mtlsamplerminmagfilter/linear.md), [`MTLSamplerAddressMode.repeat`](../Metal/mtlsampleraddressmode/repeat.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and repeat address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-linear-repeat@2x.png) |
| [`MTLSamplerMinMagFilter.linear`](../Metal/mtlsamplerminmagfilter/linear.md), [`MTLSamplerAddressMode.mirrorRepeat`](../Metal/mtlsampleraddressmode/mirrorrepeat.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and mirror-repeat address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-linear-mirror@2x.png) |
| [`MTLSamplerMinMagFilter.linear`](../Metal/mtlsamplerminmagfilter/linear.md), [`MTLSamplerAddressMode.clampToZero`](../Metal/mtlsampleraddressmode/clamptozero.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-zero address mode.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-linear-zero@2x.png) |
| [`MTLSamplerMinMagFilter.linear`](../Metal/mtlsamplerminmagfilter/linear.md), [`MTLSamplerAddressMode.clampToBorderColor`](../Metal/mtlsampleraddressmode/clamptobordercolor.md), [`MTLSamplerBorderColor.opaqueBlack`](../Metal/mtlsamplerbordercolor/opaqueblack.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-border address mode. The border color is opaque black.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-linear-clamp-border-black@2x.png) |
| [`MTLSamplerMinMagFilter.linear`](../Metal/mtlsamplerminmagfilter/linear.md), [`MTLSamplerAddressMode.clampToBorderColor`](../Metal/mtlsampleraddressmode/clamptobordercolor.md), [`MTLSamplerBorderColor.opaqueWhite`](../Metal/mtlsamplerbordercolor/opaquewhite.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-border address mode. The border color is opaque white.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-linear-clamp-border-white@2x.png) |
| [`MTLSamplerMinMagFilter.linear`](../Metal/mtlsamplerminmagfilter/linear.md), [`MTLSamplerAddressMode.clampToBorderColor`](../Metal/mtlsampleraddressmode/clamptobordercolor.md), [`MTLSamplerBorderColor.transparentBlack`](../Metal/mtlsamplerbordercolor/transparentblack.md) | ![A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-border address mode. The border color is transparent black.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-sv-linear-clamp-border-transparent@2x.png) |

## See Also

### Metal resource inspection
- [Inspecting acceleration structures](./inspecting-acceleration-structures.md)
  Reveal ray intersection bottlenecks by examining your acceleration structures.
- [Inspecting buffers](./inspecting-buffers.md)
  Confirm your buffer formats by examining buffer content.
- [Inspecting pipeline states](./inspecting-pipeline-states.md)
  Determine how your render and compute passes behave by examining their properties.
- [Inspecting shaders](./inspecting-shaders.md)
  Improve your app’s shader performance by examining and editing your shaders.
- [Inspecting textures](./inspecting-textures.md)
  Discover issues in your textures by examining their content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/inspecting-sampler-states)*