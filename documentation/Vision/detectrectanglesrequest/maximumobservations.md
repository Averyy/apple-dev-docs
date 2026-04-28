# maximumObservations

**Framework**: Vision  
**Kind**: property

The maximum number of rectangles the request returns.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var maximumObservations: Int
```

#### Discussion

The property’s default value is `1`. Setting this property to `0` will return a potentially unlimited number of observations.

## See Also

- [var maximumAspectRatio: Float](detectrectanglesrequest/maximumaspectratio.md)
  The largest aspect ratio the rectangle request detects.
- [var minimumAspectRatio: Float](detectrectanglesrequest/minimumaspectratio.md)
  The smallest aspect ratio the rectangle request detects.
- [var minimumConfidence: Float](detectrectanglesrequest/minimumconfidence.md)
  The minimum acceptable confidence level for detected rectangles.
- [var minimumSize: Float](detectrectanglesrequest/minimumsize.md)
  The minimum size of the rectangle detected as a proportion of the smallest dimension.
- [var quadratureToleranceDegrees: Float](detectrectanglesrequest/quadraturetolerancedegrees.md)
  The maximum number of degrees a rectangle corner angle deviates from 90°.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectrectanglesrequest/maximumobservations)*