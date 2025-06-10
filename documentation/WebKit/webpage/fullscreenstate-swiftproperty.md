# fullscreenState

**Framework**: WebKit  
**Kind**: property

The fullscreen state the page is currently in.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final var fullscreenState: WebPage.FullscreenState { get }
```

## See Also

- [WebPage.FullscreenState](webpage/fullscreenstate-swift.enum.md)
  The set of possible fullscreen states a webpage may be in.
- [func pauseAllMediaPlayback() async](webpage/pauseallmediaplayback.md)
  Pauses playback of all media in the web view.
- [func mediaPlaybackState() async -> WKMediaPlaybackState](webpage/mediaplaybackstate.md)
  Determine the playback status of media in the page.
- [func setAllMediaPlaybackSuspended(Bool) async](webpage/setallmediaplaybacksuspended(_:).md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations() async](webpage/closeallmediapresentations.md)
  Closes all media the webpage is presenting, including picture-in-picture video and fullscreen video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/fullscreenstate-swift.property)*