# USDPlayer.MaterialData

**Framework**: USDKit  
**Kind**: struct

Material data from a USD material prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct MaterialData
```

## Topics

### Structures
- [USDPlayer.MaterialData.Update](usdplayer/materialdata/update.md)
  Delta update carrying only the material fields that changed since the last frame.
### Instance Properties
- [let assignedTextures: [String : USDPlayer.TextureID]](usdplayer/materialdata/assignedtextures.md)
  Map from shader parameter name to the bound [`USDPlayer.TextureID`](usdplayer/textureid.md).
- [let id: USDPlayer.MaterialID](usdplayer/materialdata/id.md)
  Unique identifier for this material resource.
- [let primPath: String](usdplayer/materialdata/primpath.md)
  USD prim path this material corresponds to.
- [var shaderGraph: ShaderGraph](usdplayer/materialdata/shadergraph.md)
  Shader graph constructed from the material prim.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/materialdata)*