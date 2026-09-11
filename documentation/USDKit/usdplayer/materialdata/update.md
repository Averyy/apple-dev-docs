# USDPlayer.MaterialData.Update

**Framework**: USDKit  
**Kind**: struct

Delta update carrying only the material fields that changed since the last frame.

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
- [let assignedTextures: [String : USDPlayer.TextureID]?](usdplayer/materialdata/update/assignedtextures.md)
  Updated texture bindings.
- [let id: USDPlayer.MaterialID](usdplayer/materialdata/update/id.md)
  Unique identifier for the material being updated.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/materialdata/update)*