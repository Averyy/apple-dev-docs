# webViewIsStatusBarVisible(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the status bar in a web view’s window is visible.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewIsStatusBarVisible(_ sender: WebView!) -> Bool
```

```objc
- (BOOL) webViewIsStatusBarVisible:(WebView *) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if a web view’s status bar (if any) is visible; otherwise, [`false`](../../Swift/false.md).

#### Discussion

If you do not implement this method, it returns [`false`](../../Swift/false.md) by default.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Managing Toolbars and the Status Bar
- [func webViewAreToolbarsVisible(WebView!) -> Bool](./webviewaretoolbarsvisible%28_%29.md)
  Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.
- [func webView(WebView!, setToolbarsVisible: Bool)](./webview%28_,settoolbarsvisible%29.md)
  Sets whether a web view’s toolbars should be visible.
- [func webView(WebView!, setStatusBarVisible: Bool)](./webview%28_,setstatusbarvisible%29.md)
  Sets the visibility of the status bar in a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewisstatusbarvisible(_:))*