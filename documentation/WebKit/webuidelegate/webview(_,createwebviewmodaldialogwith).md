# webView(_:createWebViewModalDialogWith:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Creates a modal window containing a web view that loads the specified request.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, createWebViewModalDialogWith request: URLRequest!) -> WebView!
```

```objc
- (WebView *) webView:(WebView *) sender createWebViewModalDialogWithRequest:(NSURLRequest *) request;
```

## Return Value

The web view that is loading the specified request.

## Discussion

This method is invoked when JavaScript calls `window.showModalDialog`. It should create a new modal window containing the web view and initially hide the window. The [`webViewRunModal(_:)`](./webviewrunmodal%28_%29.md) message is sent to the delegate to display the web view.

## Parameters

- `sender`: The web view that sent the message.
- `request`: The request to load.

## See Also

### Related Documentation
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
### Creating and Closing Windows
- [func webViewRunModal(WebView!)](./webviewrunmodal%28_%29.md)
  Displays a web view in a modal window.
- [func webView(WebView!, createWebViewWith: URLRequest!) -> WebView!](./webview%28_,createwebviewwith%29.md)
  Creates a window containing a web view to load the specified request.
- [func webViewClose(WebView!)](./webviewclose%28_%29.md)
  Closes a web view in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:createwebviewmodaldialogwith:))*