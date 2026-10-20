# webView(_:shouldEndEditingIn:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the user should be allowed to end editing.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldEndEditingIn range: DOMRange!) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView shouldEndEditingInDOMRange:(DOMRange *) range;
```

#### Return Value

[`true`](../../Swift/true.md) if the user should be allowed to end editing `webView`; otherwise, [`false`](../../Swift/false.md). If this method returns[`true`](../../Swift/true.md), `webView` ends editing and resigns as the first responder.

#### Discussion

This method is invoked when a web view attempts to resign as the first responder.

## Parameters

- `webView`: The web view that the user is editing.
- `range`: Typically, the current selection, although it might not be. Use the `range` parameter to help determine whether the user can end editing.

## See Also

### Related Documentation
- [func webView(WebView!, shouldBeginEditingIn: DOMRange!) -> Bool](./webview%28_,shouldbegineditingin%29.md)
  Returns whether the user is allowed to edit a range of content in a web view.
- [func webViewDidEndEditing(Notification!)](./webviewdidendediting%28_%29.md)
  Sent by the default notification center when the user stops editing the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldendeditingin:))*