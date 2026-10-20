# VNGeneratePersonSegmentationRequest.QualityLevel

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

Constants that define the levels of quality for a person segmentation request.

## Declaration

```swift
enum QualityLevel
```

```c
enum VNGeneratePersonSegmentationRequestQualityLevel : NSUInteger;
```

## Topics

### Quality Levels
- [VNGeneratePersonSegmentationRequest.QualityLevel.accurate](./qualitylevel-swift.enum/accurate.md)
  Prefers image quality over performance.
- [VNGeneratePersonSegmentationRequest.QualityLevel.balanced](./qualitylevel-swift.enum/balanced.md)
  Prefers processing that balances image quality and performance.
- [VNGeneratePersonSegmentationRequest.QualityLevel.fast](./qualitylevel-swift.enum/fast.md)
  Prefers performance over image quality.
### Creating a Quality Level
- [init?(rawValue: UInt)](./qualitylevel-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the Request
- [var outputPixelFormat: OSType](./outputpixelformat.md)
  The pixel format of the output image.
- [var qualityLevel: VNGeneratePersonSegmentationRequest.QualityLevel](./qualitylevel-swift.property.md)
  A value that indicates how the request balances accuracy and performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeneratepersonsegmentationrequest/qualitylevel-swift.enum)*