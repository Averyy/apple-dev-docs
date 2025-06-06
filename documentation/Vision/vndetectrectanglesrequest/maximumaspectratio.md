# maximumAspectRatio

**Framework**: Vision  
**Kind**: property

A `float` specifying the maximum aspect ratio of the rectangle to detect, defined as the shorter dimension over the longer dimension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var maximumAspectRatio: VNAspectRatio { get set }
```

#### Discussion

The value should range from `0.0` to `1.0`, inclusive. The default value is `0.5`.

## See Also

- [var minimumAspectRatio: VNAspectRatio](vndetectrectanglesrequest/minimumaspectratio.md)
  A `float` specifying the minimum aspect ratio of the rectangle to detect, defined as the shorter dimension over the longer dimension.
- [typealias VNAspectRatio](vnaspectratio.md)
  A type alias for expressing rectangle aspect ratios in Vision.
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectrectanglesrequest/maximumaspectratio)*