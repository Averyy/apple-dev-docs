# update(timeCode:)

**Framework**: USDKit  
**Kind**: method

Updates the stage to `timeCode` and returns a [`USDPlayer.FrameUpdate`](usdplayer/frameupdate.md) describing all scene changes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func update(timeCode: USDStage.TimeCode) -> sending USDPlayer.FrameUpdate?
```

#### Discussion

Returns `nil` if nothing changed.

## See Also

- [USDPlayer.FrameUpdate](usdplayer/frameupdate.md)
  A snapshot of all mesh, material, texture, and deformation changes from the last update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/update(timecode:))*