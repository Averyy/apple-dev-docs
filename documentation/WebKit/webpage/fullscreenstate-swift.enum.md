# WebPage.FullscreenState

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

The set of possible fullscreen states a webpage may be in.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum FullscreenState
```

## Topics

### Enumeration Cases
- [WebPage.FullscreenState.enteringFullscreen](./fullscreenstate-swift.enum/enteringfullscreen.md)
  The page is entering fullscreen.
- [WebPage.FullscreenState.exitingFullscreen](./fullscreenstate-swift.enum/exitingfullscreen.md)
  The page is exiting fullscreen.
- [WebPage.FullscreenState.inFullscreen](./fullscreenstate-swift.enum/infullscreen.md)
  The page is currently in fullscreen.
- [WebPage.FullscreenState.notInFullscreen](./fullscreenstate-swift.enum/notinfullscreen.md)
  The page is not currently in fullscreen.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Interacting with media
- [func pauseAllMediaPlayback() async](./pauseallmediaplayback%28%29.md)
  Pauses playback of all media in the web view.
- [func mediaPlaybackState() async -> WKMediaPlaybackState](./mediaplaybackstate%28%29.md)
  Determine the playback status of media in the page.
- [func setAllMediaPlaybackSuspended(Bool) async](./setallmediaplaybacksuspended%28_%29.md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations() async](./closeallmediapresentations%28%29.md)
  Closes all media the webpage is presenting, including picture-in-picture video and fullscreen video.
- [var fullscreenState: WebPage.FullscreenState](./fullscreenstate-swift.property.md)
  The fullscreen state the page is currently in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/fullscreenstate-swift.enum)*