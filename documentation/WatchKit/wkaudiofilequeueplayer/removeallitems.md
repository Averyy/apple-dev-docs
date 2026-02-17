# removeAllItems()

**Framework**: WatchKit  
**Kind**: method

Removes all items from the queue.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func removeAllItems()
```

#### Discussion

This method has the side effect of stopping playback.

## See Also

- [var items: [WKAudioFilePlayerItem]](wkaudiofilequeueplayer/items.md)
  The array of queued items.
- [func advanceToNextItem()](wkaudiofilequeueplayer/advancetonextitem.md)
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](wkaudiofilequeueplayer/appenditem(_:).md)
  Adds the specified item to the end of the queue.
- [func removeItem(WKAudioFilePlayerItem)](wkaudiofilequeueplayer/removeitem(_:).md)
  Removes the specified item from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeallitems())*