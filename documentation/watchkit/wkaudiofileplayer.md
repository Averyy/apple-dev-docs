# WKAudioFilePlayer

**Framework**: WatchKit  
**Kind**: class

An object that controls playback of a single audio item.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAudioFilePlayer
```

#### Overview

Use a player object to start and stop playback and to control the rate of playback. (The [`WKAudioFileQueuePlayer`](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer) subclass extends the basic behavior to support playback of more than one item.)

The value of the player’s presentation-related properties are not valid until the underlying asset is loaded. Use the value of the [`status`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/status) property to determine when it is valid to get the values of other properties. Specifically, wait until the status changes to [`WKAudioFilePlayerStatus.readyToPlay`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/readytoplay) to access relevant properties.

The [`WKAudioFilePlayer`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer) class is key-value observing compliant for the [`currentItem`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/currentitem), [`status`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/status), and [`rate`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/rate) properties. You can use an observer to detect changes to those properties and react accordingly. For information on how to observe properties using key-value observing, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## Topics

### Creating a Player
- [convenience init(playerItem: WKAudioFilePlayerItem)](init(playeritem:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/init(playeritem:)))
  Creates and returns a player initialized with the specified player item.
- [func replaceCurrentItem(with: WKAudioFilePlayerItem?)](replacecurrentitem(with:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/replacecurrentitem(with:)))
  Replaces the current player item with a different one.
### Configuring and Controlling Playback
- [func play()](play().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/play()))
  Begins playback of the current item.
- [func pause()](pause().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/pause()))
  Pauses playback of the associated item.
- [var rate: Float](rate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/rate))
  The current rate of playback.
### Getting Information About the Player
- [var currentItem: WKAudioFilePlayerItem?](currentitem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/currentitem))
  The player’s current item.
- [var status: WKAudioFilePlayerStatus](status.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/status))
  The status of the player.
- [var error: (any Error)?](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/error))
  An error that describes the cause of a failure.
### Getting Timing Information
- [var currentTime: TimeInterval](currenttime.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/currenttime))
  The elapsed time for the current playing item.
### Constants
- [enum WKAudioFilePlayerStatus](wkaudiofileplayerstatus.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus))
  Constants that represent the status of the player.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Inherited By
- [WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [Playing Background Audio](playing-background-audio.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/playing-background-audio))
  Enable background audio in your app to provide a seamless playback experience.
- [Adding a Now Playing View](adding-a-now-playing-view.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/adding-a-now-playing-view))
  Provide a view that controls the currently playing audio from your app.
- [class WKInterfaceVolumeControl](wkinterfacevolumecontrol.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol))
  An interface element that provides control of the audio volume from the watch or a paired iPhone.
- PUICAutoLaunchAudioOptOut ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut))
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer))
  An object that controls playback of one or more audio items.
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem))
  An object that manages the presentation state of an audio file while it is playing.
- [class WKAudioFileAsset](wkaudiofileasset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset))
  An object that stores a reference to an audio file and provides metadata information about that file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer)*