# crop

**Framework**: Core Image  
**Kind**: property

A key used to specify whether to return a filter that crops the image to focus on detected features.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let crop: CIImageAutoAdjustmentOption
```

#### Discussion

The value associated with this key is a `CFBoolean` value. If `true`, the returned filters include an operation that crops the image around the features specified with the [`features`](ciimageautoadjustmentoption/features.md) option (or any features detected in the image, if that option is not present). Supply `false` to indicate not to return a crop filter. If you don’t specify this option, Core Image assumes its value is `false`.

## See Also

- [static let enhance: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/enhance.md)
  A key used to specify whether to return enhancement filters.
- [static let features: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/features.md)
  A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [static let level: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/level.md)
  A key used to specify whether to return a filter that rotates the image to keep a level perspective.
- [static let redEye: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/redeye.md)
  A key used to specify whether to return a red eye filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/crop)*