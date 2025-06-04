# items

**Framework**: Watchkit  
**Kind**: property

The array of queued items.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var items: [WKAudioFilePlayerItem] { get }
```

## Overview

This property contains the array of queued [`WKAudioFilePlayerItem`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem) objects. The initial contents of this array are set at initialization time but you may add or remove items using the methods of this class.

## See Also

- [func advanceToNextItem()](advancetonextitem().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/advancetonextitem()))
- [func appendItem(WKAudioFilePlayerItem)](appenditem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/appenditem(_:)))
- [func removeItem(WKAudioFilePlayerItem)](removeitem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeitem(_:)))
- [func removeAllItems()](removeallitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeallitems()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/items)*