# ClassificationObservation

**Framework**: Vision  
**Kind**: struct

An object that represents classification information that an image-analysis request produces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct ClassificationObservation
```

## Topics

### Creating an observation
- [init(VNClassificationObservation)](classificationobservation/init(_:).md)
  Creates a classification observation.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [var hasPrecisionRecallCurve: Bool](classificationobservation/hasprecisionrecallcurve.md)
  A Boolean value that indicates whether the observation contains precision and recall curves.
- [let identifier: String](classificationobservation/identifier.md)
  The classification label that identifies the type of observation.
### Determining precision and recall
- [func hasMinimumPrecision(Float, forRecall: Float) -> Bool](classificationobservation/hasminimumprecision(_:forrecall:).md)
  Determines whether the observation has a minimum precision value for a specific recall.
- [func hasMinimumRecall(Float, forPrecision: Float) -> Bool](classificationobservation/hasminimumrecall(_:forprecision:).md)
  Determines whether the observation has a minimum recall value for a specific precision.

## Relationships

### Conforms To
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/classificationobservation)*