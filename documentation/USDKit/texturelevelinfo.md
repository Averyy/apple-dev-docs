# TextureLevelInfo

**Framework**: USDKit  
**Kind**: struct

The byte layout of a single mip level within a texture’s pixel data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TextureLevelInfo
```

## Topics

### Instance Properties
- [let byteCountPerImage: Int](texturelevelinfo/bytecountperimage.md)
- [let byteCountPerRow: Int](texturelevelinfo/bytecountperrow.md)
- [let dataOffset: Int](texturelevelinfo/dataoffset.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MeshData](meshdata.md)
  The geometry of a mesh extracted from a USD stage for rendering in RealityKit.
- [struct MaterialData](materialdata.md)
  A material, including its shader graph and assigned textures, extracted from a USD stage for rendering.
- [struct TextureData](texturedata.md)
  A texture, including its pixel data and layout, extracted from a USD stage for rendering.
- [struct DeformationData](deformationdata.md)
  The blend-shape, skinning, and renormalization data that animates a mesh extracted from a USD stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/texturelevelinfo)*