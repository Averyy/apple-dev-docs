# webViewShow(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays a web view’s window and moves it to the front.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewShow(_ sender: WebView!)
```

```objc
- (void) webViewShow:(WebView *) sender;
```

## Discussion

This method is typically used after a call to [`webView(_:createWebViewWith:)`](./webview%28_,createwebviewwith%29.md), which creates a new window. The new window is not ordered to the front (or even shown) unless you implement this method.

## Parameters

- `sender`: The web view that sent the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewshow(_:))*