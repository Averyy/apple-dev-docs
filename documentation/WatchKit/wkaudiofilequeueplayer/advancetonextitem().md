# advanceToNextItem()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Ends playback of the current item and begins playing the next item in the queue.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
func advanceToNextItem()
```

```objc
- (void) advanceToNextItem;
```

## Discussion

The method removes the current item from the queue before beginning playback of the next item.

## See Also

### Managing Items
- [var items: [WKAudioFilePlayerItem]](./items.md)
  The array of queued items.
- [func appendItem(WKAudioFilePlayerItem)](./appenditem%28_%29.md)
  Adds the specified item to the end of the queue.
- [func removeItem(WKAudioFilePlayerItem)](./removeitem%28_%29.md)
  Removes the specified item from the queue.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/advancetonextitem())*