# cameraCaptureState

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the webpage is using the camera to capture images or video.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var cameraCaptureState: WKMediaCaptureState { get }
```

## See Also

### Managing the microphone and camera
- [var microphoneCaptureState: WKMediaCaptureState](./microphonecapturestate.md)
  Indicates whether the webpage is using the microphone to capture audio.
- [func setCameraCaptureState(WKMediaCaptureState) async](./setcameracapturestate%28_%29.md)
  Changes whether the webpage is using the camera to capture images or video.
- [func setMicrophoneCaptureState(WKMediaCaptureState) async](./setmicrophonecapturestate%28_%29.md)
  Changes whether the webpage is using the microphone to capture audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/cameracapturestate)*