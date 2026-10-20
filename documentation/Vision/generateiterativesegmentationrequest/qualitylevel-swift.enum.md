# GenerateIterativeSegmentationRequest.QualityLevel

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

The resolution and quality of the segmentation mask the request produces.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum QualityLevel
```

#### Overview

Higher quality levels produce a smoother, higher-resolution mask. Lower quality levels favor speed over resolution.

## Topics

### Quality cases
- [GenerateIterativeSegmentationRequest.QualityLevel.accurate](./qualitylevel-swift.enum/accurate.md)
  Produces a high-resolution mask.
- [GenerateIterativeSegmentationRequest.QualityLevel.balanced](./qualitylevel-swift.enum/balanced.md)
  Produces a medium-resolution mask that balances speed and accuracy. This is the default setting.
- [GenerateIterativeSegmentationRequest.QualityLevel.fast](./qualitylevel-swift.enum/fast.md)
  Produces a low-resolution mask, but runs very quickly.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the quality level
- [var qualityLevel: GenerateIterativeSegmentationRequest.QualityLevel](./qualitylevel-swift.property.md)
  Controls the resolution of the produced mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/qualitylevel-swift.enum)*