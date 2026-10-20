# HumanObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An object that represents a person that the request detects.

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
struct HumanObservation
```

## Topics

### Creating an observation
- [init(VNHumanObservation)](./humanobservation/init%28_%29.md)
  Creates a human observation.
- [init(boundingBox: NormalizedRect, revision: DetectHumanRectanglesRequest.Revision?)](./humanobservation/init%28boundingbox,revision%29.md)
### Inspecting an observation
- [enum RequestDescriptor](./requestdescriptor.md)
  A type that describes the request and revision combination.
- [let isUpperBodyOnly: Bool](./humanobservation/isupperbodyonly.md)
  A Boolean value that indicates whether the observation represents an upper-body or full-body rectangle.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanobservation)*