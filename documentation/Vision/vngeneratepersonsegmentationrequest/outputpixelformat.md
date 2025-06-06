# outputPixelFormat

**Framework**: Vision  
**Kind**: property

The pixel format of the output image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var outputPixelFormat: OSType { get set }
```

#### Discussion

The property supports the following values:

- [`kCVPixelFormatType_OneComponent8`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent8)
- [`kCVPixelFormatType_OneComponent16Half`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent16Half)
- [`kCVPixelFormatType_OneComponent32Float`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent32Float)

The default value is [`kCVPixelFormatType_OneComponent8`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent8).

## See Also

- [var qualityLevel: VNGeneratePersonSegmentationRequest.QualityLevel](vngeneratepersonsegmentationrequest/qualitylevel-swift.property.md)
  A value that indicates how the request balances accuracy and performance.
- [VNGeneratePersonSegmentationRequest.QualityLevel](vngeneratepersonsegmentationrequest/qualitylevel-swift.enum.md)
  Constants that define the levels of quality for a person segmentation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeneratepersonsegmentationrequest/outputpixelformat)*