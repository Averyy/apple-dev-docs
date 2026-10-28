# removeItem(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified item from the queue.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
func removeItem(_ item: WKAudioFilePlayerItem)
```

```objc
- (void) removeItem:(WKAudioFilePlayerItem *) item;
```

## Discussion

If `item` is currently playing, the queue stops playback of item before removing it. It then begins playing the next item in the queue.

## Parameters

- `item`: The player item to remove.

## See Also

### Managing Items
- [var items: [WKAudioFilePlayerItem]](./items.md)
  The array of queued items.
- [func advanceToNextItem()](./advancetonextitem%28%29.md)
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](./appenditem%28_%29.md)
  Adds the specified item to the end of the queue.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeitem(_:))*