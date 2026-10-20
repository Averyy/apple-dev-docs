# appendItem(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified item to the end of the queue.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
func appendItem(_ item: WKAudioFilePlayerItem)
```

```objc
- (void) appendItem:(WKAudioFilePlayerItem *) item;
```

## Parameters

- `item`: The player item to add to the queue.

## See Also

### Managing Items
- [var items: [WKAudioFilePlayerItem]](./items.md)
  The array of queued items.
- [func advanceToNextItem()](./advancetonextitem%28%29.md)
  Ends playback of the current item and begins playing the next item in the queue.
- [func removeItem(WKAudioFilePlayerItem)](./removeitem%28_%29.md)
  Removes the specified item from the queue.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/appenditem(_:))*