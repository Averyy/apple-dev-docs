# webViewFocus(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Brings a web view’s window to the front and makes it the active window.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewFocus(_ sender: WebView!)
```

```objc
- (void) webViewFocus:(WebView *) sender;
```

#### Discussion

By default, this method brings a web view’s window into focus. If you display multiple web views in a window then you might also want to focus the input on `sender`, using [`webView(_:makeFirstResponder:)`](./webview%28_,makefirstresponder%29.md).

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Making Windows Key and Main
- [func webViewUnfocus(WebView!)](./webviewunfocus%28_%29.md)
  Relinquishes focus on a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewfocus(_:))*