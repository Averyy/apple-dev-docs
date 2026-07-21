# USDPlayer.MeshData

**Framework**: USDKit  
**Kind**: struct

Mesh geometry data from a USD mesh prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MeshData
```

## Topics

### Structures
- [USDPlayer.MeshData.Update](usdplayer/meshdata/update.md)
  Delta update carrying only the mesh fields that changed since the last frame.
### Instance Properties
- [let assignedMaterials: [USDPlayer.MaterialID]](usdplayer/meshdata/assignedmaterials.md)
  Material IDs bound to each mesh part, in order.
- [let descriptor: LowLevelMesh.Descriptor](usdplayer/meshdata/descriptor.md)
  Low-level mesh descriptor.
- [let id: USDPlayer.MeshID](usdplayer/meshdata/id.md)
  Unique identifier for this mesh resource.
- [let indexData: Data](usdplayer/meshdata/indexdata.md)
  Index buffer data.
- [let instanceTransforms: [float4x4]](usdplayer/meshdata/instancetransforms.md)
  World-space transforms for each mesh instance.
- [let meshType: USDPlayer.MeshData.MeshType](usdplayer/meshdata/meshtype-swift.property.md)
  Whether the mesh is rigid or driven by a deformation resource.
- [let parts: [LowLevelMesh.Part]](usdplayer/meshdata/parts.md)
  Low-level mesh parts.
- [let primPath: String](usdplayer/meshdata/primpath.md)
  USD prim path this mesh corresponds to.
- [let vertexData: [Data]](usdplayer/meshdata/vertexdata.md)
  Vertex buffer data.
### Enumerations
- [USDPlayer.MeshData.MeshType](usdplayer/meshdata/meshtype-swift.enum.md)
  Distinguishes static and deformable mesh geometries.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/meshdata)*