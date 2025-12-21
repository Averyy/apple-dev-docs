# webViewAreToolbarsVisible(_:)

**Framework**: WebKit  
**Kind**: method

Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewAreToolbarsVisible(_ sender: WebView!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if a web view’s window has any toolbars that are currently visible (other than the status bar); otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webView(WebView!, setToolbarsVisible: Bool)](webuidelegate/webview(_:settoolbarsvisible:).md)
  Sets whether a web view’s toolbars should be visible.
- [func webViewIsStatusBarVisible(WebView!) -> Bool](webuidelegate/webviewisstatusbarvisible(_:).md)
  Returns a Boolean value indicating whether the status bar in a web view’s window is visible.
- [func webView(WebView!, setStatusBarVisible: Bool)](webuidelegate/webview(_:setstatusbarvisible:).md)
  Sets the visibility of the status bar in a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewaretoolbarsvisible(_:))*