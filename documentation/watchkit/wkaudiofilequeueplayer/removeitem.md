# removeItem(_:)

**Framework**: Watchkit  
**Kind**: method

Removes the specified item from the queue.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func removeItem(_ item: WKAudioFilePlayerItem)
```

## Overview

If `item` is currently playing, the queue stops playback of item before removing it. It then begins playing the next item in the queue.

## Parameters

- `item`: The player item to remove.

## See Also

- [var items: [WKAudioFilePlayerItem]](items.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/items))
- [func advanceToNextItem()](advancetonextitem().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/advancetonextitem()))
- [func appendItem(WKAudioFilePlayerItem)](appenditem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/appenditem(_:)))
- [func removeAllItems()](removeallitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeallitems()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeitem(_:))*