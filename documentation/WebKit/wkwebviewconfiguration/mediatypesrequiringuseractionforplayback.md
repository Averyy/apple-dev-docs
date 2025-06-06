# mediaTypesRequiringUserActionForPlayback

**Framework**: Webkit  
**Kind**: property

The media types that require a user gesture to begin playing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var mediaTypesRequiringUserActionForPlayback: WKAudiovisualMediaTypes { get set }
```

#### Discussion

Use [`WKAudiovisualMediaTypeNone`](wkaudiovisualmediatypes/wkaudiovisualmediatypenone.md) to indicate that no user gestures are required to begin playing media.

## See Also

- [var allowsInlineMediaPlayback: Bool](wkwebviewconfiguration/allowsinlinemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos play inline or use the native full-screen controller.
- [var allowsAirPlayForMediaPlayback: Bool](wkwebviewconfiguration/allowsairplayformediaplayback.md)
  A Boolean value that indicates whether the web view allows media playback over AirPlay.
- [var allowsPictureInPictureMediaPlayback: Bool](wkwebviewconfiguration/allowspictureinpicturemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos can play Picture in Picture.
- [struct WKAudiovisualMediaTypes](wkaudiovisualmediatypes.md)
  The media types that require a user gesture to begin playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/mediatypesrequiringuseractionforplayback)*