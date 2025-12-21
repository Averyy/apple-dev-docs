# minimumSize

**Framework**: Vision  
**Kind**: property

The minimum size of the rectangle to be detected, as a proportion of the smallest dimension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var minimumSize: Float
```

#### Discussion

The value should range from `0.0` to `1.0` inclusive. The default minimum size is `0.2`.

Any smaller rectangles that the framework might detect aren’t returned.

## See Also

- [var maximumAspectRatio: Float](detectrectanglesrequest/maximumaspectratio.md)
  The largest aspect ratio the rectangle request detects.
- [var maximumObservations: Int](detectrectanglesrequest/maximumobservations.md)
  The maximum number of rectangles Vision returns.
- [var minimumAspectRatio: Float](detectrectanglesrequest/minimumaspectratio.md)
  The smallest aspect ratio the rectangle request detects.
- [var minimumConfidence: Float](detectrectanglesrequest/minimumconfidence.md)
  The minimum acceptable confidence level for detected rectangles.
- [var quadratureToleranceDegrees: Float](detectrectanglesrequest/quadraturetolerancedegrees.md)
  The maximum number of degrees a rectangle corner angle can deviate from 90°.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectrectanglesrequest/minimumsize)*