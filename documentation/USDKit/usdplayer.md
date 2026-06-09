# USDPlayer

**Framework**: USDKit  
**Kind**: class

An object that drives timeline playback of a USD stage in RealityKit.

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

## Topics

### Creating a player
- [convenience init(stage: USDStage)](usdplayer/init(stage:).md)
- [convenience init(stage: USDStage, gpuFamily: MTLGPUFamily)](usdplayer/init(stage:gpufamily:).md)
### Driving playback
- [func update(timeCode: USDStage.TimeCode) -> sending USDPlayer.FrameUpdate?](usdplayer/update(timecode:).md)
- [USDPlayer.FrameUpdate](usdplayer/frameupdate.md)
### Supplying lighting
- [func importCustomIBLTexture(data: Data) -> TextureData?](usdplayer/importcustomibltexture(data:).md)
  Import a custom IBL texture with CPU import processing. Returns the texture data directly; returns nil on failure.

## See Also

- [struct USDStageComponent](usdstagecomponent.md)
  A component that renders a USD stage as RealityKit entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer)*