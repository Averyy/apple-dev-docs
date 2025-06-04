# currentTime

**Framework**: Watchkit  
**Kind**: property

The elapsed time for the current playing item.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var currentTime: TimeInterval { get }
```

## Overview

This property refers to how much of the audio file has already been played. The value in this property is updated during playback to reflect the current position of the playhead.

The value of this property is valid only when the player item’s status is [`WKAudioFilePlayerStatus.readyToPlay`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/readytoplay).


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/currenttime)*