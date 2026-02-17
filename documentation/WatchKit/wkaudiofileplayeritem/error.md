# error

**Framework**: WatchKit  
**Kind**: property

An error that describes the cause of a failure.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

This property is `nil` unless the [`status`](wkaudiofileplayeritem/status.md) property of the player item is [`WKAudioFilePlayerItemStatus.failed`](wkaudiofileplayeritemstatus/failed.md). When playback fails, the error indicates the reason for the failure.

## See Also

- [var asset: WKAudioFileAsset](wkaudiofileplayeritem/asset.md)
  The audio file asset being managed.
- [var status: WKAudioFilePlayerItemStatus](wkaudiofileplayeritem/status.md)
  The status of the player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/error)*