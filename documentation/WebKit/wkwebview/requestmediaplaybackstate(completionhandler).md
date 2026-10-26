# requestMediaPlaybackState(completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Requests the playback status of media in the web view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func requestMediaPlaybackState(completionHandler: @escaping @MainActor @Sendable (WKMediaPlaybackState) -> Void)
```

```swift
func requestMediaPlaybackState() async -> WKMediaPlaybackState
```

```objc
- (void) requestMediaPlaybackStateWithCompletionHandler:(void (^)(enum WKMediaPlaybackState)) completionHandler;
```

## Parameters

- `completionHandler`: A closure the system executes after the web view determines the current state of media playback.

## See Also

### Interacting with media
- [func pauseAllMediaPlayback(completionHandler: (() -> Void)?)](./pauseallmediaplayback%28completionhandler%29.md)
  Pauses playback of all media in the web view.
- [func setAllMediaPlaybackSuspended(Bool, completionHandler: (() -> Void)?)](./setallmediaplaybacksuspended%28_,completionhandler%29.md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations(completionHandler: (() -> Void)?)](./closeallmediapresentations%28completionhandler%29.md)
  Closes all media the web view is presenting, including picture-in-picture video and fullscreen video.
- [enum WKMediaPlaybackState](../wkmediaplaybackstate.md)
  An enumeration that describes whether an audio or video presentation is playing, paused, or suspended.
- [- pauseAllMediaPlayback:](./pauseallmediaplayback_.md)
  Pauses playback of all media in the web view.
- [- requestMediaPlaybackState:](./requestmediaplaybackstate_.md)
  Requests the playback status of media in the web view.
- [- suspendAllMediaPlayback:](./suspendallmediaplayback_.md)
  Changes whether the webpage is suspending playback of all media in the page.
- [- resumeAllMediaPlayback:](./resumeallmediaplayback_.md)
  Resumes playback of all media in a web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/requestmediaplaybackstate(completionhandler:))*