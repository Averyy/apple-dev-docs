# CIDynamicRangeOption

**Framework**: Core Image  
**Kind**: struct

An enum string type that your code can use to select different System Tone Mapping modes. These options are consistent with the analogous options available in Core Graphics, Core Animation, AppKit, UIKit, and SwiftUI, In Core Image, this option can be set on the `CISystemToneMap` filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct CIDynamicRangeOption
```

## Topics

### Enumeration Cases
- [static let standard: CIDynamicRangeOption](cidynamicrangeoption/standard.md)
  Standard dynamic range. Images with `contentHeadroom` metadata will be tone mapped to a maximum pixel value of 1.0.
- [static let constrainedHigh: CIDynamicRangeOption](cidynamicrangeoption/constrainedhigh.md)
  Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content. For best results, images should contain `contentAverageLightLevel` metadata.
- [static let high: CIDynamicRangeOption](cidynamicrangeoption/high.md)
  Use High dynamic range. Provides the best HDR quality. This needs to be reserved for situations where the user is focused on the media, such as larger views in an image editing/viewing app, or annotating/drawing with HDR colors
### Initializers
- [init(rawValue: String)](cidynamicrangeoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidynamicrangeoption)*