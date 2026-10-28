# webView(_:dismiss:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- visionOS 27.0+

## Declaration

```swift
func webView(_ webView: WKWebView, dismiss environment: WKImmersiveEnvironment, completionHandler: @escaping () -> Void)
```

```swift
func webView(_ webView: WKWebView, dismissImmersiveEnvironment environment: WKImmersiveEnvironment) async
```

```objc
- (void) webView:(WKWebView *) webView dismissImmersiveEnvironment:(WKImmersiveEnvironment *) environment completionHandler:(void (^)()) completionHandler;
```

## Discussion

Asks the delegate to dismiss an immersive environment.

## Parameters

- `webView`: The web view requesting dismissal.
- `environment`: The immersive environment to dismiss.
- `completionHandler`: The completion handler you must invoke once the dismissal transition has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkimmersiveenvironmentdelegate/webview(_:dismiss:completionhandler:))*