# CIFormat

**Framework**: Core Image  
**Kind**: struct

Pixel data formats for image input, output, and processing.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct CIFormat
```

## Topics

### Image Formats
- [static let A16: CIFormat](ciformat/a16.md)
  A 16-bit-per-pixel, fixed-point pixel format in which the sole component is alpha.
- [static let A8: CIFormat](ciformat/a8.md)
  An 8-bit-per-pixel, fixed-point pixel format in which the sole component is alpha.
- [static let ABGR8: CIFormat](ciformat/abgr8.md)
  A 32-bit-per-pixel, fixed-point pixel format in which the alpha value precedes the blue, green, and red color components.
- [static let ARGB8: CIFormat](ciformat/argb8.md)
  A 32-bit-per-pixel, fixed-point pixel format in which the alpha value precedes the red, green, and blue color components.
- [static let Af: CIFormat](ciformat/af.md)
  A 32-bit-per-pixel, full-width floating-point pixel format in which the sole component is alpha.
- [static let Ah: CIFormat](ciformat/ah.md)
  A 16-bit-per-pixel, half-width floating-point pixel format in which the sole component is alpha.
- [static let BGRA8: CIFormat](ciformat/bgra8.md)
  A 32-bit-per-pixel, fixed-point pixel format in which the blue, green, and red color components precede the alpha value.
- [static let R16: CIFormat](ciformat/r16.md)
  A 16-bit-per-pixel, fixed-point pixel format in which the sole component is a red color value.
- [static let R8: CIFormat](ciformat/r8.md)
  An 8-bit-per-pixel, fixed-point pixel format in which the sole component is a red color value.
- [static let RG16: CIFormat](ciformat/rg16.md)
  A 32-bit-per-pixel, fixed-point pixel format with only red and green color components.
- [static let RG8: CIFormat](ciformat/rg8.md)
  A 16-bit-per-pixel, fixed-point pixel format with only red and green color components.
- [static let RGB10: CIFormat](ciformat/rgb10.md)
- [static let RGBA16: CIFormat](ciformat/rgba16.md)
  A 64-bit-per-pixel, fixed-point pixel format.
- [static let RGBX16: CIFormat](ciformat/rgbx16.md)
- [static let RGBA8: CIFormat](ciformat/rgba8.md)
  A 32-bit-per-pixel, fixed-point pixel format in which the red, green, and blue color components precede the alpha value.
- [static let RGBAf: CIFormat](ciformat/rgbaf.md)
  A 128-bit-per-pixel, floating-point pixel format.
- [static let rgbXf: CIFormat](ciformat/rgbxf.md)
- [static let RGBAh: CIFormat](ciformat/rgbah.md)
  A 64-bit-per-pixel, floating-point pixel format.
- [static let rgbXh: CIFormat](ciformat/rgbxh.md)
- [static let RGf: CIFormat](ciformat/rgf.md)
  A 64-bit-per-pixel, floating-point pixel format with only red and green color components.
- [static let RGh: CIFormat](ciformat/rgh.md)
  A 32-bit-per-pixel, floating-point pixel format with only red and green color components.
- [static let Rf: CIFormat](ciformat/rf.md)
  A 32-bit-per-pixel, floating-point pixel format in which the sole component is a red color value.
- [static let Rh: CIFormat](ciformat/rh.md)
  A 16-bit-per-pixel, floating-point pixel format in which the sole component is a red color value.
- [static let L16: CIFormat](ciformat/l16.md)
  A 16-bit-per-pixel, fixed-point pixel format in which the sole component is luminance.
- [static let L8: CIFormat](ciformat/l8.md)
  An 8-bit-per-pixel, fixed-point pixel format in which the sole component is luminance.
- [static let LA16: CIFormat](ciformat/la16.md)
  A 32-bit-per-pixel, fixed-point pixel format with only 16-bit luminance and alpha components.
- [static let LA8: CIFormat](ciformat/la8.md)
  A 16-bit-per-pixel, fixed-point pixel format with only 8-bit luminance and alpha components.
- [static let LAf: CIFormat](ciformat/laf.md)
  A 64-bit-per-pixel, full-width floating-point pixel format with 32-bit luminance and alpha components.
- [static let LAh: CIFormat](ciformat/lah.md)
  A 32-bit-per-pixel, half-width floating-point pixel format with 16-bit luminance and alpha components.
- [static let Lf: CIFormat](ciformat/lf.md)
  A 32-bit-per-pixel, full-width floating-point pixel format in which the sole component is luminance.
- [static let Lh: CIFormat](ciformat/lh.md)
  A 16-bit-per-pixel, half-width floating-point pixel format in which the sole component is luminance.
### Initializers
- [init(rawValue: Int32)](ciformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Writing Custom Kernels](writing-custom-kernels.md)
  Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [class CIKernel](cikernel.md)
  A GPU-based image-processing routine used to create custom Core Image filters.
- [class CIColorKernel](cicolorkernel.md)
  A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [class CIWarpKernel](ciwarpkernel.md)
  A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [class CIBlendKernel](ciblendkernel.md)
  A GPU-based image-processing routine that is optimized for blending two images.
- [class CISampler](cisampler.md)
  An object that retrieves pixel samples for processing by a filter kernel.
- [class CIFilterShape](cifiltershape.md)
  A description of the bounding shape of a filter and the domain of definition for a filter operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciformat)*