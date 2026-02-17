# status

**Framework**: WatchKit  
**Kind**: property

The status of the player item.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var status: WKAudioFilePlayerItemStatus { get }
```

#### Discussion

When the value of this property is [`WKAudioFilePlayerItemStatus.failed`](wkaudiofileplayeritemstatus/failed.md), the [`error`](wkaudiofileplayeritem/error.md) property contains the reason for the failure.

## See Also

- [var asset: WKAudioFileAsset](wkaudiofileplayeritem/asset.md)
  The audio file asset being managed.
- [var error: (any Error)?](wkaudiofileplayeritem/error.md)
  An error that describes the cause of a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/status)*