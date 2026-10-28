# webView(_:requestGeolocationPermissionFor:initiatedByFrame:decisionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, requestGeolocationPermissionFor origin: WKSecurityOrigin, initiatedByFrame frame: WKFrameInfo, decisionHandler: @escaping @MainActor @Sendable (WKPermissionDecision) -> Void)
```

```swift
optional func webView(_ webView: WKWebView, requestGeolocationPermissionFor origin: WKSecurityOrigin, initiatedBy frame: WKFrameInfo) async -> WKPermissionDecision
```

```objc
- (void) webView:(WKWebView *) webView requestGeolocationPermissionForOrigin:(WKSecurityOrigin *) origin initiatedByFrame:(WKFrameInfo *) frame decisionHandler:(void (^)(enum WKPermissionDecision)) decisionHandler;
```

## Discussion

Allows your app to determine whether or not the given security origin should have access to geolocation APIs.

## Parameters

- `frame`: The frame that initiated the request.
- `decisionHandler`: The decision handler to call once the app has made its decision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:requestgeolocationpermissionfor:initiatedbyframe:decisionhandler:))*