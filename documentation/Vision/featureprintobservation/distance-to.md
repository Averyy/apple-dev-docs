# distance(to:)

**Framework**: Vision  
**Kind**: method

Computes the distance between two feature print observations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func distance(to featurePrint: FeaturePrintObservation) throws -> Double
```

#### Return Value

The distance between two observations. Shorter distances indicate greater similarity between feature prints.

## Parameters

- `featurePrint`: The feature print object to calculate the distance to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/featureprintobservation/distance(to:))*