# setMicrophoneCaptureState(_:)

**Framework**: WebKit  
**Kind**: method

Changes whether the webpage is using the microphone to capture audio.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final func setMicrophoneCaptureState(_ state: WKMediaCaptureState) async
```

## Parameters

- `state`: The new capture state the page should use.

## See Also

- [var cameraCaptureState: WKMediaCaptureState](webpage/cameracapturestate.md)
  Indicates whether the webpage is using the camera to capture images or video.
- [var microphoneCaptureState: WKMediaCaptureState](webpage/microphonecapturestate.md)
  Indicates whether the webpage is using the microphone to capture audio.
- [func setCameraCaptureState(WKMediaCaptureState) async](webpage/setcameracapturestate(_:).md)
  Changes whether the webpage is using the camera to capture images or video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/setmicrophonecapturestate(_:))*