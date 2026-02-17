# quadratureToleranceDegrees

**Framework**: Vision  
**Kind**: property

The maximum number of degrees a rectangle corner angle deviates from 90°.

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

The property’s value defaults to `30`, but you can set it to any value in the range `[0, 45]`.

## See Also

- [var maximumAspectRatio: Float](detectrectanglesrequest/maximumaspectratio.md)
  The largest aspect ratio the rectangle request detects.
- [var maximumObservations: Int](detectrectanglesrequest/maximumobservations.md)
  The maximum number of rectangles the request returns.
- [var minimumAspectRatio: Float](detectrectanglesrequest/minimumaspectratio.md)
  The smallest aspect ratio the rectangle request detects.
- [var minimumConfidence: Float](detectrectanglesrequest/minimumconfidence.md)
  The minimum acceptable confidence level for detected rectangles.
- [var minimumSize: Float](detectrectanglesrequest/minimumsize.md)
  The minimum size of the rectangle detected as a proportion of the smallest dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectrectanglesrequest/quadraturetolerancedegrees)*