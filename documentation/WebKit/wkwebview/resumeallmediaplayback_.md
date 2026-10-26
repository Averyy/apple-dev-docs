# resumeAllMediaPlayback:

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Resumes playback of all media in a web view.

**Availability**:
- iOS 14.5+ - Deprecated in 15.0
- iPadOS 14.5+ - Deprecated in 15.0
- Mac Catalyst 14.5+ - Deprecated in 15.0
- macOS 11.3+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```objc
- (void) resumeAllMediaPlayback:(void (^)(void)) completionHandler;
```

## See Also

### Interacting with media
- [func pauseAllMediaPlayback(completionHandler: (() -> Void)?)](./pauseallmediaplayback%28completionhandler%29.md)
  Pauses playback of all media in the web view.
- [- pauseAllMediaPlayback:](./pauseallmediaplayback_.md)
  Pauses playback of all media in the web view.
- [func requestMediaPlaybackState(completionHandler: (WKMediaPlaybackState) -> Void)](./requestmediaplaybackstate%28completionhandler%29.md)
  Requests the playback status of media in the web view.
- [- requestMediaPlaybackState:](./requestmediaplaybackstate_.md)
  Requests the playback status of media in the web view.
- [func setAllMediaPlaybackSuspended(Bool, completionHandler: (() -> Void)?)](./setallmediaplaybacksuspended%28_,completionhandler%29.md)
  Changes whether the webpage is suspending playback of all media in the page.
- [- suspendAllMediaPlayback:](./suspendallmediaplayback_.md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations(completionHandler: (() -> Void)?)](./closeallmediapresentations%28completionhandler%29.md)
  Closes all media the web view is presenting, including picture-in-picture video and fullscreen video.
- [enum WKMediaPlaybackState](../wkmediaplaybackstate.md)
  An enumeration that describes whether an audio or video presentation is playing, paused, or suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/resumeallmediaplayback:)*