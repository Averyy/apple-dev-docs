# histogramInfo

**Framework**: Metal Performance Shaders  
**Kind**: instp

A structure describing the histogram content.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var histogramInfo: MPSImageHistogramInfo { get }
```

#### Discussion

Returns a structure describing the format of the histogram.

## See Also

- [var clipRectSource: MTLRegion](mpsimagehistogram/1618765-cliprectsource.md)
  The source rectangle to use when reading data.
- [var zeroHistogram: Bool](mpsimagehistogram/1618891-zerohistogram.md)
  Determines whether to zero-initialize the histogram results.
- [var minPixelThresholdValue: vector_float4](mpsimagehistogram/2867008-minpixelthresholdvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618844-histograminfo)*