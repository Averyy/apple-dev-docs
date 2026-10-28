# webView(_:setFrame:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the frame rectangle of a web view’s window to the specified frame size.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, setFrame frame: NSRect)
```

```objc
- (void) webView:(WebView *) sender setFrame:(NSRect) frame;
```

## Discussion

The sender invokes this method instead of setting the window’s frame directly, allowing delegates to augment the behavior by, for example, saving the original window size before resizing as a result of JavaScript running. If you do not implement this method, the `NSWindow` method [`setFrame(_:display:)`](../../AppKit/nswindow/setframe%28_,display%29.md) is sent to the window that contains `sender`, with [`true`](../../Swift/true.md) passed as the display argument.

## Parameters

- `sender`: The web view that sent the message.
- `frame`: The frame size.

## See Also

### Moving and Resizing Windows
- [func webViewIsResizable(WebView!) -> Bool](./webviewisresizable%28_%29.md)
  Returns a Boolean value indicating whether a web view’s window can be resized.
- [func webView(WebView!, setResizable: Bool)](./webview%28_,setresizable%29.md)
  Sets whether a web view’s window can be resized.
- [func webViewFrame(WebView!) -> NSRect](./webviewframe%28_%29.md)
  Returns the frame rectangle of a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:setframe:))*