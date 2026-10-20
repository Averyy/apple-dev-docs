# webViewAreToolbarsVisible(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewAreToolbarsVisible(_ sender: WebView!) -> Bool
```

```objc
- (BOOL) webViewAreToolbarsVisible:(WebView *) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if a web view’s window has any toolbars that are currently visible (other than the status bar); otherwise, [`false`](../../Swift/false.md).

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Managing Toolbars and the Status Bar
- [func webView(WebView!, setToolbarsVisible: Bool)](./webview%28_,settoolbarsvisible%29.md)
  Sets whether a web view’s toolbars should be visible.
- [func webViewIsStatusBarVisible(WebView!) -> Bool](./webviewisstatusbarvisible%28_%29.md)
  Returns a Boolean value indicating whether the status bar in a web view’s window is visible.
- [func webView(WebView!, setStatusBarVisible: Bool)](./webview%28_,setstatusbarvisible%29.md)
  Sets the visibility of the status bar in a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewaretoolbarsvisible(_:))*