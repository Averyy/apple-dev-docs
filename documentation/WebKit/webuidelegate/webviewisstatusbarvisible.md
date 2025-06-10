# webViewIsStatusBarVisible(_:)

**Framework**: WebKit  
**Kind**: method

Returns a Boolean value indicating whether the status bar in a web view’s window is visible.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewIsStatusBarVisible(_ sender: WebView!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a web view’s status bar (if any) is visible; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If you do not implement this method, it returns [`false`](https://developer.apple.com/documentation/swift/false) by default.

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webViewAreToolbarsVisible(WebView!) -> Bool](webuidelegate/webviewaretoolbarsvisible(_:).md)
  Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.
- [func webView(WebView!, setToolbarsVisible: Bool)](webuidelegate/webview(_:settoolbarsvisible:).md)
  Sets whether a web view’s toolbars should be visible.
- [func webView(WebView!, setStatusBarVisible: Bool)](webuidelegate/webview(_:setstatusbarvisible:).md)
  Sets the visibility of the status bar in a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewisstatusbarvisible(_:))*