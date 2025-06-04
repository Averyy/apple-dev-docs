# Adding a Now Playing View

**Framework**: Watchkit

Provide a view that controls the currently playing audio from your app.

## Overview

With a Now Playing view, users can control current or recently played audio without leaving your app. When your app presents the Now Playing view, it immediately displays information about the current audio source, such as another app on the user’s Apple Watch or iPhone. For example, users can play and pause music from their Apple Watch’s Music app or control the volume of a podcast on their iPhone.

The system automatically selects the source. If the user is listening to audio on their watch or phone, the system selects that audio source. Otherwise, the system selects the most recently used source.

To add the Now Playing view, drag it from the Library to an empty interface controller in your WatchKit app’s storyboard.

Always present the Now Playing view so that it fills the screen in a nonscrolling container. Don’t add any other elements to this scene.

> **Note**:  If you are using SwiftUI, use the [`NowPlayingView`](https://developer.apple.com/documentation/watchkit/nowplayingview) structure instead.

 If you are using SwiftUI, use the [`NowPlayingView`](https://developer.apple.com/documentation/watchkit/nowplayingview) structure instead.

The Now Playing view uses your app’s tint color, but otherwise has no attributes or properties that you can set. In addition, no public interface class exists for the Now Playing view. This means you can’t access or control the view programmatically. Your app just presents the view; the system handles the rest.

## See Also

- [Playing Background Audio](playing-background-audio.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/playing-background-audio))
- [class WKInterfaceVolumeControl](wkinterfacevolumecontrol.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol))
- PUICAutoLaunchAudioOptOut ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut))
- [class WKAudioFilePlayer](wkaudiofileplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer))
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer))
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem))
- [class WKAudioFileAsset](wkaudiofileasset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/adding-a-now-playing-view)*