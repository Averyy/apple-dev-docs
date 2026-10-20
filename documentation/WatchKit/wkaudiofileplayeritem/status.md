# status

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The status of the player item.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var status: WKAudioFilePlayerItemStatus { get }
```

```objc
@property (nonatomic, readonly) WKAudioFilePlayerItemStatus status;
```

#### Discussion

When the value of this property is [`WKAudioFilePlayerItemStatus.failed`](../wkaudiofileplayeritemstatus/failed.md), the [`error`](./error.md) property contains the reason for the failure.

## See Also

### Getting Information About the Item
- [var asset: WKAudioFileAsset](./asset.md)
  The audio file asset being managed.
- [var error: (any Error)?](./error.md)
  An error that describes the cause of a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/status)*