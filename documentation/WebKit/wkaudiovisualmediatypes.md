# WKAudiovisualMediaTypes

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

The media types that require a user gesture to begin playing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
struct WKAudiovisualMediaTypes
```

```c
enum WKAudiovisualMediaTypes : NSUInteger;
```

#### Overview

To indicate that no user gestures are required to play media, use an empty set of audio/visual media types, indicated by the empty array literal, `[]`. For example, `let myAudiovisualMediaType: WKAudiovisualMediaTypes = []`.

## Topics

### Media Types
- [static var audio: WKAudiovisualMediaTypes](./wkaudiovisualmediatypes/audio.md)
  Media types that contain audio require a user gesture to begin playing.
- [static var video: WKAudiovisualMediaTypes](./wkaudiovisualmediatypes/video.md)
  Media types that contain video require a user gesture to begin playing.
- [static var all: WKAudiovisualMediaTypes](./wkaudiovisualmediatypes/all.md)
  All media types require a user gesture to begin playing.
- [WKAudiovisualMediaTypeNone](./wkaudiovisualmediatypes/wkaudiovisualmediatypenone.md)
  No media types require a user gesture to begin playing.
### Initializers
- [init(rawValue: UInt)](./wkaudiovisualmediatypes/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Setting media playback preferences
- [var allowsInlineMediaPlayback: Bool](./wkwebviewconfiguration/allowsinlinemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos play inline or use the native full-screen controller.
- [var allowsAirPlayForMediaPlayback: Bool](./wkwebviewconfiguration/allowsairplayformediaplayback.md)
  A Boolean value that indicates whether the web view allows media playback over AirPlay.
- [var allowsPictureInPictureMediaPlayback: Bool](./wkwebviewconfiguration/allowspictureinpicturemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos can play Picture in Picture.
- [var mediaTypesRequiringUserActionForPlayback: WKAudiovisualMediaTypes](./wkwebviewconfiguration/mediatypesrequiringuseractionforplayback.md)
  The media types that require a user gesture to begin playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkaudiovisualmediatypes)*