# HumanObservation

**Framework**: Vision  
**Kind**: struct

An object that represents a person that the request detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct HumanObservation
```

## Topics

### Creating an observation
- [init(VNHumanObservation)](humanobservation/init(_:).md)
  Creates a human observation.
- [init(boundingBox: NormalizedRect, revision: DetectHumanRectanglesRequest.Revision?)](humanobservation/init(boundingbox:revision:).md)
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let isUpperBodyOnly: Bool](humanobservation/isupperbodyonly.md)
  A Boolean value that indicates whether the observation represents an upper-body or full-body rectangle.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanobservation)*