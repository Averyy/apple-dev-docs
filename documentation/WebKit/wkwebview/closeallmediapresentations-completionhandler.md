# closeAllMediaPresentations(completionHandler:)

**Framework**: WebKit  
**Kind**: method

Closes all media the web view is presenting, including picture-in-picture video and fullscreen video.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func closeAllMediaPresentations() async
```

## Parameters

- `completionHandler`: A closure the system executes after it completes closing all media presentations.

## See Also

- [func pauseAllMediaPlayback(completionHandler: (() -> Void)?)](wkwebview/pauseallmediaplayback(completionhandler:).md)
  Pauses playback of all media in the web view.
- [func requestMediaPlaybackState(completionHandler: (WKMediaPlaybackState) -> Void)](wkwebview/requestmediaplaybackstate(completionhandler:).md)
  Requests the playback status of media in the web view.
- [func setAllMediaPlaybackSuspended(Bool, completionHandler: (() -> Void)?)](wkwebview/setallmediaplaybacksuspended(_:completionhandler:).md)
  Changes whether the webpage is suspending playback of all media in the page.
- [enum WKMediaPlaybackState](wkmediaplaybackstate.md)
  An enumeration that describes whether an audio or video presentation is playing, paused, or suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/closeallmediapresentations(completionhandler:))*