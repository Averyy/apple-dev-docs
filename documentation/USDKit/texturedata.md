# TextureData

**Framework**: USDKit  
**Kind**: struct

A texture, including its pixel data and layout, extracted from a USD stage for rendering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TextureData
```

## Topics

### Identifying the texture
- [let id: TextureID](texturedata/id.md)
- [let assetPath: String](texturedata/assetpath.md)
### Accessing texture content
- [let data: Data](texturedata/data.md)
- [let descriptor: LowLevelTexture.Descriptor](texturedata/descriptor.md)
- [let layout: [TextureLevelInfo]](texturedata/layout.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MeshData](meshdata.md)
  The geometry of a mesh extracted from a USD stage for rendering in RealityKit.
- [struct MaterialData](materialdata.md)
  A material, including its shader graph and assigned textures, extracted from a USD stage for rendering.
- [struct TextureLevelInfo](texturelevelinfo.md)
  The byte layout of a single mip level within a texture’s pixel data.
- [struct DeformationData](deformationdata.md)
  The blend-shape, skinning, and renormalization data that animates a mesh extracted from a USD stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/texturedata)*