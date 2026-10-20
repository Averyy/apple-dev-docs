# hasPrecisionRecallCurve

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign, readonly) BOOL hasPrecisionRecallCurve;
```

#### Discussion

Precision refers to the percentage of your classification results that are relevant, while recall refers to the percentage of total relevant results correctly classified.

If this property is [`true`](../../Swift/true.md), then you can call precision and recall-related methods in this observation. If this property is [`false`](../../Swift/false.md), then the  precision and recall-related methods won’t return meaningful data.

## See Also

### Measuring Confidence and Precision
- [func hasMinimumPrecision(Float, forRecall: Float) -> Bool](./hasminimumprecision%28_,forrecall%29.md)
  Determines whether the observation for a specific recall has a minimum precision value.
- [func hasMinimumRecall(Float, forPrecision: Float) -> Bool](./hasminimumrecall%28_,forprecision%29.md)
  Determines whether the observation for a specific precision has a minimum recall value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassificationobservation/hasprecisionrecallcurve)*