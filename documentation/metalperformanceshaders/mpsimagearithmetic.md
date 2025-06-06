# MPSImageArithmetic

**Framework**: Metal Performance Shaders  
**Kind**: cl

Base class for basic arithmetic nodes

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageArithmetic : MPSBinaryImageKernel
```

## Topics

### Instance Properties
- [var bias: Float](mpsimagearithmetic/2866609-bias.md)
- [var primaryScale: Float](mpsimagearithmetic/2866602-primaryscale.md)
- [var primaryStrideInPixels: MTLSize](mpsimagearithmetic/2889864-primarystrideinpixels.md)
- [var secondaryScale: Float](mpsimagearithmetic/2866601-secondaryscale.md)
- [var secondaryStrideInPixels: MTLSize](mpsimagearithmetic/2889865-secondarystrideinpixels.md)
- [var maximumValue: Float](mpsimagearithmetic/2942356-maximumvalue.md)
- [var minimumValue: Float](mpsimagearithmetic/2942357-minimumvalue.md)

## Relationships

### Inherits From
- [MPSBinaryImageKernel](mpsbinaryimagekernel.md)

## See Also

- [class MPSImageAdd](mpsimageadd.md)
  A filter that returns the element-wise sum of its two input images.
- [class MPSImageSubtract](mpsimagesubtract.md)
  A filter that returns the element-wise difference of its two input images.
- [class MPSImageMultiply](mpsimagemultiply.md)
  A filter that returns the element-wise product of its two input images.
- [class MPSImageDivide](mpsimagedivide.md)
  A filter that returns the element-wise quotient of its two input images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagearithmetic)*