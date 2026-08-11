# update(timeCode:)

**Framework**: USDKit  
**Kind**: method

Updates the stage to `timeCode` and returns a [`USDPlayer.FrameUpdate`](usdplayer/frameupdate.md) describing all scene changes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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