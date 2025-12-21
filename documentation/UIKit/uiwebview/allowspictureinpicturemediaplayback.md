# allowsPictureInPictureMediaPlayback

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether Picture in Picture playback is allowed from this view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

## Declaration

```swift
@MainActor
var allowsPictureInPictureMediaPlayback: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true) on devices that support Picture in Picture (PiP) mode and [`false`](https://developer.apple.com/documentation/Swift/false) on all other devices.

## See Also

- [var allowsInlineMediaPlayback: Bool](uiwebview/allowsinlinemediaplayback.md)
  A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller.
- [var mediaPlaybackRequiresUserAction: Bool](uiwebview/mediaplaybackrequiresuseraction.md)
  A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them.
- [var mediaPlaybackAllowsAirPlay: Bool](uiwebview/mediaplaybackallowsairplay.md)
  A Boolean value that determines whether Air Play is allowed from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/allowspictureinpicturemediaplayback)*