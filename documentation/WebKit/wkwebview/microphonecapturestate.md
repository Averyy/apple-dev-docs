# microphoneCaptureState

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

An enumeration case that indicates whether the webpage is using the microphone to capture audio.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var microphoneCaptureState: WKMediaCaptureState { get }
```

```objc
@property (nonatomic, readonly) WKMediaCaptureState microphoneCaptureState;
```

## See Also

### Managing the microphone and camera
- [var cameraCaptureState: WKMediaCaptureState](./cameracapturestate.md)
  An enumeration case that indicates whether the webpage is using the camera to capture images or video.
- [func setCameraCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](./setcameracapturestate%28_,completionhandler%29.md)
  Changes whether the webpage is using the camera to capture images or video.
- [func setMicrophoneCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](./setmicrophonecapturestate%28_,completionhandler%29.md)
  Changes whether the webpage is using the microphone to capture audio.
- [enum WKMediaCaptureState](../wkmediacapturestate.md)
  An enumeration that describes whether a media device, like a camera or microphone, is currently capturing audio or video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/microphonecapturestate)*