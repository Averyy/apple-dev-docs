# webViewFrame(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the frame rectangle of a web view’s window.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewFrame(_ sender: WebView!) -> NSRect
```

```objc
- (NSRect) webViewFrame:(WebView *) sender;
```

#### Return Value

The frame rectangle of the web view’s window.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Moving and Resizing Windows
- [func webViewIsResizable(WebView!) -> Bool](./webviewisresizable%28_%29.md)
  Returns a Boolean value indicating whether a web view’s window can be resized.
- [func webView(WebView!, setResizable: Bool)](./webview%28_,setresizable%29.md)
  Sets whether a web view’s window can be resized.
- [func webView(WebView!, setFrame: NSRect)](./webview%28_,setframe%29.md)
  Sets the frame rectangle of a web view’s window to the specified frame size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewframe(_:))*