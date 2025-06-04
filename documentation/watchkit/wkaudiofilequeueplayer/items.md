# items

**Framework**: WatchKit  
**Kind**: property

The array of queued items.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var items: [WKAudioFilePlayerItem] { get }
```

#### Discussion

This property contains the array of queued [`WKAudioFilePlayerItem`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem) objects. The initial contents of this array are set at initialization time but you may add or remove items using the methods of this class.

## See Also

- [func advanceToNextItem()](advancetonextitem().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/advancetonextitem()))
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](appenditem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/appenditem(_:)))
  Adds the specified item to the end of the queue.
- [func removeItem(WKAudioFilePlayerItem)](removeitem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeitem(_:)))
  Removes the specified item from the queue.
- [func removeAllItems()](removeallitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeallitems()))
  Removes all items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/items)*