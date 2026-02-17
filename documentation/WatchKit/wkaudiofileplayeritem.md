# WKAudioFilePlayerItem

**Framework**: WatchKit  
**Kind**: class

An object that manages the presentation state of an audio file while it is playing.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAudioFilePlayerItem
```

#### Overview

Create a player item for each [`WKAudioFileAsset`](wkaudiofileasset.md) object you want to play and use the player item to observe the state of the audio during playback. You can then associate the player item with an audio queue or player object to control the playback.

The value of the player item’s presentation-related properties are not valid until the underlying asset is loaded. Use the value of the [`status`](wkaudiofileplayeritem/status.md) property to determine when it is valid to get the values of other properties. Specifically, wait until the status changes to [`WKAudioFilePlayerItemStatus.readyToPlay`](wkaudiofileplayeritemstatus/readytoplay.md) to access relevant properties.

If you want to play an asset more than once within a queue of items, you must create separate player items for each placement in the queue.

## Topics

### Creating a Player Item
- [init(asset: WKAudioFileAsset)](wkaudiofileplayeritem/init(asset:).md)
  Creates and returns a player item for the specified audio file asset.
### Getting Information About the Item
- [var asset: WKAudioFileAsset](wkaudiofileplayeritem/asset.md)
  The audio file asset being managed.
- [var status: WKAudioFilePlayerItemStatus](wkaudiofileplayeritem/status.md)
  The status of the player item.
- [var error: (any Error)?](wkaudiofileplayeritem/error.md)
  An error that describes the cause of a failure.
### Managing the Playback Position
- [var currentTime: TimeInterval](wkaudiofileplayeritem/currenttime.md)
  The current playback point, measured in seconds, from the beginning of the audio file.
- [func setCurrentTime(TimeInterval)](wkaudiofileplayeritem/setcurrenttime(_:).md)
  Sets the playback point, measured in seconds, from the beginning of the audio file.
### Accessing the Item’s Status
- [enum WKAudioFilePlayerItemStatus](wkaudiofileplayeritemstatus.md)
  Constants that represent the status of a player item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md)
  An object that controls playback of one or more audio items.
- [class WKAudioFileAsset](wkaudiofileasset.md)
  An object that stores a reference to an audio file and provides metadata information about that file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem)*