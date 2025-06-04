# WKAudioFileAsset

**Framework**: WatchKit  
**Kind**: class

An object that stores a reference to an audio file and provides metadata information about that file.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAudioFileAsset
```

#### Overview

You create assets when you want to play audio from your watchOS app. Use the audio file asset object to store the location of the file and any Now Playing information you want displayed while the audio is playing.

Audio assets must refer to files on the local file system. If you have audio files that are stored on a server, you must download them to the user’s Apple Watch before attempting to play them using an audio file asset object.

It is recommended that you encode audio files using 32 kbps stereo AAC. You may use other bit rates, or the LPCM encoding, as preferred for your content.

To play an audio file asset, wrap it in a [`WKAudioFilePlayerItem`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem) object. The player item object stores information about the playback status of the asset and works with a [`WKAudioFilePlayer`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer) object to coordinate playback. If you want to queue several audio files for playback, you manage those items using a [`WKAudioFileQueuePlayer`](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer) object.

## Topics

### Creating an Asset
- [convenience init(url: URL)](init(url:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/init(url:)))
  Returns an asset for the audio file at the specified URL.
- [convenience init(url: URL, title: String?, albumTitle: String?, artist: String?)](init(url:title:albumtitle:artist:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/init(url:title:albumtitle:artist:)))
  Returns an audio file asset and sets the metadata for that item.
### Getting the Asset’s Properties
- [var url: URL](url.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/url))
  The URL of the audio file.
- [var duration: TimeInterval](duration.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/duration))
  The duration (in seconds) of the audio file.
- [var title: String?](title.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/title))
  The title information for the audio file.
- [var albumTitle: String?](albumtitle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/albumtitle))
  The album title information for the audio file.
- [var artist: String?](artist.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/artist))
  The artist information for the audio file.

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
  Enable background audio in your app to provide a seamless playback experience.
- [Adding a Now Playing View](adding-a-now-playing-view.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/adding-a-now-playing-view))
  Provide a view that controls the currently playing audio from your app.
- [class WKInterfaceVolumeControl](wkinterfacevolumecontrol.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol))
  An interface element that provides control of the audio volume from the watch or a paired iPhone.
- PUICAutoLaunchAudioOptOut ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut))
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [class WKAudioFilePlayer](wkaudiofileplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer))
  An object that controls playback of a single audio item.
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer))
  An object that controls playback of one or more audio items.
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem))
  An object that manages the presentation state of an audio file while it is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset)*