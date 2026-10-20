# setCameraCaptureState(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Changes whether the webpage is using the camera to capture images or video.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func setCameraCaptureState(_ state: WKMediaCaptureState, completionHandler: (@MainActor @Sendable () -> Void)? = nil)
```

```swift
func setCameraCaptureState(_ state: WKMediaCaptureState) async
```

```objc
- (void) setCameraCaptureState:(WKMediaCaptureState) state completionHandler:(void (^)(void)) completionHandler;
```

## Parameters

- `state`: An enumeration case that indicates whether the webpage should use the camera to capture images or video.
- `completionHandler`: A closure the system executes after changing whether the webpage is using the camera to capture images or video.

## See Also

### Managing the microphone and camera
- [var cameraCaptureState: WKMediaCaptureState](./cameracapturestate.md)
  An enumeration case that indicates whether the webpage is using the camera to capture images or video.
- [var microphoneCaptureState: WKMediaCaptureState](./microphonecapturestate.md)
  An enumeration case that indicates whether the webpage is using the microphone to capture audio.
- [func setMicrophoneCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](./setmicrophonecapturestate%28_,completionhandler%29.md)
  Changes whether the webpage is using the microphone to capture audio.
- [enum WKMediaCaptureState](../wkmediacapturestate.md)
  An enumeration that describes whether a media device, like a camera or microphone, is currently capturing audio or video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/setcameracapturestate(_:completionhandler:))*