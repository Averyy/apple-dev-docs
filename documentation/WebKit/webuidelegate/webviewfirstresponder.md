# webViewFirstResponder(_:)

**Framework**: WebKit  
**Kind**: method

Returns the first responder of the web view’s window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewFirstResponder(_ sender: WebView!) -> NSResponder!
```

#### Return Value

The view or subview that currently has the input focus. It can return `nil` or the default first responder if the sender is not attached to a window or if another view (not in the window) has the focus.

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webView(WebView!, makeFirstResponder: NSResponder!)](webuidelegate/webview(_:makefirstresponder:).md)
  Sets the first responder of a web view’s window to the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewfirstresponder(_:))*