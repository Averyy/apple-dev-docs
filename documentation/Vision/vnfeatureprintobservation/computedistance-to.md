# computeDistance(_:to:)

**Framework**: Vision  
**Kind**: method

Computes the distance between two feature print observations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func computeDistance(_ outDistance: UnsafeMutablePointer<Float>, to featurePrint: VNFeaturePrintObservation) throws
```

#### Discussion

Shorter distances indicate greater similarity between feature prints.

## Parameters

- `outDistance`: A pointer to store the calculated distance value.
- `featurePrint`: The feature print object whose distance to calculate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfeatureprintobservation/computedistance(_:to:))*