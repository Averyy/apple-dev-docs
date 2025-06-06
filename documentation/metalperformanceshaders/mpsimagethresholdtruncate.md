# MPSImageThresholdTruncate

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that clamps the return value to an upper specified value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageThresholdTruncate : MPSUnaryImageKernel
```

#### Overview

An [`MPSImageThresholdTruncate`](mpsimagethresholdtruncate.md) filter converts a single channel image to a binary image. If the input image is not a single channel image, the function first converts the input image into a single channel luminance image using the linear gray color transform, and then it applies the threshold.

[`Listing 1`](mpsimagethresholdtruncate#2851307.md) shows the threshold truncate function.

```other
destinationPixelValue = sourcePixelValue > thresholdValue ? thresholdValue : sourcePixelValue
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagethresholdtruncate/2865664-init.md)
### Methods
- [init(device: any MTLDevice, thresholdValue: Float, linearGrayColorTransform: UnsafePointer<Float>?)](mpsimagethresholdtruncate/1618818-init.md)
  Initializes the kernel.
### Properties
- [var thresholdValue: Float](mpsimagethresholdtruncate/1618882-thresholdvalue.md)
  The threshold value used to initialize the threshold filter.
- [var transform: UnsafePointer<Float>](mpsimagethresholdtruncate/1618787-transform.md)
  The color transform used to initialize the threshold filter.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)

## See Also

- [class MPSImageThresholdBinary](mpsimagethresholdbinary.md)
  A filter that returns a specified value for each pixel with a value greater than a specified threshold or 0 otherwise. 
- [class MPSImageThresholdBinaryInverse](mpsimagethresholdbinaryinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or a specified value otherwise. 
- [class MPSImageThresholdToZero](mpsimagethresholdtozero.md)
  A filter that returns the original value for each pixel with a value greater than a specified threshold or 0 otherwise. 
- [class MPSImageThresholdToZeroInverse](mpsimagethresholdtozeroinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or the original value otherwise. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtruncate)*