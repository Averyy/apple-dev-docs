# Adding a Now Playing View

**Framework**: WatchKit

Provide a view that controls the currently playing audio from your app.

#### Overview

With a Now Playing view, users can control current or recently played audio without leaving your app. When your app presents the Now Playing view, it immediately displays information about the current audio source, such as another app on the user’s Apple Watch or iPhone. For example, users can play and pause music from their Apple Watch’s Music app or control the volume of a podcast on their iPhone.

The system automatically selects the source. If the user is listening to audio on their watch or phone, the system selects that audio source. Otherwise, the system selects the most recently used source.

##### Add the View to Your Storyboard

To add the Now Playing view, drag it from the Library to an empty interface controller in your WatchKit app’s storyboard.

![A screenshot showing the Now Playing view inside an interface controller in the storyboard.](https://docs-assets.developer.apple.com/published/5daf416d20b998f9195e06c5815073ff/media-3377250%402x.png)

Always present the Now Playing view so that it fills the screen in a nonscrolling container. Don’t add any other elements to this scene.

> **Note**:  If you are using SwiftUI, use the [`NowPlayingView`](nowplayingview.md) structure instead.

 If you are using SwiftUI, use the [`NowPlayingView`](nowplayingview.md) structure instead.

The Now Playing view uses your app’s tint color, but otherwise has no attributes or properties that you can set. In addition, no public interface class exists for the Now Playing view. This means you can’t access or control the view programmatically. Your app just presents the view; the system handles the rest.

## See Also

- [Playing Background Audio](playing-background-audio.md)
  Enable background audio in your app to provide a seamless playback experience.
- [class WKInterfaceVolumeControl](wkinterfacevolumecontrol.md)
  An interface element that provides control of the audio volume from the watch or a paired iPhone.
- [PUICAutoLaunchAudioOptOut](https://developer.apple.com/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [class WKAudioFilePlayer](wkaudiofileplayer.md)
  An object that controls playback of a single audio item.
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md)
  An object that controls playback of one or more audio items.
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md)
  An object that manages the presentation state of an audio file while it is playing.
- [class WKAudioFileAsset](wkaudiofileasset.md)
  An object that stores a reference to an audio file and provides metadata information about that file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/adding-a-now-playing-view)*