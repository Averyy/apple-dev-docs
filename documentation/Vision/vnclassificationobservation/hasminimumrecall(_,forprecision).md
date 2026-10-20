# hasMinimumRecall(_:forPrecision:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Determines whether the observation for a specific precision has a minimum recall value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func hasMinimumRecall(_ minimumRecall: Float, forPrecision precision: Float) -> Bool
```

```objc
- (BOOL) hasMinimumRecall:(float) minimumRecall forPrecision:(float) precision;
```

#### Return Value

A Boolean indicating whether or not this classification observation provides a minimum percentage of relevant results that meet the desired precision criterion.

## Parameters

- `minimumRecall`: The minimum percentage of relevant results that the algorithm correctly classified.
- `precision`: The percentage of classification results that are relevant.

## See Also

### Measuring Confidence and Precision
- [var hasPrecisionRecallCurve: Bool](./hasprecisionrecallcurve.md)
  A Boolean variable indicating whether the observation contains precision and recall curves.
- [func hasMinimumPrecision(Float, forRecall: Float) -> Bool](./hasminimumprecision%28_,forrecall%29.md)
  Determines whether the observation for a specific recall has a minimum precision value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassificationobservation/hasminimumrecall(_:forprecision:))*