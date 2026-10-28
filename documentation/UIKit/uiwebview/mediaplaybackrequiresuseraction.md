# mediaPlaybackRequiresUserAction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them.

**Availability**:
- iOS 4.0+ - Deprecated in 12.0
- iPadOS 4.0+ - Deprecated in 12.0
- Mac Catalyst 4.0+ - Deprecated in 12.0

## Declaration

```swift
var mediaPlaybackRequiresUserAction: Bool { get set }
```

```objc
@property (nonatomic) BOOL mediaPlaybackRequiresUserAction;
```

## Discussion

The default value on both iPad and iPhone is [`true`](../../Swift/true.md). To make media play automatically when loaded, set this property to [`false`](../../Swift/false.md) and ensure the `<audio>` or `<video>` element you want to play has the `autoplay` attribute set.

## See Also

### Managing media playback
- [var allowsInlineMediaPlayback: Bool](./allowsinlinemediaplayback.md)
  A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller.
- [var mediaPlaybackAllowsAirPlay: Bool](./mediaplaybackallowsairplay.md)
  A Boolean value that determines whether Air Play is allowed from this view.
- [var allowsPictureInPictureMediaPlayback: Bool](./allowspictureinpicturemediaplayback.md)
  A Boolean value that determines whether Picture in Picture playback is allowed from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/mediaplaybackrequiresuseraction)*