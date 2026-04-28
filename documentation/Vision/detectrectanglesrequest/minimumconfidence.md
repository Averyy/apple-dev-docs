# minimumConfidence

**Framework**: Vision  
**Kind**: property

The minimum acceptable confidence level for detected rectangles.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var minimumConfidence: Float
```

#### Discussion

Vision won’t return rectangles with a confidence score lower than the specified minimum. The property’s default value is `0.0`, but you can set it to any value in the range `[0.0, 1.0]`. A value of `0.0` represents no confidence, while `1.0` represents full confidence.

## See Also

- [var maximumAspectRatio: Float](detectrectanglesrequest/maximumaspectratio.md)
  The largest aspect ratio the rectangle request detects.
- [var maximumObservations: Int](detectrectanglesrequest/maximumobservations.md)
  The maximum number of rectangles the request returns.
- [var minimumAspectRatio: Float](detectrectanglesrequest/minimumaspectratio.md)
  The smallest aspect ratio the rectangle request detects.
- [var minimumSize: Float](detectrectanglesrequest/minimumsize.md)
  The minimum size of the rectangle detected as a proportion of the smallest dimension.
- [var quadratureToleranceDegrees: Float](detectrectanglesrequest/quadraturetolerancedegrees.md)
  The maximum number of degrees a rectangle corner angle deviates from 90°.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectrectanglesrequest/minimumconfidence)*