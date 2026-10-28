# webView(_:setStatusBarVisible:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the visibility of the status bar in a web view’s window.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, setStatusBarVisible visible: Bool)
```

```objc
- (void) webView:(WebView *) sender setStatusBarVisible:(BOOL) visible;
```

## Discussion

No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `visible`: If [`true`](../../Swift/true.md), the delegate should display the status bar (if any); if [`false`](../../Swift/false.md), the delegate should hide the status bar.

## See Also

### Managing Toolbars and the Status Bar
- [func webViewAreToolbarsVisible(WebView!) -> Bool](./webviewaretoolbarsvisible%28_%29.md)
  Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.
- [func webView(WebView!, setToolbarsVisible: Bool)](./webview%28_,settoolbarsvisible%29.md)
  Sets whether a web view’s toolbars should be visible.
- [func webViewIsStatusBarVisible(WebView!) -> Bool](./webviewisstatusbarvisible%28_%29.md)
  Returns a Boolean value indicating whether the status bar in a web view’s window is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:setstatusbarvisible:))*