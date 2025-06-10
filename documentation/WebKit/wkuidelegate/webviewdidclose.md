# webViewDidClose(_:)

**Framework**: WebKit  
**Kind**: method

Notifies your app that the DOM window closed successfully.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webViewDidClose(_ webView: WKWebView)
```

#### Discussion

Your app should remove the web view from the view hierarchy and update the UI as needed, for instance by closing the containing browser tab or window.

## Parameters

- `webView`: The web view invoking the delegate method.

## See Also

- [func webView(WKWebView, createWebViewWith: WKWebViewConfiguration, for: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView?](wkuidelegate/webview(_:createwebviewwith:for:windowfeatures:).md)
  Creates a new web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webviewdidclose(_:))*