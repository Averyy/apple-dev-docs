# requestMediaPlaybackState(completionHandler:)

**Framework**: WebKit  
**Kind**: method

Requests the playback status of media in the web view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func requestMediaPlaybackState() async -> WKMediaPlaybackState
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func requestMediaPlaybackState() async -> WKMediaPlaybackState
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: A closure the system executes after the web view determines the current state of media playback.

## See Also

- [func pauseAllMediaPlayback(completionHandler: (() -> Void)?)](wkwebview/pauseallmediaplayback(completionhandler:).md)
  Pauses playback of all media in the web view.
- [func setAllMediaPlaybackSuspended(Bool, completionHandler: (() -> Void)?)](wkwebview/setallmediaplaybacksuspended(_:completionhandler:).md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations(completionHandler: (() -> Void)?)](wkwebview/closeallmediapresentations(completionhandler:).md)
  Closes all media the web view is presenting, including picture-in-picture video and fullscreen video.
- [enum WKMediaPlaybackState](wkmediaplaybackstate.md)
  An enumeration that describes whether an audio or video presentation is playing, paused, or suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/requestmediaplaybackstate(completionhandler:))*