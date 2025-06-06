# webViewClose(_:)

**Framework**: Webkit  
**Kind**: method

Closes a web view in a window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewClose(_ sender: WebView!)
```

#### Discussion

If you display multiple web views in a window then you might want to close only `sender` in your implementation. By default, this method sends the [`close()`](https://developer.apple.com/documentation/AppKit/NSWindow/close()) method to the [`NSWindow`](https://developer.apple.com/documentation/AppKit/NSWindow) object that contains `sender`.

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webView(WebView!, createWebViewModalDialogWith: URLRequest!) -> WebView!](webuidelegate/webview(_:createwebviewmodaldialogwith:).md)
  Creates a modal window containing a web view that loads the specified request.
- [func webViewRunModal(WebView!)](webuidelegate/webviewrunmodal(_:).md)
  Displays a web view in a modal window.
- [func webView(WebView!, createWebViewWith: URLRequest!) -> WebView!](webuidelegate/webview(_:createwebviewwith:).md)
  Creates a window containing a web view to load the specified request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewclose(_:))*