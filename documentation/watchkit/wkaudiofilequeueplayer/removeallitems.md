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

- [var items: [WKAudioFilePlayerItem]](items.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/items))
  The array of queued items.
- [func advanceToNextItem()](advancetonextitem().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/advancetonextitem()))
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](appenditem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/appenditem(_:)))
  Adds the specified item to the end of the queue.
- [func removeItem(WKAudioFilePlayerItem)](removeitem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeitem(_:)))
  Removes the specified item from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeallitems())*