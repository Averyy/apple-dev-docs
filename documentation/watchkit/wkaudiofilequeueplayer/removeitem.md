# removeItem(_:)

**Framework**: WatchKit  
**Kind**: method

Removes the specified item from the queue.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func removeItem(_ item: WKAudioFilePlayerItem)
```

#### Discussion

If `item` is currently playing, the queue stops playback of item before removing it. It then begins playing the next item in the queue.

## Parameters

- `item`: The player item to remove.

## See Also

- [var items: [WKAudioFilePlayerItem]](items.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/items))
  The array of queued items.
- [func advanceToNextItem()](advancetonextitem().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/advancetonextitem()))
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](appenditem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/appenditem(_:)))
  Adds the specified item to the end of the queue.
- [func removeAllItems()](removeallitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeallitems()))
  Removes all items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeitem(_:))*