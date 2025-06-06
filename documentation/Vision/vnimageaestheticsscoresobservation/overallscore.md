# overallScore

**Framework**: Vision  
**Kind**: property

A score that incorporates the aesthetic score, failure score, and utility labels.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var overallScore: Float { get }
```

#### Discussion

This returns a value within the range of `-1` and `1`, where `1` is most desirable and `-1` isn’t desireable.

## See Also

- [var isUtility: Bool](vnimageaestheticsscoresobservation/isutility.md)
  Returns a Boolean value that represents an image that may not have memorable or exciting content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageaestheticsscoresobservation/overallscore)*