# VNImageAestheticsScoresObservation

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNImageAestheticsScoresObservation : VNObservation
```

## Topics

### Parsing Observation Content
- [var overallScore: Float](./vnimageaestheticsscoresobservation/overallscore.md)
  A score which incorporates aesthetic score, failure score, and utility labels.
- [var isUtility: Bool](./vnimageaestheticsscoresobservation/isutility.md)
  A Boolean value that represents images that are not necessarily of poor image quality, but may not have memorable or exciting content.

## Relationships

### Inherits From
- [VNObservation](./vnobservation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [VNRequestRevisionProviding](./vnrequestrevisionproviding.md)

## See Also

### Accessing the results
- [var results: [VNImageAestheticsScoresObservation]?](./vncalculateimageaestheticsscoresrequest/results.md)
  The results of the aesthetics request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageaestheticsscoresobservation)*