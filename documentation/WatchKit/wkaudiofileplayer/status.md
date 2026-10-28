# status

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The status of the player.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var status: WKAudioFilePlayerStatus { get }
```

```objc
@property (nonatomic, readonly) WKAudioFilePlayerStatus status;
```

## Discussion

When the value of this property is [`WKAudioFilePlayerStatus.failed`](../wkaudiofileplayerstatus/failed.md), the [`error`](./error.md) property contains the reason for the failure.

## See Also

### Getting Information About the Player
- [var currentItem: WKAudioFilePlayerItem?](./currentitem.md)
  The player’s current item.
- [var error: (any Error)?](./error.md)
  An error that describes the cause of a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/status)*