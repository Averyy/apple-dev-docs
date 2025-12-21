# VNAspectRatio

**Framework**: Vision  
**Kind**: typealias

A type alias for expressing rectangle aspect ratios in Vision.

## Declaration

```swift
typealias VNAspectRatio = Float
```

#### Discussion

The value is a [`float`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/StandardCSSProperties.html#//apple_ref/doc/uid/TP30001266-float), but limited to a range of `0.0` to `1.0`, inclusive, with the default of `0.5` indicating a square image. It defines aspect ratio as the shorter dimension over the longer dimension.

## See Also

- [var minimumAspectRatio: VNAspectRatio](vndetectrectanglesrequest/minimumaspectratio.md)
  A `float` specifying the minimum aspect ratio of the rectangle to detect, defined as the shorter dimension over the longer dimension.
- [var maximumAspectRatio: VNAspectRatio](vndetectrectanglesrequest/maximumaspectratio.md)
  A `float` specifying the maximum aspect ratio of the rectangle to detect, defined as the shorter dimension over the longer dimension.
- [var quadratureTolerance: VNDegrees](vndetectrectanglesrequest/quadraturetolerance.md)
  A float specifying the number of degrees a rectangle corner angle can deviate from 90°.
- [typealias VNDegrees](vndegrees.md)
  A typealias for expressing tolerance angles in Vision.
- [var minimumSize: Float](vndetectrectanglesrequest/minimumsize.md)
  The minimum size of a rectangle to detect, as a proportion of the smallest dimension.
- [var minimumConfidence: VNConfidence](vndetectrectanglesrequest/minimumconfidence.md)
  A value specifying the minimum acceptable confidence level.
- [typealias VNConfidence](vnconfidence.md)
  A type alias for the confidence value of an observation.
- [var maximumObservations: Int](vndetectrectanglesrequest/maximumobservations.md)
  An integer specifying the maximum number of rectangles Vision returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnaspectratio)*