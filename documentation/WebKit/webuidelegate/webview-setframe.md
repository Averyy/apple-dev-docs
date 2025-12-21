# webView(_:setFrame:)

**Framework**: WebKit  
**Kind**: method

Sets the frame rectangle of a web view’s window to the specified frame size.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, setFrame frame: NSRect)
```

#### Discussion

The sender invokes this method instead of setting the window’s frame directly, allowing delegates to augment the behavior by, for example, saving the original window size before resizing as a result of JavaScript running. If you do not implement this method, the `NSWindow` method [`setFrame(_:display:)`](https://developer.apple.com/documentation/AppKit/NSWindow/setFrame(_:display:)) is sent to the window that contains `sender`, with [`true`](https://developer.apple.com/documentation/Swift/true) passed as the display argument.

## Parameters

- `sender`: The web view that sent the message.
- `frame`: The frame size.

## See Also

- [func webViewIsResizable(WebView!) -> Bool](webuidelegate/webviewisresizable(_:).md)
  Returns a Boolean value indicating whether a web view’s window can be resized.
- [func webView(WebView!, setResizable: Bool)](webuidelegate/webview(_:setresizable:).md)
  Sets whether a web view’s window can be resized.
- [func webViewFrame(WebView!) -> NSRect](webuidelegate/webviewframe(_:).md)
  Returns the frame rectangle of a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:setframe:))*