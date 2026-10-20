# outputPixelFormat

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) OSType outputPixelFormat;
```

#### Discussion

The property supports the following values:

- [`kCVPixelFormatType_OneComponent8`](../../CoreVideo/kcvpixelformattype_onecomponent8.md)
- [`kCVPixelFormatType_OneComponent16Half`](../../CoreVideo/kcvpixelformattype_onecomponent16half.md)
- [`kCVPixelFormatType_OneComponent32Float`](../../CoreVideo/kcvpixelformattype_onecomponent32float.md)

The default value is [`kCVPixelFormatType_OneComponent8`](../../CoreVideo/kcvpixelformattype_onecomponent8.md).

## See Also

### Configuring the Request
- [var qualityLevel: VNGeneratePersonSegmentationRequest.QualityLevel](./qualitylevel-swift.property.md)
  A value that indicates how the request balances accuracy and performance.
- [VNGeneratePersonSegmentationRequest.QualityLevel](./qualitylevel-swift.enum.md)
  Constants that define the levels of quality for a person segmentation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeneratepersonsegmentationrequest/outputpixelformat)*