# webViewRunModal(_:)

**Framework**: Webkit  
**Kind**: method

Displays a web view in a modal window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewRunModal(_ sender: WebView!)
```

#### Discussion

This method should display and order front a modal window containing the specified web view. This method is invoked after the [`webView(_:createWebViewModalDialogWith:)`](webuidelegate/webview(_:createwebviewmodaldialogwith:).md) method is used to create a new window.

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webView(WebView!, createWebViewModalDialogWith: URLRequest!) -> WebView!](webuidelegate/webview(_:createwebviewmodaldialogwith:).md)
  Creates a modal window containing a web view that loads the specified request.
- [func webView(WebView!, createWebViewWith: URLRequest!) -> WebView!](webuidelegate/webview(_:createwebviewwith:).md)
  Creates a window containing a web view to load the specified request.
- [func webViewClose(WebView!)](webuidelegate/webviewclose(_:).md)
  Closes a web view in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewrunmodal(_:))*