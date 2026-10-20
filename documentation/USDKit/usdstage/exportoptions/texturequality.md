# USDStage.ExportOptions.TextureQuality

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A texture quality level.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct TextureQuality
```

## Topics

### Type Properties
- [static var low: USDStage.ExportOptions.TextureQuality](./texturequality/low.md)
  Aggressively reduces the texture file size. Some visual details may be suppressed to reach the smallest file size.
- [static var medium: USDStage.ExportOptions.TextureQuality](./texturequality/medium.md)
  Further reduces the texture file size. Fine details may not be preserved to reach a small file size.
- [static var standard: USDStage.ExportOptions.TextureQuality](./texturequality/standard.md)
  Reduces the texture file size while preserving most details.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/exportoptions/texturequality)*