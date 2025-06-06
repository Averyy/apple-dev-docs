# CIFilterShape

**Framework**: Core Image  
**Kind**: cl

A description of the bounding shape of a filter and the domain of definition for a filter operation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIFilterShape : NSObject
```

#### Overview

You use `CIFilterShape` objects in conjunction with Core Image classes, such as [`CIFilter`](cifilter.md), [`CIKernel`](cikernel.md), and [`CISampler`](cisampler.md), to create custom filters.

## Topics

### Initializing a Filter Shape
- [init(rect: CGRect)](cifiltershape/1437921-init.md)
  Initializes a filter shape object with a rectangle.
### Inspecting a Filter Shape
- [var extent: CGRect](cifiltershape/1438022-extent.md)
  The extent of the filter shape.
### Modifying a Filter Shape
- [func insetBy(x: Int32, y: Int32) -> CIFilterShape](cifiltershape/1437987-insetby.md)
  Modifies a filter shape object so that it is inset by the specified x and y values.
- [func intersect(with: CIFilterShape) -> CIFilterShape](cifiltershape/1437881-intersect.md)
  Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.
- [func intersect(with: CGRect) -> CIFilterShape](cifiltershape/1437806-intersect.md)
  Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [func transform(by: CGAffineTransform, interior: Bool) -> CIFilterShape](cifiltershape/1437808-transform.md)
  Creates a filter shape that results from applying a transform to the current filter shape.
- [func union(with: CIFilterShape) -> CIFilterShape](cifiltershape/1438227-union.md)
  Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [func union(with: CGRect) -> CIFilterShape](cifiltershape/1437601-union.md)
  Creates a filter shape that results from the union of the current filter shape and a rectangle.

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
- [class CISampler](cisampler.md)
  An object that retrieves pixel samples for processing by a filter kernel.
- [struct CIFormat](ciformat.md)
  Pixel data formats for image input, output, and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltershape)*