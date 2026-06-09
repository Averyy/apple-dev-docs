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
- [let deformationAdditions: [DeformationID]](usdplayer/frameupdate/deformationadditions.md)
- [let deformationRemovals: [DeformationID]](usdplayer/frameupdate/deformationremovals.md)
- [let deformationUpdates: [DeformationID]](usdplayer/frameupdate/deformationupdates.md)
- [let errors: [USDRenderError]](usdplayer/frameupdate/errors.md)
- [let materialAdditions: [MaterialID]](usdplayer/frameupdate/materialadditions.md)
- [let materialRemovals: [MaterialID]](usdplayer/frameupdate/materialremovals.md)
- [let materialUpdates: [MaterialID]](usdplayer/frameupdate/materialupdates.md)
- [let meshAdditions: [MeshID]](usdplayer/frameupdate/meshadditions.md)
- [let meshRemovals: [MeshID]](usdplayer/frameupdate/meshremovals.md)
- [let meshUpdates: [MeshID]](usdplayer/frameupdate/meshupdates.md)
- [let textureAdditions: [TextureID]](usdplayer/frameupdate/textureadditions.md)
- [let textureRemovals: [TextureID]](usdplayer/frameupdate/textureremovals.md)
- [let timestamp: USDStage.TimeCode](usdplayer/frameupdate/timestamp.md)
### Instance Methods
- [func takeDeformationAddition(id: DeformationID) -> DeformationData?](usdplayer/frameupdate/takedeformationaddition(id:).md)
- [func takeDeformationUpdate(id: DeformationID) -> DeformationData.Update?](usdplayer/frameupdate/takedeformationupdate(id:).md)
- [func takeMaterialAddition(id: MaterialID) -> MaterialData?](usdplayer/frameupdate/takematerialaddition(id:).md)
- [func takeMaterialUpdate(id: MaterialID) -> MaterialData.Update?](usdplayer/frameupdate/takematerialupdate(id:).md)
- [func takeMeshAddition(id: MeshID) -> MeshData?](usdplayer/frameupdate/takemeshaddition(id:).md)
- [func takeMeshUpdate(id: MeshID) -> MeshData.Update?](usdplayer/frameupdate/takemeshupdate(id:).md)
- [func takeTextureAddition(id: TextureID) -> TextureData?](usdplayer/frameupdate/taketextureaddition(id:).md)

## See Also

- [func update(timeCode: USDStage.TimeCode) -> sending USDPlayer.FrameUpdate?](usdplayer/update(timecode:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/frameupdate)*