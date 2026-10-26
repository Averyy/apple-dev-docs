# closeAllMediaPresentations(completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Closes all media the web view is presenting, including picture-in-picture video and fullscreen video.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func closeAllMediaPresentations(completionHandler: (@MainActor @Sendable () -> Void)? = nil)
```

```swift
func closeAllMediaPresentations() async
```

```objc
- (void) closeAllMediaPresentationsWithCompletionHandler:(void (^)(void)) completionHandler;
```

## Parameters

- `completionHandler`: A closure the system executes after it completes closing all media presentations.

## See Also

### Interacting with media
- [func pauseAllMediaPlayback(completionHandler: (() -> Void)?)](./pauseallmediaplayback%28completionhandler%29.md)
  Pauses playback of all media in the web view.
- [func requestMediaPlaybackState(completionHandler: (WKMediaPlaybackState) -> Void)](./requestmediaplaybackstate%28completionhandler%29.md)
  Requests the playback status of media in the web view.
- [func setAllMediaPlaybackSuspended(Bool, completionHandler: (() -> Void)?)](./setallmediaplaybacksuspended%28_,completionhandler%29.md)
  Changes whether the webpage is suspending playback of all media in the page.
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/closeallmediapresentations(completionhandler:))*