# webView(_:setResizable:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets whether a web view’s window can be resized.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, setResizable resizable: Bool)
```

```objc
- (void) webView:(WebView *) sender setResizable:(BOOL) resizable;
```

## Discussion

By default, this method sets the window containing a web view to be resizable. If you display multiple web views in a window then your user interface delegate should implement this method to handle this special case. If you do not implement this method, the `NSWindow` method [`showsResizeIndicator`](../../AppKit/nswindow/showsresizeindicator.md) is sent to the window that contains  `sender`.

## Parameters

- `sender`: The web view that sent the message.
- `resizable`: If [`true`](../../Swift/true.md), the web view’s window can be resized; if [`false`](../../Swift/false.md), the window is not resizable.

## See Also

### Moving and Resizing Windows
- [func webViewIsResizable(WebView!) -> Bool](./webviewisresizable%28_%29.md)
  Returns a Boolean value indicating whether a web view’s window can be resized.
- [func webView(WebView!, setFrame: NSRect)](./webview%28_,setframe%29.md)
  Sets the frame rectangle of a web view’s window to the specified frame size.
- [func webViewFrame(WebView!) -> NSRect](./webviewframe%28_%29.md)
  Returns the frame rectangle of a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:setresizable:))*