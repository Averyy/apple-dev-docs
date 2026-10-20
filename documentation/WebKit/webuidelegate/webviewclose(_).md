# webViewClose(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Closes a web view in a window.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewClose(_ sender: WebView!)
```

```objc
- (void) webViewClose:(WebView *) sender;
```

#### Discussion

If you display multiple web views in a window then you might want to close only `sender` in your implementation. By default, this method sends the [`close()`](../../AppKit/nswindow/close%28%29.md) method to the [`NSWindow`](../../AppKit/nswindow.md) object that contains `sender`.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Creating and Closing Windows
- [func webView(WebView!, createWebViewModalDialogWith: URLRequest!) -> WebView!](./webview%28_,createwebviewmodaldialogwith%29.md)
  Creates a modal window containing a web view that loads the specified request.
- [func webViewRunModal(WebView!)](./webviewrunmodal%28_%29.md)
  Displays a web view in a modal window.
- [func webView(WebView!, createWebViewWith: URLRequest!) -> WebView!](./webview%28_,createwebviewwith%29.md)
  Creates a window containing a web view to load the specified request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewclose(_:))*