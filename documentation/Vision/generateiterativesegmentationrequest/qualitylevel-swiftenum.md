# GenerateIterativeSegmentationRequest.QualityLevel

**Framework**: Vision  
**Kind**: enum

The resolution and quality of the segmentation mask the request produces.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum QualityLevel
```

#### Overview

Higher quality levels produce a smoother, higher-resolution mask. Lower quality levels favor speed over resolution.

## Topics

### Quality cases
- [GenerateIterativeSegmentationRequest.QualityLevel.accurate](generateiterativesegmentationrequest/qualitylevel-swift.enum/accurate.md)
  Produces a high-resolution mask.
- [GenerateIterativeSegmentationRequest.QualityLevel.balanced](generateiterativesegmentationrequest/qualitylevel-swift.enum/balanced.md)
  Produces a medium-resolution mask that balances speed and accuracy. This is the default setting.
- [GenerateIterativeSegmentationRequest.QualityLevel.fast](generateiterativesegmentationrequest/qualitylevel-swift.enum/fast.md)
  Produces a low-resolution mask, but runs very quickly.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var qualityLevel: GenerateIterativeSegmentationRequest.QualityLevel](generateiterativesegmentationrequest/qualitylevel-swift.property.md)
  Controls the resolution of the produced mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/qualitylevel-swift.enum)*