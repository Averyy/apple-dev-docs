# WKAudioFilePlayerStatus

**Framework**: WatchKit  
**Kind**: enum

Constants that represent the status of the player.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKAudioFilePlayerStatus
```

## Topics

### Constants
- [WKAudioFilePlayerStatus.unknown](wkaudiofileplayerstatus/unknown.md)
  The status of the item is unknown because the player has not yet loaded the audio file for playback.
- [WKAudioFilePlayerStatus.readyToPlay](wkaudiofileplayerstatus/readytoplay.md)
  The player is ready to play its item.
- [WKAudioFilePlayerStatus.failed](wkaudiofileplayerstatus/failed.md)
  The player can no longer play the audio because of an error. Use the [`error`](wkaudiofileplayer/error.md) property to get information about the error that occurred.
### Initializers
- [init?(rawValue: Int)](wkaudiofileplayerstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus)*