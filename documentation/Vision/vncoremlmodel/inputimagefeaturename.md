# inputImageFeatureName

**Framework**: Vision  
**Kind**: property

The name of the feature value that Vision sets from the request handler.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var inputImageFeatureName: String { get set }
```

#### Discussion

By default, Vision uses the first input found, but you can manually set that input to another [`featureName`](vncoremlfeaturevalueobservation/featurename.md) instead.

## See Also

- [var featureProvider: (any MLFeatureProvider)?](vncoremlmodel/featureprovider.md)
  An optional object to support inputs outside Vision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlmodel/inputimagefeaturename)*