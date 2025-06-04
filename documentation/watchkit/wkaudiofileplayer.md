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

Use a player object to start and stop playback and to control the rate of playback. (The [`WKAudioFileQueuePlayer`](wkaudiofilequeueplayer.md) subclass extends the basic behavior to support playback of more than one item.)

The value of the player’s presentation-related properties are not valid until the underlying asset is loaded. Use the value of the [`status`](wkaudiofileplayer/status.md) property to determine when it is valid to get the values of other properties. Specifically, wait until the status changes to [`WKAudioFilePlayerStatus.readyToPlay`](wkaudiofileplayerstatus/readytoplay.md) to access relevant properties.

The [`WKAudioFilePlayer`](wkaudiofileplayer.md) class is key-value observing compliant for the [`currentItem`](wkaudiofileplayer/currentitem.md), [`status`](wkaudiofileplayer/status.md), and [`rate`](wkaudiofileplayer/rate.md) properties. You can use an observer to detect changes to those properties and react accordingly. For information on how to observe properties using key-value observing, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## Topics

### Creating a Player
- [convenience init(playerItem: WKAudioFilePlayerItem)](wkaudiofileplayer/init(playeritem:).md)
  Creates and returns a player initialized with the specified player item.
- [func replaceCurrentItem(with: WKAudioFilePlayerItem?)](wkaudiofileplayer/replacecurrentitem(with:).md)
  Replaces the current player item with a different one.
### Configuring and Controlling Playback
- [func play()](wkaudiofileplayer/play.md)
  Begins playback of the current item.
- [func pause()](wkaudiofileplayer/pause.md)
  Pauses playback of the associated item.
- [var rate: Float](wkaudiofileplayer/rate.md)
  The current rate of playback.
### Getting Information About the Player
- [var currentItem: WKAudioFilePlayerItem?](wkaudiofileplayer/currentitem.md)
  The player’s current item.
- [var status: WKAudioFilePlayerStatus](wkaudiofileplayer/status.md)
  The status of the player.
- [var error: (any Error)?](wkaudiofileplayer/error.md)
  An error that describes the cause of a failure.
### Getting Timing Information
- [var currentTime: TimeInterval](wkaudiofileplayer/currenttime.md)
  The elapsed time for the current playing item.
### Constants
- [enum WKAudioFilePlayerStatus](wkaudiofileplayerstatus.md)
  Constants that represent the status of the player.

## Relationships

### Inherits From
- [NSObject](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
### Inherited By
- [WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md)
### Conforms To
- [CVarArg](https://developer.apple.com/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [NSObjectProtocol](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)

## See Also

- [Playing Background Audio](playing-background-audio.md)
  Enable background audio in your app to provide a seamless playback experience.
- [Adding a Now Playing View](adding-a-now-playing-view.md)
  Provide a view that controls the currently playing audio from your app.
- [class WKInterfaceVolumeControl](wkinterfacevolumecontrol.md)
  An interface element that provides control of the audio volume from the watch or a paired iPhone.
- [PUICAutoLaunchAudioOptOut](https://developer.apple.com/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md)
  An object that controls playback of one or more audio items.
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md)
  An object that manages the presentation state of an audio file while it is playing.
- [class WKAudioFileAsset](wkaudiofileasset.md)
  An object that stores a reference to an audio file and provides metadata information about that file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer)*