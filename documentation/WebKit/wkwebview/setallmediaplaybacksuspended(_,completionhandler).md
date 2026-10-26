# setAllMediaPlaybackSuspended(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Changes whether the webpage is suspending playback of all media in the page.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func setAllMediaPlaybackSuspended(_ suspended: Bool, completionHandler: (@MainActor @Sendable () -> Void)? = nil)
```

```swift
func setAllMediaPlaybackSuspended(_ suspended: Bool) async
```

```objc
- (void) setAllMediaPlaybackSuspended:(BOOL) suspended completionHandler:(void (^)(void)) completionHandler;
```

#### Discussion

Pass `true` to pause all media the web view is playing. Neither the user nor the webpage can resume playback until you call this method again with `false`.

## Parameters

- `suspended`: A Boolean value that indicates whether the webpage should suspend media playback.
- `completionHandler`: A closure the system executes after it completes changing the media playback suspension status.

## See Also

### Interacting with media
- [func pauseAllMediaPlayback(completionHandler: (() -> Void)?)](./pauseallmediaplayback%28completionhandler%29.md)
  Pauses playback of all media in the web view.
- [func requestMediaPlaybackState(completionHandler: (WKMediaPlaybackState) -> Void)](./requestmediaplaybackstate%28completionhandler%29.md)
  Requests the playback status of media in the web view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/setallmediaplaybacksuspended(_:completionhandler:))*