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

To play an audio file asset, wrap it in a [`WKAudioFilePlayerItem`](wkaudiofileplayeritem.md) object. The player item object stores information about the playback status of the asset and works with a [`WKAudioFilePlayer`](wkaudiofileplayer.md) object to coordinate playback. If you want to queue several audio files for playback, you manage those items using a [`WKAudioFileQueuePlayer`](wkaudiofilequeueplayer.md) object.

## Topics

### Creating an Asset
- [convenience init(url: URL)](wkaudiofileasset/init(url:).md)
  Returns an asset for the audio file at the specified URL.
- [convenience init(url: URL, title: String?, albumTitle: String?, artist: String?)](wkaudiofileasset/init(url:title:albumtitle:artist:).md)
  Returns an audio file asset and sets the metadata for that item.
### Getting the Asset’s Properties
- [var url: URL](wkaudiofileasset/url.md)
  The URL of the audio file.
- [var duration: TimeInterval](wkaudiofileasset/duration.md)
  The duration (in seconds) of the audio file.
- [var title: String?](wkaudiofileasset/title.md)
  The title information for the audio file.
- [var albumTitle: String?](wkaudiofileasset/albumtitle.md)
  The album title information for the audio file.
- [var artist: String?](wkaudiofileasset/artist.md)
  The artist information for the audio file.

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
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md)
  An object that manages the presentation state of an audio file while it is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset)*