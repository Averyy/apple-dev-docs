# WKMediaPlaybackState

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that describes whether an audio or video presentation is playing, paused, or suspended.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
enum WKMediaPlaybackState
```

```c
enum WKMediaPlaybackState : NSInteger;
```

## Topics

### Constants
- [WKMediaPlaybackState.none](./wkmediaplaybackstate/none.md)
  There is no media to play back.
- [WKMediaPlaybackState.paused](./wkmediaplaybackstate/paused.md)
  The media playback is paused.
- [WKMediaPlaybackState.playing](./wkmediaplaybackstate/playing.md)
  The media is playing.
- [WKMediaPlaybackState.suspended](./wkmediaplaybackstate/suspended.md)
  The media is not playing, and cannot be resumed until the user revokes the suspension.
### Initializers
- [init?(rawValue: Int)](./wkmediaplaybackstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interacting with media
- [func pauseAllMediaPlayback(completionHandler: (() -> Void)?)](./wkwebview/pauseallmediaplayback%28completionhandler%29.md)
  Pauses playback of all media in the web view.
- [func requestMediaPlaybackState(completionHandler: (WKMediaPlaybackState) -> Void)](./wkwebview/requestmediaplaybackstate%28completionhandler%29.md)
  Requests the playback status of media in the web view.
- [func setAllMediaPlaybackSuspended(Bool, completionHandler: (() -> Void)?)](./wkwebview/setallmediaplaybacksuspended%28_,completionhandler%29.md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations(completionHandler: (() -> Void)?)](./wkwebview/closeallmediapresentations%28completionhandler%29.md)
  Closes all media the web view is presenting, including picture-in-picture video and fullscreen video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkmediaplaybackstate)*