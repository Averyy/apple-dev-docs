# USDPlayer.MeshData.Update

**Framework**: USDKit  
**Kind**: struct

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
- [let assignedMaterials: [USDPlayer.MaterialID]?](usdplayer/meshdata/update/assignedmaterials.md)
  Updated material bindings.
- [let id: USDPlayer.MeshID](usdplayer/meshdata/update/id.md)
  Unique identifier for the mesh being updated.
- [let indexData: Data?](usdplayer/meshdata/update/indexdata.md)
  Updated index buffer data.
- [let instanceTransforms: [float4x4]?](usdplayer/meshdata/update/instancetransforms.md)
  Updated world-space instance transforms.
- [let meshType: USDPlayer.MeshData.MeshType?](usdplayer/meshdata/update/meshtype.md)
  Updated mesh type.
- [let parts: [LowLevelMesh.Part]?](usdplayer/meshdata/update/parts.md)
  Updated mesh parts.
- [let vertexData: [Data]?](usdplayer/meshdata/update/vertexdata.md)
  Updated vertex buffer data.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/meshdata/update)*