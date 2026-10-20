# USDPlayer.MeshData

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Mesh geometry data from a USD mesh prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct MeshData
```

## Topics

### Structures
- [USDPlayer.MeshData.Update](./meshdata/update.md)
  Delta update carrying only the mesh fields that changed since the last frame.
### Instance Properties
- [let assignedMaterials: [USDPlayer.MaterialID]](./meshdata/assignedmaterials.md)
  Material IDs bound to each mesh part, in order.
- [let descriptor: LowLevelMesh.Descriptor](./meshdata/descriptor.md)
  Low-level mesh descriptor.
- [let id: USDPlayer.MeshID](./meshdata/id.md)
  Unique identifier for this mesh resource.
- [let indexData: Data](./meshdata/indexdata.md)
  Index buffer data.
- [let instanceTransforms: [float4x4]](./meshdata/instancetransforms.md)
  World-space transforms for each mesh instance.
- [let meshType: USDPlayer.MeshData.MeshType](./meshdata/meshtype-swift.property.md)
  Whether the mesh is rigid or driven by a deformation resource.
- [let parts: [LowLevelMesh.Part]](./meshdata/parts.md)
  Low-level mesh parts.
- [let primPath: String](./meshdata/primpath.md)
  USD prim path this mesh corresponds to.
- [let vertexData: [Data]](./meshdata/vertexdata.md)
  Vertex buffer data.
### Enumerations
- [USDPlayer.MeshData.MeshType](./meshdata/meshtype-swift.enum.md)
  Distinguishes static and deformable mesh geometries.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/meshdata)*