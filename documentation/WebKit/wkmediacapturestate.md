# WKMediaCaptureState

**Framework**: Webkit  
**Kind**: enum

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

## Topics

### Constants
- [WKMediaCaptureState.active](wkmediacapturestate/active.md)
  The media device is actively capturing audio or video.
- [WKMediaCaptureState.muted](wkmediacapturestate/muted.md)
  The media device is muted, and not actively capturing audio or video.
- [WKMediaCaptureState.none](wkmediacapturestate/none.md)
  The media device is off.
### Initializers
- [init?(rawValue: Int)](wkmediacapturestate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var cameraCaptureState: WKMediaCaptureState](wkwebview/cameracapturestate.md)
  An enumeration case that indicates whether the webpage is using the camera to capture images or video.
- [var microphoneCaptureState: WKMediaCaptureState](wkwebview/microphonecapturestate.md)
  An enumeration case that indicates whether the webpage is using the microphone to capture audio.
- [func setCameraCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](wkwebview/setcameracapturestate(_:completionhandler:).md)
  Changes whether the webpage is using the camera to capture images or video.
- [func setMicrophoneCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](wkwebview/setmicrophonecapturestate(_:completionhandler:).md)
  Changes whether the webpage is using the microphone to capture audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkmediacapturestate)*