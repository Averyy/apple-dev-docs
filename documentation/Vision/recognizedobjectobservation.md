# RecognizedObjectObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An observation with an array of classification labels that classify the recognized object.

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
struct RecognizedObjectObservation
```

#### Overview

The confidence of the classifications sum up to `1.0`. Multiply the classification confidence with the confidence of this observation.

## Topics

### Creating an observation
- [init(VNRecognizedObjectObservation)](./recognizedobjectobservation/init%28_%29.md)
  Creates a recognized object observation.
### Inspecting an observation
- [enum RequestDescriptor](./requestdescriptor.md)
  A type that describes the request and revision combination.
- [let labels: [ClassificationObservation]](./recognizedobjectobservation/labels.md)
  The classification of the recognized object.
- [struct ClassificationObservation](./classificationobservation.md)
  An object that represents classification information that an image-analysis request produces.

## Relationships

### Conforms To
- [BoundingBoxProviding](./boundingboxproviding.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionObservation](./visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedobjectobservation)*