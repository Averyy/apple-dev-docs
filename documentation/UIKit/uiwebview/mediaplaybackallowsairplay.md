# mediaPlaybackAllowsAirPlay

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether Air Play is allowed from this view.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- Mac Catalyst 5.0+ - Deprecated in 12.0

## Declaration

```swift
var mediaPlaybackAllowsAirPlay: Bool { get set }
```

```objc
@property (nonatomic) BOOL mediaPlaybackAllowsAirPlay;
```

## Discussion

The default value on both iPad and iPhone is [`true`](../../Swift/true.md).

## See Also

### Managing media playback
- [var allowsInlineMediaPlayback: Bool](./allowsinlinemediaplayback.md)
  A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller.
- [var mediaPlaybackRequiresUserAction: Bool](./mediaplaybackrequiresuseraction.md)
  A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them.
- [var allowsPictureInPictureMediaPlayback: Bool](./allowspictureinpicturemediaplayback.md)
  A Boolean value that determines whether Picture in Picture playback is allowed from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/mediaplaybackallowsairplay)*