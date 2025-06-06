# webView(_:setToolbarsVisible:)

**Framework**: Webkit  
**Kind**: method

Sets whether a web view’s toolbars should be visible.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, setToolbarsVisible visible: Bool)
```

#### Discussion

No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `visible`: If  , all toolbars (with the exception of the status bar) are shown; otherwise, all toolbars (with the exception of the status bar) are removed.

## See Also

- [func webViewAreToolbarsVisible(WebView!) -> Bool](webuidelegate/webviewaretoolbarsvisible(_:).md)
  Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.
- [func webViewIsStatusBarVisible(WebView!) -> Bool](webuidelegate/webviewisstatusbarvisible(_:).md)
  Returns a Boolean value indicating whether the status bar in a web view’s window is visible.
- [func webView(WebView!, setStatusBarVisible: Bool)](webuidelegate/webview(_:setstatusbarvisible:).md)
  Sets the visibility of the status bar in a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:settoolbarsvisible:))*