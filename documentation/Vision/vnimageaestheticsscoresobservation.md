# VNImageAestheticsScoresObservation

**Framework**: Vision  
**Kind**: class

An object that represents the overall score of aesthetic attributes for an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class VNImageAestheticsScoresObservation
```

## Topics

### Parsing Observation Content
- [var overallScore: Float](vnimageaestheticsscoresobservation/overallscore.md)
  A score that incorporates the aesthetic score, failure score, and utility labels.
- [var isUtility: Bool](vnimageaestheticsscoresobservation/isutility.md)
  Returns a Boolean value that represents an image that may not have memorable or exciting content.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [var results: [VNImageAestheticsScoresObservation]?](vncalculateimageaestheticsscoresrequest/results.md)
  The results of the aesthetics request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageaestheticsscoresobservation)*