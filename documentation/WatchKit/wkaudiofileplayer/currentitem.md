# currentItem

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The player’s current item.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var currentItem: WKAudioFilePlayerItem? { get }
```

```objc
@property (nonatomic, readonly, nullable) WKAudioFilePlayerItem * currentItem;
```

#### Discussion

The value of this property is set at initialization time.

## See Also

### Getting Information About the Player
- [var status: WKAudioFilePlayerStatus](./status.md)
  The status of the player.
- [var error: (any Error)?](./error.md)
  An error that describes the cause of a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/currentitem)*