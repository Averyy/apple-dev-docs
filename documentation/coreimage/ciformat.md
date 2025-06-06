# CIFormat

**Framework**: Core Image  
**Kind**: struct

Pixel data formats for image input, output, and processing.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CIFormat
```

## Topics

### Image Formats
- [static let A16: CIFormat](ciformat/1438171-a16.md)
  A 16-bit-per-pixel, fixed-point pixel format in which the sole component is alpha.
- [static let A8: CIFormat](ciformat/1438141-a8.md)
  An 8-bit-per-pixel, fixed-point pixel format in which the sole component is alpha.
- [static let ABGR8: CIFormat](ciformat/1437726-abgr8.md)
  A 32-bit-per-pixel, fixed-point pixel format in which the alpha value precedes the blue, green, and red color components.
- [static let ARGB8: CIFormat](ciformat/1437883-argb8.md)
  A 32-bit-per-pixel, fixed-point pixel format in which the alpha value precedes the red, green, and blue color components.
- [static let Af: CIFormat](ciformat/1438259-af.md)
  A 32-bit-per-pixel, full-width floating-point pixel format in which the sole component is alpha.
- [static let Ah: CIFormat](ciformat/1438161-ah.md)
  A 16-bit-per-pixel, half-width floating-point pixel format in which the sole component is alpha.
- [static let BGRA8: CIFormat](ciformat/1438064-bgra8.md)
  A 32-bit-per-pixel, fixed-point pixel format in which the blue, green, and red color components precede the alpha value.
- [static let R16: CIFormat](ciformat/1437646-r16.md)
  A 16-bit-per-pixel, fixed-point pixel format in which the sole component is a red color value.
- [static let R8: CIFormat](ciformat/1437695-r8.md)
  An 8-bit-per-pixel, fixed-point pixel format in which the sole component is a red color value.
- [static let RG16: CIFormat](ciformat/1437648-rg16.md)
  A 32-bit-per-pixel, fixed-point pixel format with only red and green color components.
- [static let RG8: CIFormat](ciformat/1438080-rg8.md)
  A 16-bit-per-pixel, fixed-point pixel format with only red and green color components.
- [static let RGB10: CIFormat](ciformat/4226855-rgb10.md)
- [static let RGBA16: CIFormat](ciformat/1437999-rgba16.md)
  A 64-bit-per-pixel, fixed-point pixel format.
- [static let RGBX16: CIFormat](ciformat/4245766-rgbx16.md)
- [static let RGBA8: CIFormat](ciformat/1438063-rgba8.md)
  A 32-bit-per-pixel, fixed-point pixel format in which the red, green, and blue color components precede the alpha value.
- [static let RGBAf: CIFormat](ciformat/1437756-rgbaf.md)
  A 128-bit-per-pixel, floating-point pixel format.
- [static let rgbXf: CIFormat](ciformat/4245767-rgbxf.md)
- [static let RGBAh: CIFormat](ciformat/1437998-rgbah.md)
  A 64-bit-per-pixel, floating-point pixel format.
- [static let rgbXh: CIFormat](ciformat/4245768-rgbxh.md)
- [static let RGf: CIFormat](ciformat/1438157-rgf.md)
  A 64-bit-per-pixel, floating-point pixel format with only red and green color components.
- [static let RGh: CIFormat](ciformat/1437729-rgh.md)
  A 32-bit-per-pixel, floating-point pixel format with only red and green color components.
- [static let Rf: CIFormat](ciformat/1437668-rf.md)
  A 32-bit-per-pixel, floating-point pixel format in which the sole component is a red color value.
- [static let Rh: CIFormat](ciformat/1438219-rh.md)
  A 16-bit-per-pixel, floating-point pixel format in which the sole component is a red color value.
- [static let L16: CIFormat](ciformat/2867345-l16.md)
  A 16-bit-per-pixel, fixed-point pixel format in which the sole component is luminance.
- [static let L8: CIFormat](ciformat/2867387-l8.md)
  An 8-bit-per-pixel, fixed-point pixel format in which the sole component is luminance.
- [static let LA16: CIFormat](ciformat/2867382-la16.md)
  A 32-bit-per-pixel, fixed-point pixel format with only 16-bit luminance and alpha components.
- [static let LA8: CIFormat](ciformat/2867355-la8.md)
  A 16-bit-per-pixel, fixed-point pixel format with only 8-bit luminance and alpha components.
- [static let LAf: CIFormat](ciformat/2867390-laf.md)
  A 64-bit-per-pixel, full-width floating-point pixel format with 32-bit luminance and alpha components.
- [static let LAh: CIFormat](ciformat/2867344-lah.md)
  A 32-bit-per-pixel, half-width floating-point pixel format with 16-bit luminance and alpha components.
- [static let Lf: CIFormat](ciformat/2867381-lf.md)
  A 32-bit-per-pixel, full-width floating-point pixel format in which the sole component is luminance.
- [static let Lh: CIFormat](ciformat/2867349-lh.md)
  A 16-bit-per-pixel, half-width floating-point pixel format in which the sole component is luminance.
### Initializers
- [init(rawValue: Int32)](ciformat/2998471-init.md)

## Relationships

### Conforms To
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [Writing Custom Kernels](writing_custom_kernels.md)
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