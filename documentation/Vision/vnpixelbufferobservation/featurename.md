# featureName

**Framework**: Vision  
**Kind**: property

A feature name that the CoreML model defines.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var featureName: String? { get }
```

#### Discussion

This value is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if the observation isn’t the result of a [`VNCoreMLRequest`](vncoremlrequest.md) operation.

## See Also

- [var pixelBuffer: CVPixelBuffer](vnpixelbufferobservation/pixelbuffer.md)
  The image that results from a request with image output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpixelbufferobservation/featurename)*