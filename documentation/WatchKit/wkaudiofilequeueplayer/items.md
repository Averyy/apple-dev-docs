# items

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The array of queued items.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var items: [WKAudioFilePlayerItem] { get }
```

```objc
@property (nonatomic, readonly) NSArray<WKAudioFilePlayerItem *> * items;
```

#### Discussion

This property contains the array of queued [`WKAudioFilePlayerItem`](../wkaudiofileplayeritem.md) objects. The initial contents of this array are set at initialization time but you may add or remove items using the methods of this class.

## See Also

### Managing Items
- [func advanceToNextItem()](./advancetonextitem%28%29.md)
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](./appenditem%28_%29.md)
  Adds the specified item to the end of the queue.
- [func removeItem(WKAudioFilePlayerItem)](./removeitem%28_%29.md)
  Removes the specified item from the queue.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/items)*