# webView(_:setStatusBarVisible:)

**Framework**: Webkit  
**Kind**: method

Sets the visibility of the status bar in a web view’s window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, setStatusBarVisible visible: Bool)
```

#### Discussion

No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `visible`: If  , the delegate should display the status bar (if any); if  , the delegate should hide the status bar.

## See Also

- [func webViewAreToolbarsVisible(WebView!) -> Bool](webuidelegate/webviewaretoolbarsvisible(_:).md)
  Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.
- [func webView(WebView!, setToolbarsVisible: Bool)](webuidelegate/webview(_:settoolbarsvisible:).md)
  Sets whether a web view’s toolbars should be visible.
- [func webViewIsStatusBarVisible(WebView!) -> Bool](webuidelegate/webviewisstatusbarvisible(_:).md)
  Returns a Boolean value indicating whether the status bar in a web view’s window is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:setstatusbarvisible:))*