# ImageAestheticsScoresObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An observation that provides an overall score of aesthetic attributes for an image.

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
struct ImageAestheticsScoresObservation
```

## Topics

### Creating an observation
- [init(VNImageAestheticsScoresObservation)](./imageaestheticsscoresobservation/init%28_%29.md)
  Creates an image aesthetics scores observation.
### Inspecting an observation
- [enum RequestDescriptor](./requestdescriptor.md)
  A type that describes the request and revision combination.
- [let isUtility: Bool](./imageaestheticsscoresobservation/isutility.md)
  A Boolean value that represents images that are not necessarily of poor image quality, but may not have memorable or exciting content.
- [let overallScore: Float](./imageaestheticsscoresobservation/overallscore.md)
  A score which incorporates aesthetic score, failure score, and utility labels.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imageaestheticsscoresobservation)*