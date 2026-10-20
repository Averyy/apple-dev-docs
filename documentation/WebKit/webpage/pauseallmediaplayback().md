# pauseAllMediaPlayback()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Pauses playback of all media in the web view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final func pauseAllMediaPlayback() async
```

## See Also

### Interacting with media
- [WebPage.FullscreenState](./fullscreenstate-swift.enum.md)
  The set of possible fullscreen states a webpage may be in.
- [func mediaPlaybackState() async -> WKMediaPlaybackState](./mediaplaybackstate%28%29.md)
  Determine the playback status of media in the page.
- [func setAllMediaPlaybackSuspended(Bool) async](./setallmediaplaybacksuspended%28_%29.md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations() async](./closeallmediapresentations%28%29.md)
  Closes all media the webpage is presenting, including picture-in-picture video and fullscreen video.
- [var fullscreenState: WebPage.FullscreenState](./fullscreenstate-swift.property.md)
  The fullscreen state the page is currently in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/pauseallmediaplayback())*