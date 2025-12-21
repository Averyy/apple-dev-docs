# minimumAspectRatio

**Framework**: Vision  
**Kind**: property

The smallest aspect ratio the rectangle request detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var minimumAspectRatio: Float
```

#### Discussion

The property’s value defaults to `0.5`, but you can set it to any value in the range `[0.0, 1.0]`. You can use this value to choose specific rectangles in the detection like filtering out narrow rectangles by excluding small aspect ratios, or setting a range of `0.95` to `1.0` to select mostly squares.

## See Also

- [var maximumAspectRatio: Float](detectrectanglesrequest/maximumaspectratio.md)
  The largest aspect ratio the rectangle request detects.
- [var maximumObservations: Int](detectrectanglesrequest/maximumobservations.md)
  The maximum number of rectangles Vision returns.
- [var minimumConfidence: Float](detectrectanglesrequest/minimumconfidence.md)
  The minimum acceptable confidence level for detected rectangles.
- [var minimumSize: Float](detectrectanglesrequest/minimumsize.md)
  The minimum size of the rectangle to be detected, as a proportion of the smallest dimension.
- [var quadratureToleranceDegrees: Float](detectrectanglesrequest/quadraturetolerancedegrees.md)
  The maximum number of degrees a rectangle corner angle can deviate from 90°.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectrectanglesrequest/minimumaspectratio)*