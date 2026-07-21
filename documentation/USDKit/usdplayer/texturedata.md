# USDPlayer.TextureData

**Framework**: USDKit  
**Kind**: struct

Texture data from a texture asset referenced by a material prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TextureData
```

## Topics

### Instance Properties
- [let assetPath: String](usdplayer/texturedata/assetpath.md)
  Asset-relative path to the source texture file.
- [let data: Data](usdplayer/texturedata/data.md)
  Packed texture data.
- [let descriptor: LowLevelTexture.Descriptor](usdplayer/texturedata/descriptor.md)
  Texture dimensions, pixel format, and type.
- [let id: USDPlayer.TextureID](usdplayer/texturedata/id.md)
  Unique identifier for this texture resource.
- [let layout: [USDPlayer.TextureLevelInfo]](usdplayer/texturedata/layout.md)
  Per-mip-level byte-layout descriptors.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/texturedata)*