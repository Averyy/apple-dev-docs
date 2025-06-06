# MPSImageIntegral

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that calculates the sum of pixels over a specified region in an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageIntegral : MPSUnaryImageKernel
```

#### Overview

 The value at each position is the sum of all pixels in a source image rectangle, `sumRect. `[`Listing 1`](mpsimageintegral#2556914.md) shows the pseudocode used to calculate `sumRect`.

```occ
sumRect.origin = filter.offset
sumRect.size = dest_position - filter.clipRect.origin
```

If the channels in the source image are normalized, half-float or floating values, the destination image is recommended to be a 32-bit floating-point image. If the channels in the source image are integer values, it is recommended that an appropriate 32-bit integer image destination format is used.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)

## See Also

- [class MPSImageIntegralOfSquares](mpsimageintegralofsquares.md)
  A filter that calculates the sum of squared pixels over a specified region in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageintegral)*