# microphoneCaptureState

**Framework**: WebKit  
**Kind**: property

Indicates whether the webpage is using the microphone to capture audio.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final var microphoneCaptureState: WKMediaCaptureState { get }
```

## See Also

- [var cameraCaptureState: WKMediaCaptureState](webpage/cameracapturestate.md)
  Indicates whether the webpage is using the camera to capture images or video.
- [func setCameraCaptureState(WKMediaCaptureState) async](webpage/setcameracapturestate(_:).md)
  Changes whether the webpage is using the camera to capture images or video.
- [func setMicrophoneCaptureState(WKMediaCaptureState) async](webpage/setmicrophonecapturestate(_:).md)
  Changes whether the webpage is using the microphone to capture audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/microphonecapturestate)*