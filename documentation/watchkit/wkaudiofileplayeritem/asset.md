# asset

**Framework**: WatchKit  
**Kind**: property

The audio file asset being managed.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var asset: WKAudioFileAsset { get }
```

#### Discussion

This property is initialized with the asset you specified at creation time. You may access this property at any time regardless of the current status of the player item.

## See Also

- [var status: WKAudioFilePlayerItemStatus](status.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/status))
  The status of the player item.
- [var error: (any Error)?](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/error))
  An error that describes the cause of a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/asset)*