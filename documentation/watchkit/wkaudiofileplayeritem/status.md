# status

**Framework**: Watchkit  
**Kind**: property

The status of the player item.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var status: WKAudioFilePlayerItemStatus { get }
```

## Overview

When the value of this property is [`WKAudioFilePlayerItemStatus.failed`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus/failed), the [`error`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/error) property contains the reason for the failure.

## See Also

- [var asset: WKAudioFileAsset](asset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/asset))
- [var error: (any Error)?](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/error))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/status)*