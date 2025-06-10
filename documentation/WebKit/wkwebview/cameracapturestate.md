# cameraCaptureState

**Framework**: WebKit  
**Kind**: property

An enumeration case that indicates whether the webpage is using the camera to capture images or video.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var cameraCaptureState: WKMediaCaptureState { get }
```

## See Also

- [var microphoneCaptureState: WKMediaCaptureState](wkwebview/microphonecapturestate.md)
  An enumeration case that indicates whether the webpage is using the microphone to capture audio.
- [func setCameraCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](wkwebview/setcameracapturestate(_:completionhandler:).md)
  Changes whether the webpage is using the camera to capture images or video.
- [func setMicrophoneCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](wkwebview/setmicrophonecapturestate(_:completionhandler:).md)
  Changes whether the webpage is using the microphone to capture audio.
- [enum WKMediaCaptureState](wkmediacapturestate.md)
  An enumeration that describes whether a media device, like a camera or microphone, is currently capturing audio or video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/cameracapturestate)*