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

This property is `nil` unless the [`status`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/status) property of the player item is [`WKAudioFilePlayerItemStatus.failed`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus/failed). When playback fails, the error indicates the reason for the failure.

## See Also

- [var asset: WKAudioFileAsset](asset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/asset))
- [var status: WKAudioFilePlayerItemStatus](status.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/status))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/error)*