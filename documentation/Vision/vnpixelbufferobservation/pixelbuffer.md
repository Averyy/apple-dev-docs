# pixelBuffer

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The image that results from a request with image output.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var pixelBuffer: CVPixelBuffer { get }
```

```objc
@property (nonatomic, readonly) CVPixelBufferRef pixelBuffer;
```

#### Discussion

[`VNCoreMLRequest`](../vncoremlrequest.md) produces observations that contain images in pixel buffer format. The confidence level is always `1.0`.

## See Also

### Parsing Observation Content
- [var featureName: String?](./featurename.md)
  A feature name that the CoreML model defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpixelbufferobservation/pixelbuffer)*