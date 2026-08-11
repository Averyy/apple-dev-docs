# USDPlayer

**Framework**: USDKit  
**Kind**: class

Drives timeline playback of a USD stage and produces per-frame render data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class USDPlayer
```

#### Overview

An object that drives timeline playback of a USD stage in RealityKit.

## Topics

### Creating a player
- [convenience init(stage: USDStage)](usdplayer/init(stage:).md)
  Creates a Metal-enabled player for the given USD stage.
- [convenience init(stage: USDStage, gpuFamily: MTLGPUFamily)](usdplayer/init(stage:gpufamily:).md)
  Creates a Metal-less player for the given USD stage.
### Driving playback
- [func update(timeCode: USDStage.TimeCode) -> sending USDPlayer.FrameUpdate?](usdplayer/update(timecode:).md)
  Updates the stage to `timeCode` and returns a [`USDPlayer.FrameUpdate`](usdplayer/frameupdate.md) describing all scene changes.
- [USDPlayer.FrameUpdate](usdplayer/frameupdate.md)
  A snapshot of all mesh, material, texture, and deformation changes from the last update.
### Supplying lighting
- [func importCustomIBLTexture(data: Data) throws -> USDPlayer.TextureData](usdplayer/importcustomibltexture(data:).md)
  Imports a custom IBL texture.
### Structures
- [USDPlayer.DeformationData](usdplayer/deformationdata.md)
  Deformation data for a single deformable mesh.
- [USDPlayer.DeformationID](usdplayer/deformationid.md)
  Deformation resource identifier.
- [USDPlayer.MaterialData](usdplayer/materialdata.md)
  Material data from a USD material prim.
- [USDPlayer.MaterialID](usdplayer/materialid.md)
  Material resource identifier.
- [USDPlayer.MeshData](usdplayer/meshdata.md)
  Mesh geometry data from a USD mesh prim.
- [USDPlayer.MeshID](usdplayer/meshid.md)
  Mesh resource identifier.
- [USDPlayer.TextureData](usdplayer/texturedata.md)
  Texture data from a texture asset referenced by a material prim.
- [USDPlayer.TextureID](usdplayer/textureid.md)
  Texture resource identifier.
- [USDPlayer.TextureLevelInfo](usdplayer/texturelevelinfo.md)
  Byte-layout descriptor for a single mip level within a [`USDPlayer.TextureData`](usdplayer/texturedata.md).

## See Also

- [struct USDStageComponent](usdstagecomponent.md)
  A component that renders a USD stage as RealityKit entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer)*