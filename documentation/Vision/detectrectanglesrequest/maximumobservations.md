# maximumObservations

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The maximum number of rectangles the request returns.

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
var maximumObservations: Int
```

## Discussion

The property’s default value is `1`. Setting this property to `0` will return a potentially unlimited number of observations.

## See Also

### Configuring a request
- [var maximumAspectRatio: Float](./maximumaspectratio.md)
  The largest aspect ratio the rectangle request detects.
- [var minimumAspectRatio: Float](./minimumaspectratio.md)
  The smallest aspect ratio the rectangle request detects.
- [var minimumConfidence: Float](./minimumconfidence.md)
  The minimum acceptable confidence level for detected rectangles.
- [var minimumSize: Float](./minimumsize.md)
  The minimum size of the rectangle detected as a proportion of the smallest dimension.
- [var quadratureToleranceDegrees: Float](./quadraturetolerancedegrees.md)
  The maximum number of degrees a rectangle corner angle deviates from 90°.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectrectanglesrequest/maximumobservations)*