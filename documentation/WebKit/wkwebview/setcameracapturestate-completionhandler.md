# setCameraCaptureState(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Changes whether the webpage is using the camera to capture images or video.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setCameraCaptureState(_ state: WKMediaCaptureState) async
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setCameraCaptureState(_ state: WKMediaCaptureState) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `state`: An enumeration case that indicates whether the webpage should use the camera to capture images or video.
- `completionHandler`: A closure the system executes after changing whether the webpage is using the camera to capture images or video.

## See Also

- [var cameraCaptureState: WKMediaCaptureState](wkwebview/cameracapturestate.md)
  An enumeration case that indicates whether the webpage is using the camera to capture images or video.
- [var microphoneCaptureState: WKMediaCaptureState](wkwebview/microphonecapturestate.md)
  An enumeration case that indicates whether the webpage is using the microphone to capture audio.
- [func setMicrophoneCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](wkwebview/setmicrophonecapturestate(_:completionhandler:).md)
  Changes whether the webpage is using the microphone to capture audio.
- [enum WKMediaCaptureState](wkmediacapturestate.md)
  An enumeration that describes whether a media device, like a camera or microphone, is currently capturing audio or video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/setcameracapturestate(_:completionhandler:))*