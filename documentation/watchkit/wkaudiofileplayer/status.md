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

When the value of this property is [`WKAudioFilePlayerStatus.failed`](wkaudiofileplayerstatus/failed.md), the [`error`](wkaudiofileplayer/error.md) property contains the reason for the failure.

## See Also

- [var currentItem: WKAudioFilePlayerItem?](wkaudiofileplayer/currentitem.md)
  The player’s current item.
- [var error: (any Error)?](wkaudiofileplayer/error.md)
  An error that describes the cause of a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/status)*