# currentTime

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The current playback point, measured in seconds, from the beginning of the audio file.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var currentTime: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval currentTime;
```

## Discussion

This property refers to how much of the audio file has already been played. The value in this property is updated during playback to reflect the current position of the playhead.

The value of this property is valid only when the player item’s status is [`WKAudioFilePlayerItemStatus.readyToPlay`](../wkaudiofileplayeritemstatus/readytoplay.md).

## See Also

### Managing the Playback Position
- [func setCurrentTime(TimeInterval)](./setcurrenttime%28_%29.md)
  Sets the playback point, measured in seconds, from the beginning of the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/currenttime)*