# VNCalculateImageAestheticsScoresRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

An object that analyzes an image for aesthetically pleasing attributes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class VNCalculateImageAestheticsScoresRequest
```

```objc
@interface VNCalculateImageAestheticsScoresRequest : VNImageBasedRequest
```

## Topics

### Accessing the results
- [var results: [VNImageAestheticsScoresObservation]?](./vncalculateimageaestheticsscoresrequest/results.md)
  The results of the aesthetics request.
- [class VNImageAestheticsScoresObservation](./vnimageaestheticsscoresobservation.md)
  An object that represents the overall score of aesthetic attributes for an image.

## Relationships

### Inherits From
- [VNImageBasedRequest](./vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncalculateimageaestheticsscoresrequest)*