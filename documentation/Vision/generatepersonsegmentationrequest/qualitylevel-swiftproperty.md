# qualityLevel

**Framework**: Vision  
**Kind**: property

A value that indicates how the request balances accuracy and performance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final var qualityLevel: GeneratePersonSegmentationRequest.QualityLevel { get set }
```

#### Discussion

The default is [`GeneratePersonSegmentationRequest.QualityLevel.accurate`](generatepersonsegmentationrequest/qualitylevel-swift.enum/accurate.md).

## See Also

- [GeneratePersonSegmentationRequest.QualityLevel](generatepersonsegmentationrequest/qualitylevel-swift.enum.md)
  Constants that define the levels of quality for a person-segmentation request.
- [var outputPixelFormatType: OSType](generatepersonsegmentationrequest/outputpixelformattype.md)
  The desired pixel format of the observation.
- [var supportedOutputPixelFormats: [OSType]](generatepersonsegmentationrequest/supportedoutputpixelformats.md)
  The collection of supported pixel format types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generatepersonsegmentationrequest/qualitylevel-swift.property)*