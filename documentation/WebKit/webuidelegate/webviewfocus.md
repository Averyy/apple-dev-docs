# webViewFocus(_:)

**Framework**: WebKit  
**Kind**: method

Brings a web view’s window to the front and makes it the active window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewFocus(_ sender: WebView!)
```

#### Discussion

By default, this method brings a web view’s window into focus. If you display multiple web views in a window then you might also want to focus the input on `sender`, using [`webView(_:makeFirstResponder:)`](webuidelegate/webview(_:makefirstresponder:).md).

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webViewUnfocus(WebView!)](webuidelegate/webviewunfocus(_:).md)
  Relinquishes focus on a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewfocus(_:))*