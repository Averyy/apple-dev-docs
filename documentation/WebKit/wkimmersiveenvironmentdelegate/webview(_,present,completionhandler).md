# webView(_:present:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- visionOS 27.0+

## Declaration

```swift
func webView(_ webView: WKWebView, present environment: WKImmersiveEnvironment, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
func webView(_ webView: WKWebView, presentImmersiveEnvironment environment: WKImmersiveEnvironment) async throws
```

```objc
- (void) webView:(WKWebView *) webView presentImmersiveEnvironment:(WKImmersiveEnvironment *) environment completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

Asks the delegate to present an immersive environment.

## Parameters

- `webView`: The web view requesting presentation.
- `environment`: The immersive environment to present.
- `completionHandler`: The completion handler you must invoke once the presentation transition has completed. The error argument should be used in case the presentation failed and the environment couldn’t be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkimmersiveenvironmentdelegate/webview(_:present:completionhandler:))*