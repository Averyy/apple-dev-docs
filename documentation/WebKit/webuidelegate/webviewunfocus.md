# webViewUnfocus(_:)

**Framework**: WebKit  
**Kind**: method

Relinquishes focus on a web view’s window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewUnfocus(_ sender: WebView!)
```

#### Discussion

This method releases focus for the entire window. If you display multiple web views in a window, you might instead want to change the input focus to another view, using the [`webView(_:makeFirstResponder:)`](webuidelegate/webview(_:makefirstresponder:).md) method.

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webViewFocus(WebView!)](webuidelegate/webviewfocus(_:).md)
  Brings a web view’s window to the front and makes it the active window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewunfocus(_:))*