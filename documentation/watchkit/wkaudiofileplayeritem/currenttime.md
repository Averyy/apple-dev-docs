# currentTime

**Framework**: WatchKit  
**Kind**: property

The current playback point, measured in seconds, from the beginning of the audio file.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var currentTime: TimeInterval { get }
```

#### Discussion

This property refers to how much of the audio file has already been played. The value in this property is updated during playback to reflect the current position of the playhead.

The value of this property is valid only when the player item’s status is [`WKAudioFilePlayerItemStatus.readyToPlay`](wkaudiofileplayeritemstatus/readytoplay.md).

## See Also

- [func setCurrentTime(TimeInterval)](wkaudiofileplayeritem/setcurrenttime(_:).md)
  Sets the playback point, measured in seconds, from the beginning of the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/currenttime)*