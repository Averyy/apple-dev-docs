# WKAudioFilePlayerItemStatus

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the status of a player item.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: Use the [AVFoundation](../AVFoundation/AVFoundation.md) framework’s [`AVPlayer`](../AVFoundation/avplayer.md) and [`AVQueuePlayer`](../AVFoundation/avqueueplayer.md) classes instead.

## Declaration

```swift
enum WKAudioFilePlayerItemStatus
```

```c
enum WKAudioFilePlayerItemStatus : NSInteger;
```

## Topics

### Statuses
- [WKAudioFilePlayerItemStatus.unknown](./wkaudiofileplayeritemstatus/unknown.md)
  The item’s status is unknown.
- [WKAudioFilePlayerItemStatus.readyToPlay](./wkaudiofileplayeritemstatus/readytoplay.md)
  The item is ready to play.
- [WKAudioFilePlayerItemStatus.failed](./wkaudiofileplayeritemstatus/failed.md)
  The item can’t be played.
### Initializers
- [init?(rawValue: Int)](./wkaudiofileplayeritemstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus)*