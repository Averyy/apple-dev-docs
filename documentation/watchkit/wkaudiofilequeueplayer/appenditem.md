# appendItem(_:)

**Framework**: WatchKit  
**Kind**: method

Adds the specified item to the end of the queue.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func appendItem(_ item: WKAudioFilePlayerItem)
```

## Parameters

- `item`: The player item to add to the queue.

## See Also

- [var items: [WKAudioFilePlayerItem]](items.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/items))
  The array of queued items.
- [func advanceToNextItem()](advancetonextitem().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/advancetonextitem()))
  Ends playback of the current item and begins playing the next item in the queue.
- [func removeItem(WKAudioFilePlayerItem)](removeitem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeitem(_:)))
  Removes the specified item from the queue.
- [func removeAllItems()](removeallitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeallitems()))
  Removes all items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/appenditem(_:))*