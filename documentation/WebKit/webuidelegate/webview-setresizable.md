# webView(_:setResizable:)

**Framework**: WebKit  
**Kind**: method

Sets whether a web view’s window can be resized.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, setResizable resizable: Bool)
```

#### Discussion

By default, this method sets the window containing a web view to be resizable. If you display multiple web views in a window then your user interface delegate should implement this method to handle this special case. If you do not implement this method, the `NSWindow` method [`showsResizeIndicator`](https://developer.apple.com/documentation/AppKit/NSWindow/showsResizeIndicator) is sent to the window that contains  `sender`.

## Parameters

- `sender`: The web view that sent the message.
- `resizable`: If  , the web view’s window can be resized; if  , the window is not resizable.

## See Also

- [func webViewIsResizable(WebView!) -> Bool](webuidelegate/webviewisresizable(_:).md)
  Returns a Boolean value indicating whether a web view’s window can be resized.
- [func webView(WebView!, setFrame: NSRect)](webuidelegate/webview(_:setframe:).md)
  Sets the frame rectangle of a web view’s window to the specified frame size.
- [func webViewFrame(WebView!) -> NSRect](webuidelegate/webviewframe(_:).md)
  Returns the frame rectangle of a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:setresizable:))*