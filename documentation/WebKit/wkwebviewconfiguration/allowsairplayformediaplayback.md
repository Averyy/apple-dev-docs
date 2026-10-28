# allowsAirPlayForMediaPlayback

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the web view allows media playback over AirPlay.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var allowsAirPlayForMediaPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsAirPlayForMediaPlayback;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Setting media playback preferences
- [var allowsInlineMediaPlayback: Bool](./allowsinlinemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos play inline or use the native full-screen controller.
- [var allowsPictureInPictureMediaPlayback: Bool](./allowspictureinpicturemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos can play Picture in Picture.
- [var mediaTypesRequiringUserActionForPlayback: WKAudiovisualMediaTypes](./mediatypesrequiringuseractionforplayback.md)
  The media types that require a user gesture to begin playing.
- [struct WKAudiovisualMediaTypes](../wkaudiovisualmediatypes.md)
  The media types that require a user gesture to begin playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/allowsairplayformediaplayback)*