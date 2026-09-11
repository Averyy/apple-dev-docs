# USDPlayer.TextureData

**Framework**: USDKit  
**Kind**: struct

Texture data from a texture asset referenced by a material prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/texturedata)*