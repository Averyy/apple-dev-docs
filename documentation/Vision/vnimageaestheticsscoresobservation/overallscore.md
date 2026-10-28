# overallScore

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A score which incorporates aesthetic score, failure score, and utility labels.

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

```objc
@property (nonatomic, assign, readonly) float overallScore;
```

## Discussion

This returns a value within the range of `-1` and `1`, where `-1` is least desirable and `1` is most desirable.

## See Also

### Parsing Observation Content
- [var isUtility: Bool](./isutility.md)
  A Boolean value that represents images that are not necessarily of poor image quality, but may not have memorable or exciting content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageaestheticsscoresobservation/overallscore)*