# webView(_:requestMediaCapturePermissionFor:initiatedByFrame:type:decisionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Determines whether a web resource, which the security origin object describes, can access to the device’s microphone audio and camera video.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, requestMediaCapturePermissionFor origin: WKSecurityOrigin, initiatedByFrame frame: WKFrameInfo, type: WKMediaCaptureType, decisionHandler: @escaping @MainActor @Sendable (WKPermissionDecision) -> Void)
```

```swift
optional func webView(_ webView: WKWebView, decideMediaCapturePermissionsFor origin: WKSecurityOrigin, initiatedBy frame: WKFrameInfo, type: WKMediaCaptureType) async -> WKPermissionDecision
```

```objc
- (void) webView:(WKWebView *) webView requestMediaCapturePermissionForOrigin:(WKSecurityOrigin *) origin initiatedByFrame:(WKFrameInfo *) frame type:(WKMediaCaptureType) type decisionHandler:(void (^)(enum WKPermissionDecision)) decisionHandler;
```

## Discussion

If you don’t implement this method in your delegate, the system returns [`WKPermissionDecision.prompt`](../wkpermissiondecision/prompt.md).

## Parameters

- `webView`: The web view requesting permission for microphone audio and camera video.
- `origin`: An object that identifies the host name, protocol, and port number for a web resource.
- `frame`: The frame that initiates the request in the web view.
- `type`: An enumeration case representing a type of media capture device, like a microphone or camera.
- `decisionHandler`: A closure that you call from your delegate method. Pass the permission decision you determine to the closure.

## See Also

### Requesting permissions
- [func webView(WKWebView, requestDeviceOrientationAndMotionPermissionFor: WKSecurityOrigin, initiatedByFrame: WKFrameInfo, decisionHandler: (WKPermissionDecision) -> Void)](./webview%28_,requestdeviceorientationandmotionpermissionfor,initiatedbyframe,decisionhandler%29.md)
  Determines whether a web resource, which the security origin object describes, can access the device’s orientation and motion.
- [enum WKPermissionDecision](../wkpermissiondecision.md)
  An enumeration of possible permission decisions for device resource access.
- [enum WKMediaCaptureType](../wkmediacapturetype.md)
  An enumeration listing the types of media devices that can capture audio, video, or both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:requestmediacapturepermissionfor:initiatedbyframe:type:decisionhandler:))*