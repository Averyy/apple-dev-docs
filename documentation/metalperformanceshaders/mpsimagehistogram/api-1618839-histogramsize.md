# histogramSize(forSourceFormat:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

The amount of space the histogram will take up in the output buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func histogramSize(forSourceFormat sourceFormat: MTLPixelFormat) -> Int
```

#### Return_value

The number of bytes needed to store the histogram results.

#### Discussion

This convenience function calculates the minimum amount of space needed in the output histogram for the results. The buffer should be at least this length and longer if the `histogramOffset` value in the [`encode(to:sourceTexture:histogram:histogramOffset:)`](mpsimagehistogram/1618853-encode.md) method is non-zero.

## Parameters

- `sourceFormat`: The pixel format of the source image, corresponding to the   object of the   method.

## See Also

- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagehistogram/1618910-init.md)
  Initializes a histogram with specific information.
- [struct MPSImageHistogramInfo](mpsimagehistograminfo.md)
  The information used to compute the histogram channels of an image.
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](mpsimagehistogram/1618853-encode.md)
  Encodes the filter to a command buffer using a compute command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618839-histogramsize)*