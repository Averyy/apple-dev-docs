# quadratureToleranceDegrees

**Framework**: Vision  
**Kind**: property

The maximum number of degrees a rectangle corner angle can deviate from 90°.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var quadratureToleranceDegrees: Float
```

#### Discussion

The tolerance value should range from 0 to 45, inclusive. The default tolerance is 30.

## See Also

- [var maximumAspectRatio: Float](detectrectanglesrequest/maximumaspectratio.md)
  The largest aspect ratio the rectangle request detects.
- [var maximumObservations: Int](detectrectanglesrequest/maximumobservations.md)
  The maximum number of rectangles Vision returns.
- [var minimumAspectRatio: Float](detectrectanglesrequest/minimumaspectratio.md)
  The smallest aspect ratio the rectangle request detects.
- [var minimumConfidence: Float](detectrectanglesrequest/minimumconfidence.md)
  The minimum acceptable confidence level for detected rectangles.
- [var minimumSize: Float](detectrectanglesrequest/minimumsize.md)
  The minimum size of the rectangle to be detected, as a proportion of the smallest dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectrectanglesrequest/quadraturetolerancedegrees)*