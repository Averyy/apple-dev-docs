# advanceToNextItem()

**Framework**: Watchkit  
**Kind**: method

Ends playback of the current item and begins playing the next item in the queue.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func advanceToNextItem()
```

#### Discussion

The method removes the current item from the queue before beginning playback of the next item.

## See Also

- [var items: [WKAudioFilePlayerItem]](wkaudiofilequeueplayer/items.md)
  The array of queued items.
- [func appendItem(WKAudioFilePlayerItem)](wkaudiofilequeueplayer/appenditem(_:).md)
  Adds the specified item to the end of the queue.
- [func removeItem(WKAudioFilePlayerItem)](wkaudiofilequeueplayer/removeitem(_:).md)
  Removes the specified item from the queue.
- [func removeAllItems()](wkaudiofilequeueplayer/removeallitems.md)
  Removes all items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/advancetonextitem())*