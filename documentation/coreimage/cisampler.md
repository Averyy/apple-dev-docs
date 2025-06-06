# CISampler

**Framework**: Core Image  
**Kind**: cl

An object that retrieves pixel samples for processing by a filter kernel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CISampler : NSObject
```

#### Overview

The `CISampler` class retrieves samples of images for processing by a [`CIKernel`](cikernel.md) object. A `CISampler` object defines a coordinate transform, and modes for interpolation and wrapping. You use `CISampler` objects in conjunction with other Core Image classes, such as  [`CIFilter`](cifilter.md), [`CIKernel`](cikernel.md), and [`CIFilterShape`](cifiltershape.md), to create custom filters.

## Topics

### Initializing a Sampler
- [init(image: CIImage)](cisampler/1438117-init.md)
  Initializes a sampler with an image object.
- [init(image: CIImage, options: [AnyHashable : Any]?)](cisampler/1437963-init.md)
  Initializes the sampler with an image object using options specified in a dictionary.
### Getting Information About the Sampler Object
- [var definition: CIFilterShape](cisampler/1437877-definition.md)
  The domain of definition (DOD) of the sampler
- [var extent: CGRect](cisampler/1437872-extent.md)
  The rectangle that specifies the extent of the sampler
### Constants
- [Sampler Option Keys](cisampler/sampler_option_keys.md)
  Keys for creating a sampler.
- [Sampler Option Values](cisampler/sampler_option_values.md)
  Values for sampler option keys.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)

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
- [class CIFilterShape](cifiltershape.md)
  A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [struct CIFormat](ciformat.md)
  Pixel data formats for image input, output, and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler)*