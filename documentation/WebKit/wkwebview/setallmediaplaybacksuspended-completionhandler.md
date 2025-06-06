# setAllMediaPlaybackSuspended(_:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Changes whether the webpage is suspending playback of all media in the page.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setAllMediaPlaybackSuspended(_ suspended: Bool) async
```

#### Discussion

Pass `true` to pause all media the web view is playing. Neither the user nor the webpage can resume playback until you call this method again with `false`.

## Parameters

- `suspended`: A Boolean value that indicates whether the webpage should suspend media playback.
- `completionHandler`: A closure the system executes after it completes changing the media playback suspension status.

## See Also

- [func pauseAllMediaPlayback(completionHandler: (() -> Void)?)](wkwebview/pauseallmediaplayback(completionhandler:).md)
  Pauses playback of all media in the web view.
- [func requestMediaPlaybackState(completionHandler: (WKMediaPlaybackState) -> Void)](wkwebview/requestmediaplaybackstate(completionhandler:).md)
  Requests the playback status of media in the web view.
- [func closeAllMediaPresentations(completionHandler: (() -> Void)?)](wkwebview/closeallmediapresentations(completionhandler:).md)
  Closes all media the web view is presenting, including picture-in-picture video and fullscreen video.
- [enum WKMediaPlaybackState](wkmediaplaybackstate.md)
  An enumeration that describes whether an audio or video presentation is playing, paused, or suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/setallmediaplaybacksuspended(_:completionhandler:))*