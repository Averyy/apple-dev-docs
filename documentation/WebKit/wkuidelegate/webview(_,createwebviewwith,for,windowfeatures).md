# webView(_:createWebViewWith:for:windowFeatures:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Creates a new web view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView?
```

```objc
- (WKWebView *) webView:(WKWebView *) webView createWebViewWithConfiguration:(WKWebViewConfiguration *) configuration forNavigationAction:(WKNavigationAction *) navigationAction windowFeatures:(WKWindowFeatures *) windowFeatures;
```

## Return Value

A new web view or `nil`.

## Discussion

The web view returned must be created with the specified configuration. WebKit loads the request in the returned web view.

## Parameters

- `webView`: The web view invoking the delegate method.
- `configuration`: The configuration to use when creating the new web view.
- `navigationAction`: The navigation action causing the new web view to be created.
- `windowFeatures`: Window features requested by the webpage.

## See Also

### Creating and closing the web view
- [func webViewDidClose(WKWebView)](./webviewdidclose%28_%29.md)
  Notifies your app that the DOM window closed successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:createwebviewwith:for:windowfeatures:))*