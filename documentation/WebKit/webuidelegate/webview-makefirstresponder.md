# webView(_:makeFirstResponder:)

**Framework**: WebKit  
**Kind**: method

Sets the first responder of a web view’s window to the specified view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, makeFirstResponder responder: NSResponder!)
```

#### Discussion

You can ignore this message if `sender` is not yet attached to a window.

## Parameters

- `sender`: The web view that sent the message.
- `responder`: A view in the web view’s hierarchy.

## See Also

- [func webViewFirstResponder(WebView!) -> NSResponder!](webuidelegate/webviewfirstresponder(_:).md)
  Returns the first responder of the web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:makefirstresponder:))*