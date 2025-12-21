# RecognizedObjectObservation

**Framework**: Vision  
**Kind**: struct

An observation with an array of classification labels that classify the recognized object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct RecognizedObjectObservation
```

#### Overview

The confidence of the classifications sum up to `1.0`. Multiply the classification confidence with the confidence of this observation.

## Topics

### Creating an observation
- [init(VNRecognizedObjectObservation)](recognizedobjectobservation/init(_:).md)
  Creates a recognized object observation.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let labels: [ClassificationObservation]](recognizedobjectobservation/labels.md)
  The classification of the recognized object.
- [struct ClassificationObservation](classificationobservation.md)
  An object that represents classification information that an image-analysis request produces.

## Relationships

### Conforms To
- [BoundingBoxProviding](boundingboxproviding.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedobjectobservation)*