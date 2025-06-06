# MPSImageNormalizedHistogram

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that computes the normalized histogram of an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageNormalizedHistogram : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagenormalizedhistogram/3019325-init.md)
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagenormalizedhistogram/3019326-init.md)
### Instance Properties
- [var clipRectSource: MTLRegion](mpsimagenormalizedhistogram/3019321-cliprectsource.md)
- [var histogramInfo: MPSImageHistogramInfo](mpsimagenormalizedhistogram/3019323-histograminfo.md)
- [var zeroHistogram: Bool](mpsimagenormalizedhistogram/3019327-zerohistogram.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, minmaxTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](mpsimagenormalizedhistogram/3019322-encode.md)
- [func histogramSize(forSourceFormat: MTLPixelFormat) -> Int](mpsimagenormalizedhistogram/3019324-histogramsize.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagenormalizedhistogram)*