# GeneratePersonSegmentationRequest.QualityLevel

**Framework**: Vision  
**Kind**: enum

Constants that define the levels of quality for a person-segmentation request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum QualityLevel
```

## Topics

### Getting the quality levels
- [GeneratePersonSegmentationRequest.QualityLevel.accurate](generatepersonsegmentationrequest/qualitylevel-swift.enum/accurate.md)
  A quality option that prefers image quality over performance.
- [GeneratePersonSegmentationRequest.QualityLevel.balanced](generatepersonsegmentationrequest/qualitylevel-swift.enum/balanced.md)
  A quality option that prefers processing that balances image quality and performance.
- [GeneratePersonSegmentationRequest.QualityLevel.fast](generatepersonsegmentationrequest/qualitylevel-swift.enum/fast.md)
  A quality option that prefers performance over image quality.

## Relationships

### Conforms To
- [CaseIterable](../swift/caseiterable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var qualityLevel: GeneratePersonSegmentationRequest.QualityLevel](generatepersonsegmentationrequest/qualitylevel-swift.property.md)
  A value that indicates how the request balances accuracy and performance.
- [var outputPixelFormatType: OSType](generatepersonsegmentationrequest/outputpixelformattype.md)
  The desired pixel format of the observation.
- [var supportedOutputPixelFormats: [OSType]](generatepersonsegmentationrequest/supportedoutputpixelformats.md)
  The collection of supported pixel format types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generatepersonsegmentationrequest/qualitylevel-swift.enum)*