# webViewIsResizable(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether a web view’s window can be resized.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewIsResizable(_ sender: WebView!) -> Bool
```

```objc
- (BOOL) webViewIsResizable:(WebView *) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if the web view’s window can be resized; otherwise, [`false`](../../Swift/false.md).

#### Discussion

If you display multiple web views in a window then your user interface delegate should implement this method to handle this special case.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Moving and Resizing Windows
- [func webView(WebView!, setResizable: Bool)](./webview%28_,setresizable%29.md)
  Sets whether a web view’s window can be resized.
- [func webView(WebView!, setFrame: NSRect)](./webview%28_,setframe%29.md)
  Sets the frame rectangle of a web view’s window to the specified frame size.
- [func webViewFrame(WebView!) -> NSRect](./webviewframe%28_%29.md)
  Returns the frame rectangle of a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewisresizable(_:))*