# webView(_:setToolbarsVisible:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets whether a web view’s toolbars should be visible.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, setToolbarsVisible visible: Bool)
```

```objc
- (void) webView:(WebView *) sender setToolbarsVisible:(BOOL) visible;
```

#### Discussion

No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `visible`: If [`true`](../../Swift/true.md), all toolbars (with the exception of the status bar) are shown; otherwise, all toolbars (with the exception of the status bar) are removed.

## See Also

### Managing Toolbars and the Status Bar
- [func webViewAreToolbarsVisible(WebView!) -> Bool](./webviewaretoolbarsvisible%28_%29.md)
  Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.
- [func webViewIsStatusBarVisible(WebView!) -> Bool](./webviewisstatusbarvisible%28_%29.md)
  Returns a Boolean value indicating whether the status bar in a web view’s window is visible.
- [func webView(WebView!, setStatusBarVisible: Bool)](./webview%28_,setstatusbarvisible%29.md)
  Sets the visibility of the status bar in a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:settoolbarsvisible:))*