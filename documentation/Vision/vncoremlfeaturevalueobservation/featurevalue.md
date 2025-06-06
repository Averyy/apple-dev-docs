# featureValue

**Framework**: Vision  
**Kind**: property

The feature result of a [`VNCoreMLRequest`](vncoremlrequest.md) that outputs neither a classification nor an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var featureValue: MLFeatureValue { get }
```

#### Discussion

Refer to [`Core ML`](https://developer.apple.com/documentation/CoreML) documentation and the model itself to learn about proper handling of the content.

## See Also

- [var featureName: String](vncoremlfeaturevalueobservation/featurename.md)
  The name used in the model description of the CoreML model that produced this observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlfeaturevalueobservation/featurevalue)*