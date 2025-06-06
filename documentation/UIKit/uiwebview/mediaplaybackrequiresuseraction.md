# mediaPlaybackRequiresUserAction

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+

## Declaration

```swift
@MainActor
var mediaPlaybackRequiresUserAction: Bool { get set }
```

#### Discussion

The default value on both iPad and iPhone is [`true`](https://developer.apple.com/documentation/swift/true). To make media play automatically when loaded, set this property to [`false`](https://developer.apple.com/documentation/swift/false) and ensure the `<audio>` or `<video>` element you want to play has the `autoplay` attribute set.

## See Also

- [var allowsInlineMediaPlayback: Bool](uiwebview/allowsinlinemediaplayback.md)
  A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller.
- [var mediaPlaybackAllowsAirPlay: Bool](uiwebview/mediaplaybackallowsairplay.md)
  A Boolean value that determines whether Air Play is allowed from this view.
- [var allowsPictureInPictureMediaPlayback: Bool](uiwebview/allowspictureinpicturemediaplayback.md)
  A Boolean value that determines whether Picture in Picture playback is allowed from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/mediaplaybackrequiresuseraction)*