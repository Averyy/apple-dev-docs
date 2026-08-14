# WKMediaCaptureType

**Framework**: WebKit  
**Kind**: enum

An enumeration listing the types of media devices that can capture audio, video, or both.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum WKMediaCaptureType
```

## Topics

### Constants
- [WKMediaCaptureType.camera](wkmediacapturetype/camera.md)
  A media device that can capture video.
- [WKMediaCaptureType.cameraAndMicrophone](wkmediacapturetype/cameraandmicrophone.md)
  A media device or devices that can capture audio and video.
- [WKMediaCaptureType.microphone](wkmediacapturetype/microphone.md)
  A media device that can capture audio.
### Initializers
- [init?(rawValue: Int)](wkmediacapturetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func webView(WKWebView, requestDeviceOrientationAndMotionPermissionFor: WKSecurityOrigin, initiatedByFrame: WKFrameInfo, decisionHandler: (WKPermissionDecision) -> Void)](wkuidelegate/webview(_:requestdeviceorientationandmotionpermissionfor:initiatedbyframe:decisionhandler:).md)
  Determines whether a web resource, which the security origin object describes, can access the device’s orientation and motion.
- [func webView(WKWebView, requestMediaCapturePermissionFor: WKSecurityOrigin, initiatedByFrame: WKFrameInfo, type: WKMediaCaptureType, decisionHandler: (WKPermissionDecision) -> Void)](wkuidelegate/webview(_:requestmediacapturepermissionfor:initiatedbyframe:type:decisionhandler:).md)
  Determines whether a web resource, which the security origin object describes, can access to the device’s microphone audio and camera video.
- [enum WKPermissionDecision](wkpermissiondecision.md)
  An enumeration of possible permission decisions for device resource access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkmediacapturetype)*