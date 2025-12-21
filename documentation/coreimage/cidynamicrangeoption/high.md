# high

**Framework**: Core Image  
**Kind**: property

Use High dynamic range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let high: CIDynamicRangeOption
```

#### Discussion

The provides the best HDR quality and needs to be reserved for situations where the user is focused on the media, such as larger views in an image editing/viewing app, or annotating/drawing with HDR colors

## See Also

- [static let standard: CIDynamicRangeOption](cidynamicrangeoption/standard.md)
  Use Standard dynamic range.
- [static let constrainedHigh: CIDynamicRangeOption](cidynamicrangeoption/constrainedhigh.md)
  Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidynamicrangeoption/high)*