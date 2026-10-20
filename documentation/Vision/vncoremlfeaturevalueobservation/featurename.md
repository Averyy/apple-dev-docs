# featureName

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The name used in the model description of the CoreML model that produced this observation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var featureName: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * featureName;
```

## See Also

### Obtaining Feature Values
- [var featureValue: MLFeatureValue](./featurevalue.md)
  The feature result of a [`VNCoreMLRequest`](../vncoremlrequest.md) that outputs neither a classification nor an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlfeaturevalueobservation/featurename)*