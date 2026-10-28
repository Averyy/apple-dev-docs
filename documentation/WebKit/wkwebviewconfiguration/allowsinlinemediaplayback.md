# allowsInlineMediaPlayback

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether HTML5 videos play inline or use the native full-screen controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsInlineMediaPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsInlineMediaPlayback;
```

## Discussion

Set this property to [`true`](../../Swift/true.md) to play videos inline, or [`false`](../../Swift/false.md) to use the native full-screen controller. When adding a video element to an HTML document on iPhone, you must also include the `playsinline` attribute.

The default value of this property is [`false`](../../Swift/false.md) for iPhone and [`true`](../../Swift/true.md) for iPad.

> ❗ **Important**:  Apps created before iOS 10.0 must use the `webkit-playsinline` attribute.

## See Also

### Setting media playback preferences
- [var allowsAirPlayForMediaPlayback: Bool](./allowsairplayformediaplayback.md)
  A Boolean value that indicates whether the web view allows media playback over AirPlay.
- [var allowsPictureInPictureMediaPlayback: Bool](./allowspictureinpicturemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos can play Picture in Picture.
- [var mediaTypesRequiringUserActionForPlayback: WKAudiovisualMediaTypes](./mediatypesrequiringuseractionforplayback.md)
  The media types that require a user gesture to begin playing.
- [struct WKAudiovisualMediaTypes](../wkaudiovisualmediatypes.md)
  The media types that require a user gesture to begin playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/allowsinlinemediaplayback)*