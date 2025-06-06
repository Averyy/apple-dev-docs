# webView(_:createWebViewModalDialogWith:)

**Framework**: Webkit  
**Kind**: method

Creates a modal window containing a web view that loads the specified request.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, createWebViewModalDialogWith request: URLRequest!) -> WebView!
```

#### Return Value

The web view that is loading the specified request.

#### Discussion

This method is invoked when JavaScript calls `window.showModalDialog`. It should create a new modal window containing the web view and initially hide the window. The [`webViewRunModal(_:)`](webuidelegate/webviewrunmodal(_:).md) message is sent to the delegate to display the web view.

## Parameters

- `sender`: The web view that sent the message.
- `request`: The request to load.

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [func webViewRunModal(WebView!)](webuidelegate/webviewrunmodal(_:).md)
  Displays a web view in a modal window.
- [func webView(WebView!, createWebViewWith: URLRequest!) -> WebView!](webuidelegate/webview(_:createwebviewwith:).md)
  Creates a window containing a web view to load the specified request.
- [func webViewClose(WebView!)](webuidelegate/webviewclose(_:).md)
  Closes a web view in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:createwebviewmodaldialogwith:))*