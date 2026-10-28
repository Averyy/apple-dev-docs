# error

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

An error that describes the cause of a failure.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var error: (any Error)? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSError * error;
```

## Discussion

This property is `nil` unless the [`status`](./status.md) property of the player item is [`WKAudioFilePlayerItemStatus.failed`](../wkaudiofileplayeritemstatus/failed.md). When playback fails, the error indicates the reason for the failure.

## See Also

### Getting Information About the Item
- [var asset: WKAudioFileAsset](./asset.md)
  The audio file asset being managed.
- [var status: WKAudioFilePlayerItemStatus](./status.md)
  The status of the player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/error)*