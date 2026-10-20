# quadratureTolerance

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A float specifying the number of degrees a rectangle corner angle can deviate from 90°.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var quadratureTolerance: VNDegrees { get set }
```

```objc
@property (nonatomic, assign, readwrite) VNDegrees quadratureTolerance;
```

#### Discussion

The tolerance value should range from `0` to `45`, inclusive. The default tolerance is `30`.

## See Also

### Configuring Detection
- [var minimumAspectRatio: VNAspectRatio](./minimumaspectratio.md)
  A `float` specifying the minimum aspect ratio of the rectangle to detect, defined as the shorter dimension over the longer dimension.
- [var maximumAspectRatio: VNAspectRatio](./maximumaspectratio.md)
  A `float` specifying the maximum aspect ratio of the rectangle to detect, defined as the shorter dimension over the longer dimension.
- [typealias VNAspectRatio](../vnaspectratio.md)
  A type alias for expressing rectangle aspect ratios in Vision.
- [typealias VNDegrees](../vndegrees.md)
  A typealias for expressing tolerance angles in Vision.
- [var minimumSize: Float](./minimumsize.md)
  The minimum size of a rectangle to detect, as a proportion of the smallest dimension.
- [var minimumConfidence: VNConfidence](./minimumconfidence.md)
  A value specifying the minimum acceptable confidence level.
- [typealias VNConfidence](../vnconfidence.md)
  A type alias for the confidence value of an observation.
- [var maximumObservations: Int](./maximumobservations.md)
  An integer specifying the maximum number of rectangles Vision returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectrectanglesrequest/quadraturetolerance)*