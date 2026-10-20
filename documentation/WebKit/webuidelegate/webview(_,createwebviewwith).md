# webView(_:createWebViewWith:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Creates a window containing a web view to load the specified request.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, createWebViewWith request: URLRequest!) -> WebView!
```

```objc
- (WebView *) webView:(WebView *) sender createWebViewWithRequest:(NSURLRequest *) request;
```

#### Return Value

The web view that is loading the request.

#### Discussion

This method should begin loading the content for the specified request by sending [`load(_:)`](../webframe/load%28_%29-47p2s.md) to its main frame. The new window should initially be hidden. Later, a [`webViewShow(_:)`](./webviewshow%28_%29.md) message is sent to the delegate of the new web view. By default, this method returns `nil`.

## Parameters

- `sender`: The web view that sent the message.
- `request`: The request to load.

## See Also

### Creating and Closing Windows
- [func webView(WebView!, createWebViewModalDialogWith: URLRequest!) -> WebView!](./webview%28_,createwebviewmodaldialogwith%29.md)
  Creates a modal window containing a web view that loads the specified request.
- [func webViewRunModal(WebView!)](./webviewrunmodal%28_%29.md)
  Displays a web view in a modal window.
- [func webViewClose(WebView!)](./webviewclose%28_%29.md)
  Closes a web view in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:createwebviewwith:))*