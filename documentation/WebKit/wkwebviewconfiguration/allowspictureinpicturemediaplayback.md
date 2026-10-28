# allowsPictureInPictureMediaPlayback

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether HTML5 videos can play Picture in Picture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsPictureInPictureMediaPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsPictureInPictureMediaPlayback;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Setting media playback preferences
- [var allowsInlineMediaPlayback: Bool](./allowsinlinemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos play inline or use the native full-screen controller.
- [var allowsAirPlayForMediaPlayback: Bool](./allowsairplayformediaplayback.md)
  A Boolean value that indicates whether the web view allows media playback over AirPlay.
- [var mediaTypesRequiringUserActionForPlayback: WKAudiovisualMediaTypes](./mediatypesrequiringuseractionforplayback.md)
  The media types that require a user gesture to begin playing.
- [struct WKAudiovisualMediaTypes](../wkaudiovisualmediatypes.md)
  The media types that require a user gesture to begin playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/allowspictureinpicturemediaplayback)*