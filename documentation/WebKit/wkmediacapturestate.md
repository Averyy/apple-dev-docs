# WKMediaCaptureState

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that describes whether a media device, like a camera or microphone, is currently capturing audio or video.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum WKMediaCaptureState
```

```c
enum WKMediaCaptureState : NSInteger;
```

## Topics

### Constants
- [WKMediaCaptureState.active](./wkmediacapturestate/active.md)
  The media device is actively capturing audio or video.
- [WKMediaCaptureState.muted](./wkmediacapturestate/muted.md)
  The media device is muted, and not actively capturing audio or video.
- [WKMediaCaptureState.none](./wkmediacapturestate/none.md)
  The media device is off.
### Initializers
- [init?(rawValue: Int)](./wkmediacapturestate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing the microphone and camera
- [var cameraCaptureState: WKMediaCaptureState](./wkwebview/cameracapturestate.md)
  An enumeration case that indicates whether the webpage is using the camera to capture images or video.
- [var microphoneCaptureState: WKMediaCaptureState](./wkwebview/microphonecapturestate.md)
  An enumeration case that indicates whether the webpage is using the microphone to capture audio.
- [func setCameraCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](./wkwebview/setcameracapturestate%28_,completionhandler%29.md)
  Changes whether the webpage is using the camera to capture images or video.
- [func setMicrophoneCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](./wkwebview/setmicrophonecapturestate%28_,completionhandler%29.md)
  Changes whether the webpage is using the microphone to capture audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkmediacapturestate)*