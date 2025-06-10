# enhance

**Framework**: Core Image  
**Kind**: property

A key used to specify whether to return enhancement filters.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let enhance: CIImageAutoAdjustmentOption
```

#### Discussion

The value associated with this key is a `CFBoolean` value. Supply `false` to indicate not to return enhancement filters. If you don’t specify this option, Core Image assumes its value is `true`.

## See Also

- [static let crop: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/crop.md)
  A key used to specify whether to return a filter that crops the image to focus on detected features.
- [static let features: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/features.md)
  A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [static let level: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/level.md)
  A key used to specify whether to return a filter that rotates the image to keep a level perspective.
- [static let redEye: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/redeye.md)
  A key used to specify whether to return a red eye filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/enhance)*