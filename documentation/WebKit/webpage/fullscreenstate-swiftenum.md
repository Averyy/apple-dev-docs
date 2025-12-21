# WebPage.FullscreenState

**Framework**: WebKit  
**Kind**: enum

The set of possible fullscreen states a webpage may be in.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum FullscreenState
```

## Topics

### Enumeration Cases
- [WebPage.FullscreenState.enteringFullscreen](webpage/fullscreenstate-swift.enum/enteringfullscreen.md)
  The page is entering fullscreen.
- [WebPage.FullscreenState.exitingFullscreen](webpage/fullscreenstate-swift.enum/exitingfullscreen.md)
  The page is exiting fullscreen.
- [WebPage.FullscreenState.inFullscreen](webpage/fullscreenstate-swift.enum/infullscreen.md)
  The page is currently in fullscreen.
- [WebPage.FullscreenState.notInFullscreen](webpage/fullscreenstate-swift.enum/notinfullscreen.md)
  The page is not currently in fullscreen.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func pauseAllMediaPlayback() async](webpage/pauseallmediaplayback.md)
  Pauses playback of all media in the web view.
- [func mediaPlaybackState() async -> WKMediaPlaybackState](webpage/mediaplaybackstate.md)
  Determine the playback status of media in the page.
- [func setAllMediaPlaybackSuspended(Bool) async](webpage/setallmediaplaybacksuspended(_:).md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations() async](webpage/closeallmediapresentations.md)
  Closes all media the webpage is presenting, including picture-in-picture video and fullscreen video.
- [var fullscreenState: WebPage.FullscreenState](webpage/fullscreenstate-swift.property.md)
  The fullscreen state the page is currently in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/fullscreenstate-swift.enum)*