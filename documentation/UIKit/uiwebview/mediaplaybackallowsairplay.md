# mediaPlaybackAllowsAirPlay

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether Air Play is allowed from this view.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+

## Declaration

```swift
@MainActor
var mediaPlaybackAllowsAirPlay: Bool { get set }
```

#### Discussion

The default value on both iPad and iPhone is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var allowsInlineMediaPlayback: Bool](uiwebview/allowsinlinemediaplayback.md)
  A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller.
- [var mediaPlaybackRequiresUserAction: Bool](uiwebview/mediaplaybackrequiresuseraction.md)
  A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them.
- [var allowsPictureInPictureMediaPlayback: Bool](uiwebview/allowspictureinpicturemediaplayback.md)
  A Boolean value that determines whether Picture in Picture playback is allowed from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/mediaplaybackallowsairplay)*