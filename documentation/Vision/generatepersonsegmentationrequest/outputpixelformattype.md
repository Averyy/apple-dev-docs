# outputPixelFormatType

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The desired pixel format of the observation.

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
final var outputPixelFormatType: OSType { get set }
```

## Discussion

The default value is [`kCVPixelFormatType_OneComponent8`](../../CoreVideo/kcvpixelformattype_onecomponent8.md).

## See Also

### Configuring a request
- [var qualityLevel: GeneratePersonSegmentationRequest.QualityLevel](./qualitylevel-swift.property.md)
  A value that indicates how the request balances accuracy and performance.
- [GeneratePersonSegmentationRequest.QualityLevel](./qualitylevel-swift.enum.md)
  Constants that define the levels of quality for a person-segmentation request.
- [var supportedOutputPixelFormats: [OSType]](./supportedoutputpixelformats.md)
  The collection of supported pixel format types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generatepersonsegmentationrequest/outputpixelformattype)*