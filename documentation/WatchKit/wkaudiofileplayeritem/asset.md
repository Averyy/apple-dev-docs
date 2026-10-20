# asset

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The audio file asset being managed.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var asset: WKAudioFileAsset { get }
```

```objc
@property (nonatomic, readonly) WKAudioFileAsset * asset;
```

#### Discussion

This property is initialized with the asset you specified at creation time. You may access this property at any time regardless of the current status of the player item.

## See Also

### Getting Information About the Item
- [var status: WKAudioFilePlayerItemStatus](./status.md)
  The status of the player item.
- [var error: (any Error)?](./error.md)
  An error that describes the cause of a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/asset)*