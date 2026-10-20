# webViewUnfocus(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Relinquishes focus on a web view’s window.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewUnfocus(_ sender: WebView!)
```

```objc
- (void) webViewUnfocus:(WebView *) sender;
```

#### Discussion

This method releases focus for the entire window. If you display multiple web views in a window, you might instead want to change the input focus to another view, using the [`webView(_:makeFirstResponder:)`](./webview%28_,makefirstresponder%29.md) method.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Making Windows Key and Main
- [func webViewFocus(WebView!)](./webviewfocus%28_%29.md)
  Brings a web view’s window to the front and makes it the active window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewunfocus(_:))*