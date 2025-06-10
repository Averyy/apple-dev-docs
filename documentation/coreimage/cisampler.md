# CISampler

**Framework**: Core Image  
**Kind**: class

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
class CISampler
```

#### Overview

The `CISampler` class retrieves samples of images for processing by a [`CIKernel`](cikernel.md) object. A `CISampler` object defines a coordinate transform, and modes for interpolation and wrapping. You use `CISampler` objects in conjunction with other Core Image classes, such as  [`CIFilter`](cifilter-swift.class.md), `CIKernel`, and [`CIFilterShape`](cifiltershape.md), to create custom filters.

## Topics

### Initializing a Sampler
- [convenience init(image: CIImage)](cisampler/init(image:).md)
  Initializes a sampler with an image object.
- [init(image: CIImage, options: [AnyHashable : Any]?)](cisampler/init(image:options:).md)
  Initializes the sampler with an image object using options specified in a dictionary.
### Getting Information About the Sampler Object
- [var definition: CIFilterShape](cisampler/definition.md)
  The domain of definition (DOD) of the sampler
- [var extent: CGRect](cisampler/extent.md)
  The rectangle that specifies the extent of the sampler
### Constants
- [Sampler Option Keys](sampler-option-keys.md)
  Keys for creating a sampler.
- [Sampler Option Values](sampler-option-values.md)
  Values for sampler option keys.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [class CIFilterShape](cifiltershape.md)
  A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [struct CIFormat](ciformat.md)
  Pixel data formats for image input, output, and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler)*