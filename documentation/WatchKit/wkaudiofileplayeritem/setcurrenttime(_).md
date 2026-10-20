# setCurrentTime(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the playback point, measured in seconds, from the beginning of the audio file.

**Availability**:
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: Use AVFoundation’s AVPlayer and AVQueuePlayer instead

## Declaration

```swift
func setCurrentTime(_ currentTime: TimeInterval)
```

```objc
- (void) setCurrentTime:(NSTimeInterval) currentTime;
```

#### Discussion

Use this method to seek a specific point in a sound file or to implement fast-forward and rewind functions.

## Parameters

- `currentTime`: The offset of the current playback position, measured in seconds from the start of the sound.

## See Also

### Managing the Playback Position
- [var currentTime: TimeInterval](./currenttime.md)
  The current playback point, measured in seconds, from the beginning of the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/setcurrenttime(_:))*