# WKAudioFilePlayerItemTimeJumpedNotification

**Framework**: WatchKit  
**Kind**: var  
**Role**: Global Variable

A notification that the item’s current time has changed discontinuously.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: Use the [AVFoundation](../AVFoundation/AVFoundation.md) framework’s [`AVPlayer`](../AVFoundation/avplayer.md) and [`AVQueuePlayer`](../AVFoundation/avqueueplayer.md) classes instead.

## Declaration

```c
extern NSString * const WKAudioFilePlayerItemTimeJumpedNotification;
```

#### Discussion

The notification’s object is the player item. There is no `userInfo` dictionary.

## See Also

### Receiving Notifications
- [WKAudioFilePlayerItemDidPlayToEndTimeNotification](./wkaudiofileplayeritemdidplaytoendtimenotification.md)
  A notification that the item has played successfully to its end.
- [WKAudioFilePlayerItemFailedToPlayToEndTimeNotification](./wkaudiofileplayeritemfailedtoplaytoendtimenotification.md)
  A notification that the item failed to play to its end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemtimejumpednotification)*