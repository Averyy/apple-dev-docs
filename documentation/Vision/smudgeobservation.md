# SmudgeObservation

**Framework**: Vision  
**Kind**: struct

An observation that provides an overall score of the presence of a smudge in an image or video frame capture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct SmudgeObservation
```

## Topics

### Inspecting an observation
- [var description: String](smudgeobservation/description.md)
  A textual representation of this instance.
- [let confidence: Float](smudgeobservation/confidence.md)
  The level of confidence in the observation’s accuracy of smudge detection on a lens.
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/smudgeobservation)*