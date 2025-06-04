# error

**Framework**: Watchkit  
**Kind**: property

An error that describes the cause of a failure.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var error: (any Error)? { get }
```

## Overview

This property is `nil` unless the [`status`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/status) property of the player item is [`WKAudioFilePlayerStatus.failed`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/failed). When playback fails, the error indicates the reason for the failure.

## See Also

- [var currentItem: WKAudioFilePlayerItem?](currentitem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/currentitem))
- [var status: WKAudioFilePlayerStatus](status.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/status))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/error)*