# removeAllItems()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Removes all items from the queue.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
func removeAllItems()
```

```objc
- (void) removeAllItems;
```

## Discussion

This method has the side effect of stopping playback.

## See Also

### Managing Items
- [var items: [WKAudioFilePlayerItem]](./items.md)
  The array of queued items.
- [func advanceToNextItem()](./advancetonextitem%28%29.md)
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](./appenditem%28_%29.md)
  Adds the specified item to the end of the queue.
- [func removeItem(WKAudioFilePlayerItem)](./removeitem%28_%29.md)
  Removes the specified item from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeallitems())*