# init(playerItem:)

**Framework**: WatchKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a player initialized with the specified player item.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
convenience init(playerItem item: WKAudioFilePlayerItem)
```

```objc
+ (instancetype) playerWithPlayerItem:(WKAudioFilePlayerItem *) item;
```

#### Return Value

An initialized player object.

## Parameters

- `item`: The player item containing the audio asset to play. This parameter must not be `nil`.

## See Also

### Creating a Player
- [func replaceCurrentItem(with: WKAudioFilePlayerItem?)](./replacecurrentitem%28with%29.md)
  Replaces the current player item with a different one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/init(playeritem:))*