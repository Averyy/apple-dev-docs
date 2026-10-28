# webViewDidClose(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Notifies your app that the DOM window closed successfully.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
optional func webViewDidClose(_ webView: WKWebView)
```

```objc
- (void) webViewDidClose:(WKWebView *) webView;
```

## Discussion

Your app should remove the web view from the view hierarchy and update the UI as needed, for instance by closing the containing browser tab or window.

## Parameters

- `webView`: The web view invoking the delegate method.

## See Also

### Creating and closing the web view
- [func webView(WKWebView, createWebViewWith: WKWebViewConfiguration, for: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView?](./webview%28_,createwebviewwith,for,windowfeatures%29.md)
  Creates a new web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webviewdidclose(_:))*