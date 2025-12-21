# allowsInlineMediaPlayback

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether HTML5 videos play inline or use the native full-screen controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsInlineMediaPlayback: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to play videos inline, or [`false`](https://developer.apple.com/documentation/Swift/false) to use the native full-screen controller. When adding a video element to an HTML document on iPhone, you must also include the `playsinline` attribute.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) for iPhone and [`true`](https://developer.apple.com/documentation/Swift/true) for iPad.

> ❗ **Important**:  Apps created before iOS 10.0 must use the `webkit-playsinline` attribute.

## See Also

- [var allowsAirPlayForMediaPlayback: Bool](wkwebviewconfiguration/allowsairplayformediaplayback.md)
  A Boolean value that indicates whether the web view allows media playback over AirPlay.
- [var allowsPictureInPictureMediaPlayback: Bool](wkwebviewconfiguration/allowspictureinpicturemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos can play Picture in Picture.
- [var mediaTypesRequiringUserActionForPlayback: WKAudiovisualMediaTypes](wkwebviewconfiguration/mediatypesrequiringuseractionforplayback.md)
  The media types that require a user gesture to begin playing.
- [struct WKAudiovisualMediaTypes](wkaudiovisualmediatypes.md)
  The media types that require a user gesture to begin playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/allowsinlinemediaplayback)*