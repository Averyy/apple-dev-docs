# webViewIsResizable(_:)

**Framework**: Webkit  
**Kind**: method

Returns a Boolean value indicating whether a web view’s window can be resized.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewIsResizable(_ sender: WebView!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the web view’s window can be resized; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If you display multiple web views in a window then your user interface delegate should implement this method to handle this special case.

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webView(WebView!, setResizable: Bool)](webuidelegate/webview(_:setresizable:).md)
  Sets whether a web view’s window can be resized.
- [func webView(WebView!, setFrame: NSRect)](webuidelegate/webview(_:setframe:).md)
  Sets the frame rectangle of a web view’s window to the specified frame size.
- [func webViewFrame(WebView!) -> NSRect](webuidelegate/webviewframe(_:).md)
  Returns the frame rectangle of a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewisresizable(_:))*