# error

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

An error that describes the cause of a failure.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var error: (any Error)? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSError * error;
```

## Discussion

This property is `nil` unless the [`status`](./status.md) property of the player item is [`WKAudioFilePlayerStatus.failed`](../wkaudiofileplayerstatus/failed.md). When playback fails, the error indicates the reason for the failure.

## See Also

### Getting Information About the Player
- [var currentItem: WKAudioFilePlayerItem?](./currentitem.md)
  The player’s current item.
- [var status: WKAudioFilePlayerStatus](./status.md)
  The status of the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/error)*