# closeAllMediaPresentations()

**Framework**: WebKit  
**Kind**: method

Closes all media the webpage is presenting, including picture-in-picture video and fullscreen video.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final func closeAllMediaPresentations() async
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
- [var fullscreenState: WebPage.FullscreenState](webpage/fullscreenstate-swift.property.md)
  The fullscreen state the page is currently in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/closeallmediapresentations())*