# webView(_:requestDeviceOrientationAndMotionPermissionFor:initiatedByFrame:decisionHandler:)

**Framework**: WebKit  
**Kind**: method

Determines whether a web resource, which the security origin object describes, can access the device’s orientation and motion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, requestDeviceOrientationAndMotionPermissionFor origin: WKSecurityOrigin, initiatedByFrame frame: WKFrameInfo, decisionHandler: @escaping @MainActor (WKPermissionDecision) -> Void)
```

#### Discussion

If you don’t implement this method in your delegate, the system returns [`WKPermissionDecision.prompt`](wkpermissiondecision/prompt.md).

## Parameters

- `webView`: The web view requesting permission for orientation and motion information.
- `origin`: An object that identifies the host name, protocol, and port number for a web resource.
- `frame`: The frame that initiates the request in the web view.
- `decisionHandler`: A closure that you call from your delegate method. Pass the permission decision you determine to the closure.

## See Also

- [func webView(WKWebView, requestMediaCapturePermissionFor: WKSecurityOrigin, initiatedByFrame: WKFrameInfo, type: WKMediaCaptureType, decisionHandler: (WKPermissionDecision) -> Void)](wkuidelegate/webview(_:requestmediacapturepermissionfor:initiatedbyframe:type:decisionhandler:).md)
  Determines whether a web resource, which the security origin object describes, can access to the device’s microphone audio and camera video.
- [enum WKPermissionDecision](wkpermissiondecision.md)
  An enumeration of possible permission decisions for device resource access.
- [enum WKMediaCaptureType](wkmediacapturetype.md)
  An enumeration listing the types of media devices that can capture audio, video, or both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:requestdeviceorientationandmotionpermissionfor:initiatedbyframe:decisionhandler:))*