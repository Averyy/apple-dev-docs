# USDPlayer.FrameUpdate

**Framework**: USDKit  
**Kind**: struct

A snapshot of all mesh, material, texture, and deformation changes from the last update.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FrameUpdate
```

## Topics

### Instance Properties
- [let deformationAdditions: [USDPlayer.DeformationID]](usdplayer/frameupdate/deformationadditions.md)
  IDs of newly added deformation resources.
- [let deformationRemovals: [USDPlayer.DeformationID]](usdplayer/frameupdate/deformationremovals.md)
  IDs of deformation resources removed this frame.
- [let deformationUpdates: [USDPlayer.DeformationID]](usdplayer/frameupdate/deformationupdates.md)
  IDs of deformation resources with delta changes this frame.
- [let errors: [USDRenderError]](usdplayer/frameupdate/errors.md)
  Errors encountered during this update.
- [let materialAdditions: [USDPlayer.MaterialID]](usdplayer/frameupdate/materialadditions.md)
  IDs of newly added materials.
- [let materialRemovals: [USDPlayer.MaterialID]](usdplayer/frameupdate/materialremovals.md)
  IDs of materials removed this frame.
- [let materialUpdates: [USDPlayer.MaterialID]](usdplayer/frameupdate/materialupdates.md)
  IDs of materials with delta changes this frame.
- [let meshAdditions: [USDPlayer.MeshID]](usdplayer/frameupdate/meshadditions.md)
  IDs of newly added meshes.
- [let meshRemovals: [USDPlayer.MeshID]](usdplayer/frameupdate/meshremovals.md)
  IDs of meshes removed this frame.
- [let meshUpdates: [USDPlayer.MeshID]](usdplayer/frameupdate/meshupdates.md)
  IDs of meshes with delta changes this frame.
- [let textureAdditions: [USDPlayer.TextureID]](usdplayer/frameupdate/textureadditions.md)
  IDs of newly added texture assets.
- [let textureRemovals: [USDPlayer.TextureID]](usdplayer/frameupdate/textureremovals.md)
  IDs of texture assets removed this frame.
- [let timeCode: USDStage.TimeCode](usdplayer/frameupdate/timecode.md)
  The USD time code this update corresponds to.
### Instance Methods
- [func takeDeformationAddition(id: USDPlayer.DeformationID) -> USDPlayer.DeformationData?](usdplayer/frameupdate/takedeformationaddition(id:).md)
  Consumes and returns the [`USDPlayer.DeformationData`](usdplayer/deformationdata.md) for the given deformation addition.
- [func takeDeformationUpdate(id: USDPlayer.DeformationID) -> USDPlayer.DeformationData.Update?](usdplayer/frameupdate/takedeformationupdate(id:).md)
  Consumes and returns the [`USDPlayer.DeformationData.Update`](usdplayer/deformationdata/update.md) for the given deformation delta update.
- [func takeMaterialAddition(id: USDPlayer.MaterialID) -> USDPlayer.MaterialData?](usdplayer/frameupdate/takematerialaddition(id:).md)
  Consumes and returns the [`USDPlayer.MaterialData`](usdplayer/materialdata.md) for the given material addition.
- [func takeMaterialUpdate(id: USDPlayer.MaterialID) -> USDPlayer.MaterialData.Update?](usdplayer/frameupdate/takematerialupdate(id:).md)
  Consumes and returns the [`USDPlayer.MaterialData.Update`](usdplayer/materialdata/update.md) for the given material delta update.
- [func takeMeshAddition(id: USDPlayer.MeshID) -> USDPlayer.MeshData?](usdplayer/frameupdate/takemeshaddition(id:).md)
  Consumes and returns the [`USDPlayer.MeshData`](usdplayer/meshdata.md) for the given mesh addition.
- [func takeMeshUpdate(id: USDPlayer.MeshID) -> USDPlayer.MeshData.Update?](usdplayer/frameupdate/takemeshupdate(id:).md)
  Consumes and returns the [`USDPlayer.MeshData.Update`](usdplayer/meshdata/update.md) for the given mesh delta update.
- [func takeTextureAddition(id: USDPlayer.TextureID) -> USDPlayer.TextureData?](usdplayer/frameupdate/taketextureaddition(id:).md)
  Consumes and returns the [`USDPlayer.TextureData`](usdplayer/texturedata.md) for the given texture addition.

## See Also

- [func update(timeCode: USDStage.TimeCode) -> sending USDPlayer.FrameUpdate?](usdplayer/update(timecode:).md)
  Updates the stage to `timeCode` and returns a [`USDPlayer.FrameUpdate`](usdplayer/frameupdate.md) describing all scene changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/frameupdate)*