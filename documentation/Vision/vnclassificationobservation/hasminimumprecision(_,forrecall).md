# hasMinimumPrecision(_:forRecall:)

**Framework**: Vision  
**Kind**: method

Determines whether the observation for a specific recall has a minimum precision value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func hasMinimumPrecision(_ minimumPrecision: Float, forRecall recall: Float) -> Bool
```

#### Return Value

A Boolean indicating whether or not this classification observation provides a minimum percentage of relevant results that meet the desired recall criterion.

## Parameters

- `minimumPrecision`: The minimum percentage of classification results that are relevant.
- `recall`: The percentage of relevant results that the algorithm correctly classified.

## See Also

- [var hasPrecisionRecallCurve: Bool](vnclassificationobservation/hasprecisionrecallcurve.md)
  A Boolean variable indicating whether the observation contains precision and recall curves.
- [func hasMinimumRecall(Float, forPrecision: Float) -> Bool](vnclassificationobservation/hasminimumrecall(_:forprecision:).md)
  Determines whether the observation for a specific precision has a minimum recall value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassificationobservation/hasminimumprecision(_:forrecall:))*