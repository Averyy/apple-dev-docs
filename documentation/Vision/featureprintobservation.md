# FeaturePrintObservation

**Framework**: Vision  
**Kind**: struct

An observation that provides the recognized feature print.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct FeaturePrintObservation
```

## Topics

### Creating an observation
- [init(VNFeaturePrintObservation)](featureprintobservation/init(_:).md)
  Creates a feature print observation.
### Inspecting an observation
- [let data: Data](featureprintobservation/data.md)
  The feature print data.
- [let elementCount: Int](featureprintobservation/elementcount.md)
  The total number of elements in the data.
- [let elementType: ElementType](featureprintobservation/elementtype.md)
  The type of each element in the data.
- [enum ElementType](elementtype.md)
  The type of element in feature print data.
### Getting the distance
- [func distance(to: FeaturePrintObservation) throws -> Double](featureprintobservation/distance(to:).md)
  Computes the distance between two feature print observations.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/featureprintobservation)*