# USDPlayer.MeshData.Update

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Delta update carrying only the mesh fields that changed since the last frame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Update
```

## Topics

### Instance Properties
- [let assignedMaterials: [USDPlayer.MaterialID]?](./update/assignedmaterials.md)
  Updated material bindings.
- [let id: USDPlayer.MeshID](./update/id.md)
  Unique identifier for the mesh being updated.
- [let indexData: Data?](./update/indexdata.md)
  Updated index buffer data.
- [let instanceTransforms: [float4x4]?](./update/instancetransforms.md)
  Updated world-space instance transforms.
- [let meshType: USDPlayer.MeshData.MeshType?](./update/meshtype.md)
  Updated mesh type.
- [let parts: [LowLevelMesh.Part]?](./update/parts.md)
  Updated mesh parts.
- [let vertexData: [Data]?](./update/vertexdata.md)
  Updated vertex buffer data.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/meshdata/update)*