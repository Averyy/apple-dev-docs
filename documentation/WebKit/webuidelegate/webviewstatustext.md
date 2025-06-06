# webViewStatusText(_:)

**Framework**: Webkit  
**Kind**: method

Returns the current status message from a web view’s window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewStatusText(_ sender: WebView!) -> String!
```

#### Return Value

The status message displayed in the web view’s window if one has been set with the [`webView(_:setStatusText:)`](webuidelegate/webview(_:setstatustext:).md) method; otherwise, `nil`.

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webView(WebView!, setStatusText: String!)](webuidelegate/webview(_:setstatustext:).md)
  Sets the status message displayed by a web view’s window, if any, to the specified text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewstatustext(_:))*