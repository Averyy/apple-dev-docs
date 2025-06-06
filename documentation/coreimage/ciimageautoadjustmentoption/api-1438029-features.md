# features

**Framework**: Core Image  
**Kind**: structdata

A key used to specify an array of features that you want to apply enhancement and red eye filters to.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let features: CIImageAutoAdjustmentOption
```

#### Discussion

The associated value is an array of `CIFeature` objects. If you don’t supply an array, the Core Image searches for features using the `CIDetector` class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1438029-features)*