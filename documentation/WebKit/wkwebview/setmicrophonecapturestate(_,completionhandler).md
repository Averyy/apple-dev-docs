# setMicrophoneCaptureState(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Changes whether the webpage is using the microphone to capture audio.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func setMicrophoneCaptureState(_ state: WKMediaCaptureState, completionHandler: (@MainActor @Sendable () -> Void)? = nil)
```

```swift
func setMicrophoneCaptureState(_ state: WKMediaCaptureState) async
```

```objc
- (void) setMicrophoneCaptureState:(WKMediaCaptureState) state completionHandler:(void (^)(void)) completionHandler;
```

## Parameters

- `state`: An enumeration case that indicates whether the webpage should use the microphone to capture audio.
- `completionHandler`: A closure the system executes after changing whether the webpage is using the microphone to capture audio.

## See Also

### Managing the microphone and camera
- [var cameraCaptureState: WKMediaCaptureState](./cameracapturestate.md)
  An enumeration case that indicates whether the webpage is using the camera to capture images or video.
- [var microphoneCaptureState: WKMediaCaptureState](./microphonecapturestate.md)
  An enumeration case that indicates whether the webpage is using the microphone to capture audio.
- [func setCameraCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](./setcameracapturestate%28_,completionhandler%29.md)
  Changes whether the webpage is using the camera to capture images or video.
- [enum WKMediaCaptureState](../wkmediacapturestate.md)
  An enumeration that describes whether a media device, like a camera or microphone, is currently capturing audio or video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/setmicrophonecapturestate(_:completionhandler:))*