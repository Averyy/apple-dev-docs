# webView(_:createWebViewWith:)

**Framework**: Webkit  
**Kind**: method

Creates a window containing a web view to load the specified request.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, createWebViewWith request: URLRequest!) -> WebView!
```

#### Return Value

The web view that is loading the request.

#### Discussion

This method should begin loading the content for the specified request by sending [`load(_:)`](webframe/load(_:)-47p2s.md) to its main frame. The new window should initially be hidden. Later, a [`webViewShow(_:)`](webuidelegate/webviewshow(_:).md) message is sent to the delegate of the new web view. By default, this method returns `nil`.

## Parameters

- `sender`: The web view that sent the message.
- `request`: The request to load.

## See Also

- [func webView(WebView!, createWebViewModalDialogWith: URLRequest!) -> WebView!](webuidelegate/webview(_:createwebviewmodaldialogwith:).md)
  Creates a modal window containing a web view that loads the specified request.
- [func webViewRunModal(WebView!)](webuidelegate/webviewrunmodal(_:).md)
  Displays a web view in a modal window.
- [func webViewClose(WebView!)](webuidelegate/webviewclose(_:).md)
  Closes a web view in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:createwebviewwith:))*