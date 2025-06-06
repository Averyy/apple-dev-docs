# MPSImageStatisticsMinAndMax

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel that computes the minimum and maximum pixel values for a given region of an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageStatisticsMinAndMax : MPSUnaryImageKernel
```

#### Overview

The minimum and maximum values are written to the destination image at the following pixel locations:

- Minimum value is written at pixel location` (0, 0)`
- Maximum value is written at pixel location `(1, 0)`

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagestatisticsminandmax/2867026-init.md)
- [init(device: any MTLDevice)](mpsimagestatisticsminandmax/2867125-init.md)
### Instance Properties
- [var clipRectSource: MTLRegion](mpsimagestatisticsminandmax/2867045-cliprectsource.md)

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)

## See Also

- [class MPSImageStatisticsMean](mpsimagestatisticsmean.md)
  A kernel that computes the mean for a given region of an image.
- [class MPSImageStatisticsMeanAndVariance](mpsimagestatisticsmeanandvariance.md)
  A kernel that computes the mean and variance for a given region of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagestatisticsminandmax)*