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

- [var items: [WKAudioFilePlayerItem]](wkaudiofilequeueplayer/items.md)
  The array of queued items.
- [func advanceToNextItem()](wkaudiofilequeueplayer/advancetonextitem.md)
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](wkaudiofilequeueplayer/appenditem(_:).md)
  Adds the specified item to the end of the queue.
- [func removeAllItems()](wkaudiofilequeueplayer/removeallitems.md)
  Removes all items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeitem(_:))*