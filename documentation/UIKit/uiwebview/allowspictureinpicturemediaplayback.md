# allowsPictureInPictureMediaPlayback

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether Picture in Picture playback is allowed from this view.

**Availability**:
- iOS 9.0+ - Deprecated in 12.0
- iPadOS 9.0+ - Deprecated in 12.0
- Mac Catalyst 9.0+ - Deprecated in 12.0

## Declaration

```swift
var allowsPictureInPictureMediaPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsPictureInPictureMediaPlayback;
```

#### Discussion

The default value is [`true`](../../Swift/true.md) on devices that support Picture in Picture (PiP) mode and [`false`](../../Swift/false.md) on all other devices.

## See Also

### Managing media playback
- [var allowsInlineMediaPlayback: Bool](./allowsinlinemediaplayback.md)
  A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller.
- [var mediaPlaybackRequiresUserAction: Bool](./mediaplaybackrequiresuseraction.md)
  A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them.
- [var mediaPlaybackAllowsAirPlay: Bool](./mediaplaybackallowsairplay.md)
  A Boolean value that determines whether Air Play is allowed from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/allowspictureinpicturemediaplayback)*