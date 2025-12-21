# ImageAestheticsScoresObservation

**Framework**: Vision  
**Kind**: struct

An observation that provides an overall score of aesthetic attributes for an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct ImageAestheticsScoresObservation
```

## Topics

### Creating an observation
- [init(VNImageAestheticsScoresObservation)](imageaestheticsscoresobservation/init(_:).md)
  Creates an image aesthetics scores observation.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let isUtility: Bool](imageaestheticsscoresobservation/isutility.md)
  A Boolean value that represents images that are not necessarily of poor image quality, but may not have memorable or exciting content.
- [let overallScore: Float](imageaestheticsscoresobservation/overallscore.md)
  A score which incorporates aesthetic score, failure score, and utility labels.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imageaestheticsscoresobservation)*