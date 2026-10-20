# USDPlayer.MaterialData.Update

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

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
- [let assignedTextures: [String : USDPlayer.TextureID]?](./update/assignedtextures.md)
  Updated texture bindings.
- [let id: USDPlayer.MaterialID](./update/id.md)
  Unique identifier for the material being updated.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/materialdata/update)*