# WKAudioFilePlayerStatus

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the status of the player.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: Use the [AVFoundation](../AVFoundation/AVFoundation.md) framework’s [`AVPlayer`](../AVFoundation/avplayer.md) and [`AVQueuePlayer`](../AVFoundation/avqueueplayer.md) classes instead.

## Declaration

```swift
enum WKAudioFilePlayerStatus
```

```c
enum WKAudioFilePlayerStatus : NSInteger;
```

## Topics

### Constants
- [WKAudioFilePlayerStatus.unknown](./wkaudiofileplayerstatus/unknown.md)
  The status of the item is unknown because the player has not yet loaded the audio file for playback.
- [WKAudioFilePlayerStatus.readyToPlay](./wkaudiofileplayerstatus/readytoplay.md)
  The player is ready to play its item.
- [WKAudioFilePlayerStatus.failed](./wkaudiofileplayerstatus/failed.md)
  The player can no longer play the audio because of an error. Use the [`error`](./wkaudiofileplayer/error.md) property to get information about the error that occurred.
### Initializers
- [init?(rawValue: Int)](./wkaudiofileplayerstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus)*