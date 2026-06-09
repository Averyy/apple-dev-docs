# DeformationData

**Framework**: USDKit  
**Kind**: struct

The blend-shape, skinning, and renormalization data that animates a mesh extracted from a USD stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DeformationData
```

## Topics

### Identifying the deformation
- [let id: DeformationID](deformationdata/id.md)
### Accessing deformation data
- [let blendShapeData: DeformationData.BlendShapeData?](deformationdata/blendshapedata-swift.property.md)
- [let skinningData: DeformationData.SkinningData?](deformationdata/skinningdata-swift.property.md)
- [let renormalizationData: DeformationData.RenormalizationData?](deformationdata/renormalizationdata-swift.property.md)
- [DeformationData.BlendShapeData](deformationdata/blendshapedata-swift.struct.md)
- [DeformationData.SkinningData](deformationdata/skinningdata-swift.struct.md)
- [DeformationData.RenormalizationData](deformationdata/renormalizationdata-swift.struct.md)
### Updating the deformation
- [DeformationData.Update](deformationdata/update.md)

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
- [struct TextureLevelInfo](texturelevelinfo.md)
  The byte layout of a single mip level within a texture’s pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/deformationdata)*