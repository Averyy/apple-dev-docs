# overallScore

**Framework**: Vision  
**Kind**: property

A score which incorporates aesthetic score, failure score and utility labels.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let overallScore: Float
```

#### Discussion

`overallScore` is within the range [-1, 1] where 1 is most desirable and -1 is not desirable.

## See Also

- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let isUtility: Bool](imageaestheticsscoresobservation/isutility.md)
  A Boolean value that represents images that aren’t necessarily of poor image quality but may not have memorable or exciting content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imageaestheticsscoresobservation/overallscore)*