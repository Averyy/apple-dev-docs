# cameraCaptureState

**Framework**: WebKit  
**Kind**: property

Indicates whether the webpage is using the camera to capture images or video.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var cameraCaptureState: WKMediaCaptureState { get }
```

## See Also

- [var microphoneCaptureState: WKMediaCaptureState](webpage/microphonecapturestate.md)
  Indicates whether the webpage is using the microphone to capture audio.
- [func setCameraCaptureState(WKMediaCaptureState) async](webpage/setcameracapturestate(_:).md)
  Changes whether the webpage is using the camera to capture images or video.
- [func setMicrophoneCaptureState(WKMediaCaptureState) async](webpage/setmicrophonecapturestate(_:).md)
  Changes whether the webpage is using the microphone to capture audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/cameracapturestate)*