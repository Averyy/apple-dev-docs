# replaceCurrentItem(with:)

**Framework**: WatchKit  
**Kind**: method

Replaces the current player item with a different one.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func replaceCurrentItem(with item: WKAudioFilePlayerItem?)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it to implement support for swapping out the current player item for a new one.

## Parameters

- `item`: The player item whose contents you want to play.

## See Also

- [convenience init(playerItem: WKAudioFilePlayerItem)](init(playeritem:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/init(playeritem:)))
  Creates and returns a player initialized with the specified player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/replacecurrentitem(with:))*