# USDPlayer.FrameUpdate

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A snapshot of all mesh, material, texture, and deformation changes from the last update.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct FrameUpdate
```

## Topics

### Instance Properties
- [let deformationAdditions: [USDPlayer.DeformationID]](./frameupdate/deformationadditions.md)
  IDs of newly added deformation resources.
- [let deformationRemovals: [USDPlayer.DeformationID]](./frameupdate/deformationremovals.md)
  IDs of deformation resources removed this frame.
- [let deformationUpdates: [USDPlayer.DeformationID]](./frameupdate/deformationupdates.md)
  IDs of deformation resources with delta changes this frame.
- [let errors: [USDRenderError]](./frameupdate/errors.md)
  Errors encountered during this update.
- [let materialAdditions: [USDPlayer.MaterialID]](./frameupdate/materialadditions.md)
  IDs of newly added materials.
- [let materialRemovals: [USDPlayer.MaterialID]](./frameupdate/materialremovals.md)
  IDs of materials removed this frame.
- [let materialUpdates: [USDPlayer.MaterialID]](./frameupdate/materialupdates.md)
  IDs of materials with delta changes this frame.
- [let meshAdditions: [USDPlayer.MeshID]](./frameupdate/meshadditions.md)
  IDs of newly added meshes.
- [let meshRemovals: [USDPlayer.MeshID]](./frameupdate/meshremovals.md)
  IDs of meshes removed this frame.
- [let meshUpdates: [USDPlayer.MeshID]](./frameupdate/meshupdates.md)
  IDs of meshes with delta changes this frame.
- [let textureAdditions: [USDPlayer.TextureID]](./frameupdate/textureadditions.md)
  IDs of newly added texture assets.
- [let textureRemovals: [USDPlayer.TextureID]](./frameupdate/textureremovals.md)
  IDs of texture assets removed this frame.
- [let timeCode: USDStage.TimeCode](./frameupdate/timecode.md)
  The USD time code this update corresponds to.
### Instance Methods
- [func takeDeformationAddition(id: USDPlayer.DeformationID) -> USDPlayer.DeformationData?](./frameupdate/takedeformationaddition%28id%29.md)
  Consumes and returns the [`USDPlayer.DeformationData`](./deformationdata.md) for the given deformation addition.
- [func takeDeformationUpdate(id: USDPlayer.DeformationID) -> USDPlayer.DeformationData.Update?](./frameupdate/takedeformationupdate%28id%29.md)
  Consumes and returns the [`USDPlayer.DeformationData.Update`](./deformationdata/update.md) for the given deformation delta update.
- [func takeMaterialAddition(id: USDPlayer.MaterialID) -> USDPlayer.MaterialData?](./frameupdate/takematerialaddition%28id%29.md)
  Consumes and returns the [`USDPlayer.MaterialData`](./materialdata.md) for the given material addition.
- [func takeMaterialUpdate(id: USDPlayer.MaterialID) -> USDPlayer.MaterialData.Update?](./frameupdate/takematerialupdate%28id%29.md)
  Consumes and returns the [`USDPlayer.MaterialData.Update`](./materialdata/update.md) for the given material delta update.
- [func takeMeshAddition(id: USDPlayer.MeshID) -> USDPlayer.MeshData?](./frameupdate/takemeshaddition%28id%29.md)
  Consumes and returns the [`USDPlayer.MeshData`](./meshdata.md) for the given mesh addition.
- [func takeMeshUpdate(id: USDPlayer.MeshID) -> USDPlayer.MeshData.Update?](./frameupdate/takemeshupdate%28id%29.md)
  Consumes and returns the [`USDPlayer.MeshData.Update`](./meshdata/update.md) for the given mesh delta update.
- [func takeTextureAddition(id: USDPlayer.TextureID) -> USDPlayer.TextureData?](./frameupdate/taketextureaddition%28id%29.md)
  Consumes and returns the [`USDPlayer.TextureData`](./texturedata.md) for the given texture addition.

## See Also

### Driving playback
- [func update(timeCode: USDStage.TimeCode) -> sending USDPlayer.FrameUpdate?](./update%28timecode%29.md)
  Updates the stage to `timeCode` and returns a [`USDPlayer.FrameUpdate`](./frameupdate.md) describing all scene changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/frameupdate)*