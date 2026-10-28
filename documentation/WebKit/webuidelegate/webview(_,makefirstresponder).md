# webView(_:makeFirstResponder:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the first responder of a web view’s window to the specified view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, makeFirstResponder responder: NSResponder!)
```

```objc
- (void) webView:(WebView *) sender makeFirstResponder:(NSResponder *) responder;
```

## Discussion

You can ignore this message if `sender` is not yet attached to a window.

## Parameters

- `sender`: The web view that sent the message.
- `responder`: A view in the web view’s hierarchy.

## See Also

### Working with the Responder Chain
- [func webViewFirstResponder(WebView!) -> NSResponder!](./webviewfirstresponder%28_%29.md)
  Returns the first responder of the web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:makefirstresponder:))*