# hasMinimumPrecision(_:forRecall:)

**Framework**: Vision  
**Kind**: method

Determines whether the observation has a minimum precision value for a specific recall.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func hasMinimumPrecision(_ minimumPrecision: Float, forRecall recall: Float) -> Bool
```

#### Return Value

A Boolean value that indicates whether the classification observation provides a minimum percentage of correct results that meet the desired recall.

#### Discussion

The following example uses the `hasMinimumPrecision(_:forRecall)` method to perform a high-recall filter on the results of a `ClassifyImageRequest`:

```swift
let results = try await request.perform(on: image)
    .filter { $0.hasMinimumPrecision(0.1, forRecall: 0.8) }
```

A high-recall filter retains a much broader range of observations, but can result in more false positive results. Testing can help determine the balance point between the `minimumPrecision` and `recall` values to return the best results for a specific use case.

## Parameters

- `minimumPrecision`: The minimum desired percentage of correct positive classifications.
- `recall`: The percentage of all positive classifications that the algorithm correctly classified.

## See Also

- [func hasMinimumRecall(Float, forPrecision: Float) -> Bool](classificationobservation/hasminimumrecall(_:forprecision:).md)
  Determines whether the observation has a minimum recall value for a specific precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/classificationobservation/hasminimumprecision(_:forrecall:))*