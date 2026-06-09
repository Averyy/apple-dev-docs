# webView(_:dismiss:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
func webView(_ webView: WKWebView, dismissImmersiveEnvironment environment: WKImmersiveEnvironment) async
```

#### Discussion

Asks the delegate to dismiss an immersive environment.

## Parameters

- `webView`: The web view requesting dismissal.
- `environment`: The immersive environment to dismiss.
- `completionHandler`: The completion handler you must invoke once the dismissal transition has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkimmersiveenvironmentdelegate/webview(_:dismiss:completionhandler:))*