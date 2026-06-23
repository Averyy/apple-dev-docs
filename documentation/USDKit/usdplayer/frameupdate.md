# USDPlayer.FrameUpdate

**Framework**: USDKit  
**Kind**: struct

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
- [let deformationRemovals: [USDPlayer.DeformationID]](usdplayer/frameupdate/deformationremovals.md)
- [let deformationUpdates: [USDPlayer.DeformationID]](usdplayer/frameupdate/deformationupdates.md)
- [let errors: [USDRenderError]](usdplayer/frameupdate/errors.md)
- [let materialAdditions: [USDPlayer.MaterialID]](usdplayer/frameupdate/materialadditions.md)
- [let materialRemovals: [USDPlayer.MaterialID]](usdplayer/frameupdate/materialremovals.md)
- [let materialUpdates: [USDPlayer.MaterialID]](usdplayer/frameupdate/materialupdates.md)
- [let meshAdditions: [USDPlayer.MeshID]](usdplayer/frameupdate/meshadditions.md)
- [let meshRemovals: [USDPlayer.MeshID]](usdplayer/frameupdate/meshremovals.md)
- [let meshUpdates: [USDPlayer.MeshID]](usdplayer/frameupdate/meshupdates.md)
- [let textureAdditions: [USDPlayer.TextureID]](usdplayer/frameupdate/textureadditions.md)
- [let textureRemovals: [USDPlayer.TextureID]](usdplayer/frameupdate/textureremovals.md)
- [let timeCode: USDStage.TimeCode](usdplayer/frameupdate/timecode.md)
### Instance Methods
- [func takeDeformationAddition(id: USDPlayer.DeformationID) -> USDPlayer.DeformationData?](usdplayer/frameupdate/takedeformationaddition(id:).md)
- [func takeDeformationUpdate(id: USDPlayer.DeformationID) -> USDPlayer.DeformationData.Update?](usdplayer/frameupdate/takedeformationupdate(id:).md)
- [func takeMaterialAddition(id: USDPlayer.MaterialID) -> USDPlayer.MaterialData?](usdplayer/frameupdate/takematerialaddition(id:).md)
- [func takeMaterialUpdate(id: USDPlayer.MaterialID) -> USDPlayer.MaterialData.Update?](usdplayer/frameupdate/takematerialupdate(id:).md)
- [func takeMeshAddition(id: USDPlayer.MeshID) -> USDPlayer.MeshData?](usdplayer/frameupdate/takemeshaddition(id:).md)
- [func takeMeshUpdate(id: USDPlayer.MeshID) -> USDPlayer.MeshData.Update?](usdplayer/frameupdate/takemeshupdate(id:).md)
- [func takeTextureAddition(id: USDPlayer.TextureID) -> USDPlayer.TextureData?](usdplayer/frameupdate/taketextureaddition(id:).md)

## See Also

- [func update(timeCode: USDStage.TimeCode) -> sending USDPlayer.FrameUpdate?](usdplayer/update(timecode:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/frameupdate)*