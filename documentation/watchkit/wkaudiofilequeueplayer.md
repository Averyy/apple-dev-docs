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

#### Overview

Items are stored in a queue and played sequentially. When playback of the current item ends, playback of the next item begins automatically.

Because this class is a subclass of [`WKAudioFilePlayer`](wkaudiofileplayer.md), it inherits the same playback controls and state information as its superclass. You can use the inherited methods to start and stop playback or change the playback rate. You can also get information about the current status of the player, including the elapsed playback time for the currently playing item. This method also implements the inherited [`replaceCurrentItem(with:)`](wkaudiofileplayer/replacecurrentitem(with:).md) method and uses it to end playback of one item and start playback of another.

## Topics

### Creating a Queue Player
- [convenience init(items: [WKAudioFilePlayerItem])](wkaudiofilequeueplayer/init(items:).md)
  Creates and returns a player initialized with an array of items.
### Managing Items
- [var items: [WKAudioFilePlayerItem]](wkaudiofilequeueplayer/items.md)
  The array of queued items.
- [func advanceToNextItem()](wkaudiofilequeueplayer/advancetonextitem.md)
  Ends playback of the current item and begins playing the next item in the queue.
- [func appendItem(WKAudioFilePlayerItem)](wkaudiofilequeueplayer/appenditem(_:).md)
  Adds the specified item to the end of the queue.
- [func removeItem(WKAudioFilePlayerItem)](wkaudiofilequeueplayer/removeitem(_:).md)
  Removes the specified item from the queue.
- [func removeAllItems()](wkaudiofilequeueplayer/removeallitems.md)
  Removes all items from the queue.

## Relationships

### Inherits From
- [WKAudioFilePlayer](wkaudiofileplayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Playing Background Audio](playing-background-audio.md)
  Enable background audio in your app to provide a seamless playback experience.
- [Adding a Now Playing View](adding-a-now-playing-view.md)
  Provide a view that controls the currently playing audio from your app.
- [class WKInterfaceVolumeControl](wkinterfacevolumecontrol.md)
  An interface element that provides control of the audio volume from the watch or a paired iPhone.
- [PUICAutoLaunchAudioOptOut](../BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut.md)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [class WKAudioFilePlayer](wkaudiofileplayer.md)
  An object that controls playback of a single audio item.
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md)
  An object that manages the presentation state of an audio file while it is playing.
- [class WKAudioFileAsset](wkaudiofileasset.md)
  An object that stores a reference to an audio file and provides metadata information about that file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer)*