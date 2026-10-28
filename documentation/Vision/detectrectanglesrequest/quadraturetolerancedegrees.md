# quadratureToleranceDegrees

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The maximum number of degrees a rectangle corner angle deviates from 90°.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
var quadratureToleranceDegrees: Float
```

## Discussion

The property’s value defaults to `30`, but you can set it to any value in the range `[0, 45]`.

## See Also

### Configuring a request
- [var maximumAspectRatio: Float](./maximumaspectratio.md)
  The largest aspect ratio the rectangle request detects.
- [var maximumObservations: Int](./maximumobservations.md)
  The maximum number of rectangles the request returns.
- [var minimumAspectRatio: Float](./minimumaspectratio.md)
  The smallest aspect ratio the rectangle request detects.
- [var minimumConfidence: Float](./minimumconfidence.md)
  The minimum acceptable confidence level for detected rectangles.
- [var minimumSize: Float](./minimumsize.md)
  The minimum size of the rectangle detected as a proportion of the smallest dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectrectanglesrequest/quadraturetolerancedegrees)*