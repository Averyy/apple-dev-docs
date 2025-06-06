# enhance

**Framework**: Core Image  
**Kind**: structdata

A key used to specify whether to return enhancement filters.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let enhance: CIImageAutoAdjustmentOption
```

#### Discussion

The value associated with this key is a `CFBoolean` value. Supply `false` to indicate not to return enhancement filters. If you don’t specify this option, Core Image assumes its value is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1437819-enhance)*