# level

**Framework**: Core Image  
**Kind**: property

A key used to specify whether to return a filter that rotates the image to keep a level perspective.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let level: CIImageAutoAdjustmentOption
```

#### Discussion

The value associated with this key is a `CFBoolean` value. If `true`, Core Image analyzes the image to determine whether it would benefit from rotation—for example, a landscape photo in which the horizon is not horizontal—and returns a filter to perform that rotation. Supply `false` to indicate not to return a rotation filter. If you don’t specify this option, Core Image assumes its value is `false`.

## See Also

- [static let crop: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/crop.md)
  A key used to specify whether to return a filter that crops the image to focus on detected features.
- [static let enhance: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/enhance.md)
  A key used to specify whether to return enhancement filters.
- [static let features: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/features.md)
  A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [static let redEye: CIImageAutoAdjustmentOption](ciimageautoadjustmentoption/redeye.md)
  A key used to specify whether to return a red eye filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/level)*