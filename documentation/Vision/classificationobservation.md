# ClassificationObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An object that represents classification information that an image-analysis request produces.

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
struct ClassificationObservation
```

## Topics

### Creating an observation
- [init(VNClassificationObservation)](./classificationobservation/init%28_%29.md)
  Creates a classification observation.
### Inspecting an observation
- [enum RequestDescriptor](./requestdescriptor.md)
  A type that describes the request and revision combination.
- [var hasPrecisionRecallCurve: Bool](./classificationobservation/hasprecisionrecallcurve.md)
  A Boolean value that indicates whether the observation contains precision and recall curves.
- [let identifier: String](./classificationobservation/identifier.md)
  The classification label that identifies the type of observation.
### Determining precision and recall
- [func hasMinimumPrecision(Float, forRecall: Float) -> Bool](./classificationobservation/hasminimumprecision%28_,forrecall%29.md)
  Determines whether the observation has a minimum precision value for a specific recall.
- [func hasMinimumRecall(Float, forPrecision: Float) -> Bool](./classificationobservation/hasminimumrecall%28_,forprecision%29.md)
  Determines whether the observation has a minimum recall value for a specific precision.

## Relationships

### Conforms To
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/classificationobservation)*