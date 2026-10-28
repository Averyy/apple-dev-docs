# webViewRunModal(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays a web view in a modal window.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewRunModal(_ sender: WebView!)
```

```objc
- (void) webViewRunModal:(WebView *) sender;
```

## Discussion

This method should display and order front a modal window containing the specified web view. This method is invoked after the [`webView(_:createWebViewModalDialogWith:)`](./webview%28_,createwebviewmodaldialogwith%29.md) method is used to create a new window.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Creating and Closing Windows
- [func webView(WebView!, createWebViewModalDialogWith: URLRequest!) -> WebView!](./webview%28_,createwebviewmodaldialogwith%29.md)
  Creates a modal window containing a web view that loads the specified request.
- [func webView(WebView!, createWebViewWith: URLRequest!) -> WebView!](./webview%28_,createwebviewwith%29.md)
  Creates a window containing a web view to load the specified request.
- [func webViewClose(WebView!)](./webviewclose%28_%29.md)
  Closes a web view in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewrunmodal(_:))*