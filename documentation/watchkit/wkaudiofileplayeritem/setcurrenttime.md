# setCurrentTime(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the playback point, measured in seconds, from the beginning of the audio file.

**Availability**:
- watchOS 3.2+

## Declaration

```swift
func setCurrentTime(_ currentTime: TimeInterval)
```

## Overview

Use this method to seek a specific point in a sound file or to implement fast-forward and rewind functions.

## Parameters

- `currentTime`: The offset of the current playback position, measured in seconds from the start of the sound.

## See Also

- [var currentTime: TimeInterval](currenttime.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/currenttime))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/setcurrenttime(_:))*