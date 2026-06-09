# webView(_:shouldAllowImmersiveEnvironmentFromFrame:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
func webView(_ webView: WKWebView, shouldAllowImmersiveEnvironmentFrom frame: WKFrameInfo) async -> Bool
```

#### Discussion

Asks the delegate whether to allow an immersive environment from the specified frame.

## Parameters

- `webView`: The web view that received the immersive environment request.
- `frame`: The frame information from the website requesting the immersive environment.
- `completionHandler`: The completion handler you must invoke with the request’s answer. `YES` to allow the environment presentation, or `NO` to deny it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkimmersiveenvironmentdelegate/webview(_:shouldallowimmersiveenvironmentfromframe:completionhandler:))*