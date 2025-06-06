# webViewFrame(_:)

**Framework**: Webkit  
**Kind**: method

Returns the frame rectangle of a web view’s window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewFrame(_ sender: WebView!) -> NSRect
```

#### Return Value

The frame rectangle of the web view’s window.

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webViewIsResizable(WebView!) -> Bool](webuidelegate/webviewisresizable(_:).md)
  Returns a Boolean value indicating whether a web view’s window can be resized.
- [func webView(WebView!, setResizable: Bool)](webuidelegate/webview(_:setresizable:).md)
  Sets whether a web view’s window can be resized.
- [func webView(WebView!, setFrame: NSRect)](webuidelegate/webview(_:setframe:).md)
  Sets the frame rectangle of a web view’s window to the specified frame size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewframe(_:))*