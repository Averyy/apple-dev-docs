# WKAudioFileQueuePlayer

**Framework**: Watchkit  
**Kind**: class

An object that controls playback of one or more audio items.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAudioFileQueuePlayer
```

## Overview

Items are stored in a queue and played sequentially. When playback of the current item ends, playback of the next item begins automatically.

Because this class is a subclass of [`WKAudioFilePlayer`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer), it inherits the same playback controls and state information as its superclass. You can use the inherited methods to start and stop playback or change the playback rate. You can also get information about the current status of the player, including the elapsed playback time for the currently playing item. This method also implements the inherited [`replaceCurrentItem(with:)`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/replacecurrentitem(with:)) method and uses it to end playback of one item and start playback of another.

## Topics

### Creating a Queue Player
- [convenience init(items: [WKAudioFilePlayerItem])](init(items:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/init(items:)))
  Creates and returns a player initialized with an array of items.
### Managing Items
- [var items: [WKAudioFilePlayerItem]](items.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/items))
  The array of queued items.
- [func advanceToNextItem()](advancetonextitem().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/advancetonextitem()))
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](appenditem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/appenditem(_:)))
  Adds the specified item to the end of the queue.
- [func removeItem(WKAudioFilePlayerItem)](removeitem(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeitem(_:)))
  Removes the specified item from the queue.
- [func removeAllItems()](removeallitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/removeallitems()))
  Removes all items from the queue.

## Relationships

### Inherits From
- [WKAudioFilePlayer](wkaudiofileplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [Playing Background Audio](playing-background-audio.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/playing-background-audio))
- [Adding a Now Playing View](adding-a-now-playing-view.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/adding-a-now-playing-view))
- [class WKInterfaceVolumeControl](wkinterfacevolumecontrol.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol))
- PUICAutoLaunchAudioOptOut ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut))
- [class WKAudioFilePlayer](wkaudiofileplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer))
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem))
- [class WKAudioFileAsset](wkaudiofileasset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer)*