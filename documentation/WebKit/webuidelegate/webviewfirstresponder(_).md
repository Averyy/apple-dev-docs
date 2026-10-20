# webViewFirstResponder(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the first responder of the web view’s window.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewFirstResponder(_ sender: WebView!) -> NSResponder!
```

```objc
- (NSResponder *) webViewFirstResponder:(WebView *) sender;
```

#### Return Value

The view or subview that currently has the input focus. It can return `nil` or the default first responder if the sender is not attached to a window or if another view (not in the window) has the focus.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Working with the Responder Chain
- [func webView(WebView!, makeFirstResponder: NSResponder!)](./webview%28_,makefirstresponder%29.md)
  Sets the first responder of a web view’s window to the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewfirstresponder(_:))*