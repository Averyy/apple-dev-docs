# status

**Framework**: WatchKit  
**Kind**: property

The status of the player.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var status: WKAudioFilePlayerStatus { get }
```

#### Discussion

When the value of this property is [`WKAudioFilePlayerStatus.failed`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/failed), the [`error`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/error) property contains the reason for the failure.

## See Also

- [var currentItem: WKAudioFilePlayerItem?](currentitem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/currentitem))
  The player’s current item.
- [var error: (any Error)?](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/error))
  An error that describes the cause of a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/status)*