# setCameraCaptureState(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Changes whether the webpage is using the camera to capture images or video.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final func setCameraCaptureState(_ state: WKMediaCaptureState) async
```

## Parameters

- `state`: The new capture state the page should use.

## See Also

### Managing the microphone and camera
- [var cameraCaptureState: WKMediaCaptureState](./cameracapturestate.md)
  Indicates whether the webpage is using the camera to capture images or video.
- [var microphoneCaptureState: WKMediaCaptureState](./microphonecapturestate.md)
  Indicates whether the webpage is using the microphone to capture audio.
- [func setMicrophoneCaptureState(WKMediaCaptureState) async](./setmicrophonecapturestate%28_%29.md)
  Changes whether the webpage is using the microphone to capture audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/setcameracapturestate(_:))*