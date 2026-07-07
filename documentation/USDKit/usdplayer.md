# USDPlayer

**Framework**: USDKit  
**Kind**: class

An object that drives timeline playback of a USD stage in RealityKit.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class USDPlayer
```

## Topics

### Creating a player
- [convenience init(stage: USDStage)](usdplayer/init(stage:).md)
- [convenience init(stage: USDStage, gpuFamily: MTLGPUFamily)](usdplayer/init(stage:gpufamily:).md)
### Driving playback
- [func update(timeCode: USDStage.TimeCode) -> sending USDPlayer.FrameUpdate?](usdplayer/update(timecode:).md)
- [USDPlayer.FrameUpdate](usdplayer/frameupdate.md)
### Supplying lighting
- [func importCustomIBLTexture(data: Data) throws -> USDPlayer.TextureData](usdplayer/importcustomibltexture(data:).md)
  Import a custom IBL texture with CPU import processing. Throws `USDRenderError` on failure.
### Structures
- [USDPlayer.DeformationData](usdplayer/deformationdata.md)
- [USDPlayer.DeformationID](usdplayer/deformationid.md)
  Deformation resource identifier
- [USDPlayer.MaterialData](usdplayer/materialdata.md)
- [USDPlayer.MaterialID](usdplayer/materialid.md)
  Material resource identifier
- [USDPlayer.MeshData](usdplayer/meshdata.md)
- [USDPlayer.MeshID](usdplayer/meshid.md)
  Mesh resource identifier
- [USDPlayer.TextureData](usdplayer/texturedata.md)
- [USDPlayer.TextureID](usdplayer/textureid.md)
  Texture resource identifier
- [USDPlayer.TextureLevelInfo](usdplayer/texturelevelinfo.md)

## See Also

- [struct USDStageComponent](usdstagecomponent.md)
  A component that renders a USD stage as RealityKit entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer)*