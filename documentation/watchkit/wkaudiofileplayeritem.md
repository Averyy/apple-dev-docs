# WKAudioFilePlayerItem

**Framework**: Watchkit  
**Kind**: class

An object that manages the presentation state of an audio file while it is playing.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAudioFilePlayerItem
```

## Overview

Create a player item for each [`WKAudioFileAsset`](https://developer.apple.com/documentation/watchkit/wkaudiofileasset) object you want to play and use the player item to observe the state of the audio during playback. You can then associate the player item with an audio queue or player object to control the playback.

The value of the player item’s presentation-related properties are not valid until the underlying asset is loaded. Use the value of the [`status`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/status) property to determine when it is valid to get the values of other properties. Specifically, wait until the status changes to [`WKAudioFilePlayerItemStatus.readyToPlay`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus/readytoplay) to access relevant properties.

If you want to play an asset more than once within a queue of items, you must create separate player items for each placement in the queue.

## Topics

### Creating a Player Item
- [init(asset: WKAudioFileAsset)](init(asset:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/init(asset:)))
  Creates and returns a player item for the specified audio file asset.
### Getting Information About the Item
- [var asset: WKAudioFileAsset](asset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/asset))
  The audio file asset being managed.
- [var status: WKAudioFilePlayerItemStatus](status.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/status))
  The status of the player item.
- [var error: (any Error)?](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/error))
  An error that describes the cause of a failure.
### Managing the Playback Position
- [var currentTime: TimeInterval](currenttime.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/currenttime))
  The current playback point, measured in seconds, from the beginning of the audio file.
- [func setCurrentTime(TimeInterval)](setcurrenttime(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/setcurrenttime(_:)))
  Sets the playback point, measured in seconds, from the beginning of the audio file.
### Accessing the Item’s Status
- [enum WKAudioFilePlayerItemStatus](wkaudiofileplayeritemstatus.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus))
  Constants that represent the status of a player item.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
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
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer))
- [class WKAudioFileAsset](wkaudiofileasset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem)*