# hasPrecisionRecallCurve

**Framework**: Vision  
**Kind**: property

A Boolean variable indicating whether the observation contains precision and recall curves.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var hasPrecisionRecallCurve: Bool { get }
```

#### Discussion

Precision refers to the percentage of your classification results that are relevant, while recall refers to the percentage of total relevant results correctly classified.

If this property is [`true`](https://developer.apple.com/documentation/Swift/true), then you can call precision and recall-related methods in this observation. If this property is [`false`](https://developer.apple.com/documentation/Swift/false), then the  precision and recall-related methods won’t return meaningful data.

## See Also

- [func hasMinimumPrecision(Float, forRecall: Float) -> Bool](vnclassificationobservation/hasminimumprecision(_:forrecall:).md)
  Determines whether the observation for a specific recall has a minimum precision value.
- [func hasMinimumRecall(Float, forPrecision: Float) -> Bool](vnclassificationobservation/hasminimumrecall(_:forprecision:).md)
  Determines whether the observation for a specific precision has a minimum recall value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassificationobservation/hasprecisionrecallcurve)*