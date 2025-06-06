# hasMinimumRecall(_:forPrecision:)

**Framework**: Vision  
**Kind**: method

Determines whether the observation has a minimum recall value for a specific precision.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func hasMinimumRecall(_ minimumRecall: Float, forPrecision precision: Float) -> Bool
```

#### Return Value

A Boolean value that indicates whether the classification observation achieves a minimum recall value for a specific precision.

#### Discussion

The following example uses the `hasMinimumRecall(_:forPrecision)` method to perform a high-precision filter on the results of a `ClassifyImageRequest`.

```swift
let results = try await request.perform(on: image)
    .filter { $0.hasMinimumRecall(0.01, forPrecision: 0.9) }
```

A high-precision filter retains a smaller number of observations, with less chance to contain false positives. Testing can help determine the balance point between the `minimumRecall` and `precision` values to return the best results for a specific use case.

## Parameters

- `minimumRecall`: The minimum desired percentage of all positive classifications that the algorithm correctly classifies.
- `precision`: The percentage of correct positive classifications.

## See Also

- [func hasMinimumPrecision(Float, forRecall: Float) -> Bool](classificationobservation/hasminimumprecision(_:forrecall:).md)
  Determines whether the observation has a minimum precision value for a specific recall.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/classificationobservation/hasminimumrecall(_:forprecision:))*