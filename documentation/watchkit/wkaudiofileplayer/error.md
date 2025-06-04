# error

**Framework**: WatchKit  
**Kind**: property

An error that describes the cause of a failure.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

This property is `nil` unless the [`status`](wkaudiofileplayer/status.md) property of the player item is [`WKAudioFilePlayerStatus.failed`](wkaudiofileplayerstatus/failed.md). When playback fails, the error indicates the reason for the failure.

## See Also

- [var currentItem: WKAudioFilePlayerItem?](wkaudiofileplayer/currentitem.md)
  The player’s current item.
- [var status: WKAudioFilePlayerStatus](wkaudiofileplayer/status.md)
  The status of the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/error)*