# VNGeneratePersonSegmentationRequest.QualityLevel

**Framework**: Vision  
**Kind**: enum

Constants that define the levels of quality for a person segmentation request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum QualityLevel
```

## Topics

### Quality Levels
- [VNGeneratePersonSegmentationRequest.QualityLevel.accurate](vngeneratepersonsegmentationrequest/qualitylevel-swift.enum/accurate.md)
  Prefers image quality over performance.
- [VNGeneratePersonSegmentationRequest.QualityLevel.balanced](vngeneratepersonsegmentationrequest/qualitylevel-swift.enum/balanced.md)
  Prefers processing that balances image quality and performance.
- [VNGeneratePersonSegmentationRequest.QualityLevel.fast](vngeneratepersonsegmentationrequest/qualitylevel-swift.enum/fast.md)
  Prefers performance over image quality.
### Creating a Quality Level
- [init?(rawValue: UInt)](vngeneratepersonsegmentationrequest/qualitylevel-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var outputPixelFormat: OSType](vngeneratepersonsegmentationrequest/outputpixelformat.md)
  The pixel format of the output image.
- [var qualityLevel: VNGeneratePersonSegmentationRequest.QualityLevel](vngeneratepersonsegmentationrequest/qualitylevel-swift.property.md)
  A value that indicates how the request balances accuracy and performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeneratepersonsegmentationrequest/qualitylevel-swift.enum)*