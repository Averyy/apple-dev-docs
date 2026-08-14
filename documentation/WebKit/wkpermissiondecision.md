# WKPermissionDecision

**Framework**: WebKit  
**Kind**: enum

An enumeration of possible permission decisions for device resource access.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum WKPermissionDecision
```

## Topics

### Constants
- [WKPermissionDecision.deny](wkpermissiondecision/deny.md)
  Deny permission for the requested resource.
- [WKPermissionDecision.grant](wkpermissiondecision/grant.md)
  Grant permission for the requested resource.
- [WKPermissionDecision.prompt](wkpermissiondecision/prompt.md)
  Prompt the user for permission for the requested resource.
### Initializers
- [init?(rawValue: Int)](wkpermissiondecision/init(rawvalue:).md)

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
- [enum WKMediaCaptureType](wkmediacapturetype.md)
  An enumeration listing the types of media devices that can capture audio, video, or both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpermissiondecision)*