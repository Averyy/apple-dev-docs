# MeshData

**Framework**: USDKit  
**Kind**: struct

The geometry of a mesh extracted from a USD stage for rendering in RealityKit.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MeshData
```

## Topics

### Identifying the mesh
- [let id: MeshID](meshdata/id.md)
- [let primPath: String](meshdata/primpath.md)
### Accessing geometry
- [let vertexData: [Data]](meshdata/vertexdata.md)
- [let indexData: Data](meshdata/indexdata.md)
- [let descriptor: LowLevelMesh.Descriptor](meshdata/descriptor.md)
- [let parts: [LowLevelMesh.Part]](meshdata/parts.md)
- [let instanceTransforms: [float4x4]](meshdata/instancetransforms.md)
- [let meshType: MeshData.MeshType](meshdata/meshtype-swift.property.md)
- [MeshData.MeshType](meshdata/meshtype-swift.enum.md)
### Assigning materials
- [let assignedMaterials: [MaterialID]](meshdata/assignedmaterials.md)
### Updating the mesh
- [MeshData.Update](meshdata/update.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MaterialData](materialdata.md)
  A material, including its shader graph and assigned textures, extracted from a USD stage for rendering.
- [struct TextureData](texturedata.md)
  A texture, including its pixel data and layout, extracted from a USD stage for rendering.
- [struct TextureLevelInfo](texturelevelinfo.md)
  The byte layout of a single mip level within a texture’s pixel data.
- [struct DeformationData](deformationdata.md)
  The blend-shape, skinning, and renormalization data that animates a mesh extracted from a USD stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/meshdata)*