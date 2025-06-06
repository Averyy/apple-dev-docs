# allowsInlineMediaPlayback

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+

## Declaration

```swift
@MainActor
var allowsInlineMediaPlayback: Bool { get set }
```

#### Discussion

You must set this property to play inline video. Set this property to `true` to play videos inline. Set this property to `false` to use the native full-screen controller. When adding a video element to a  HTML document on the iPhone, you must also include the `playsinline` attribute.

The default value for iPhone is `false` and the default value for iPad is `true`.

> ❗ **Important**:  Apps created before iOS 10.0 must use the `webkit-playsinline` attribute.

 Apps created before iOS 10.0 must use the `webkit-playsinline` attribute.

## See Also

- [var mediaPlaybackRequiresUserAction: Bool](uiwebview/mediaplaybackrequiresuseraction.md)
  A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them.
- [var mediaPlaybackAllowsAirPlay: Bool](uiwebview/mediaplaybackallowsairplay.md)
  A Boolean value that determines whether Air Play is allowed from this view.
- [var allowsPictureInPictureMediaPlayback: Bool](uiwebview/allowspictureinpicturemediaplayback.md)
  A Boolean value that determines whether Picture in Picture playback is allowed from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/allowsinlinemediaplayback)*