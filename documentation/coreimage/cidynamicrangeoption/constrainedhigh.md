# constrainedHigh

**Framework**: Core Image  
**Kind**: property

Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content. For best results, images should contain `contentAverageLightLevel` metadata.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static let constrainedHigh: CIDynamicRangeOption
```

## See Also

- [static let standard: CIDynamicRangeOption](cidynamicrangeoption/standard.md)
  Standard dynamic range. Images with `contentHeadroom` metadata will be tone mapped to a maximum pixel value of 1.0.
- [static let high: CIDynamicRangeOption](cidynamicrangeoption/high.md)
  Use High dynamic range. Provides the best HDR quality. This needs to be reserved for situations where the user is focused on the media, such as larger views in an image editing/viewing app, or annotating/drawing with HDR colors


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidynamicrangeoption/constrainedhigh)*