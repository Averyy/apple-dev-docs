# GeneratePersonSegmentationRequest.QualityLevel

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

Constants that define the levels of quality for a person-segmentation request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
enum QualityLevel
```

## Topics

### Getting the quality levels
- [GeneratePersonSegmentationRequest.QualityLevel.accurate](./qualitylevel-swift.enum/accurate.md)
  A quality option that prefers image quality over performance.
- [GeneratePersonSegmentationRequest.QualityLevel.balanced](./qualitylevel-swift.enum/balanced.md)
  A quality option that prefers processing that balances image quality and performance.
- [GeneratePersonSegmentationRequest.QualityLevel.fast](./qualitylevel-swift.enum/fast.md)
  A quality option that prefers performance over image quality.

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

### Configuring a request
- [var qualityLevel: GeneratePersonSegmentationRequest.QualityLevel](./qualitylevel-swift.property.md)
  A value that indicates how the request balances accuracy and performance.
- [var outputPixelFormatType: OSType](./outputpixelformattype.md)
  The desired pixel format of the observation.
- [var supportedOutputPixelFormats: [OSType]](./supportedoutputpixelformats.md)
  The collection of supported pixel format types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generatepersonsegmentationrequest/qualitylevel-swift.enum)*