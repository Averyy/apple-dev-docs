# webViewShow(_:)

**Framework**: Webkit  
**Kind**: method

Displays a web view’s window and moves it to the front.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewShow(_ sender: WebView!)
```

#### Discussion

This method is typically used after a call to [`webView(_:createWebViewWith:)`](webuidelegate/webview(_:createwebviewwith:).md), which creates a new window. The new window is not ordered to the front (or even shown) unless you implement this method.

## Parameters

- `sender`: The web view that sent the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewshow(_:))*