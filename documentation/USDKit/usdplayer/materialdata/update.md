# USDPlayer.MaterialData.Update

**Framework**: USDKit  
**Kind**: struct

Delta update carrying only the material fields that changed since the last frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/materialdata/update)*