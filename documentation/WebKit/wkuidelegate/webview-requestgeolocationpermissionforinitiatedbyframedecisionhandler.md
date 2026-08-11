# webView(_:requestGeolocationPermissionFor:initiatedByFrame:decisionHandler:)

**Framework**: WebKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
optional func webView(_ webView: WKWebView, requestGeolocationPermissionFor origin: WKSecurityOrigin, initiatedBy frame: WKFrameInfo) async -> WKPermissionDecision
```

#### Discussion

Allows your app to determine whether or not the given security origin should have access to geolocation APIs.

## Parameters

- `frame`: The frame that initiated the request.
- `decisionHandler`: The decision handler to call once the app has made its decision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:requestgeolocationpermissionfor:initiatedbyframe:decisionhandler:))*