# webView(_:shouldEndEditingIn:)

**Framework**: Webkit  
**Kind**: method

Returns whether the user should be allowed to end editing.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldEndEditingIn range: DOMRange!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user should be allowed to end editing `webView`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). If this method returns[`true`](https://developer.apple.com/documentation/swift/true), `webView` ends editing and resigns as the first responder.

#### Discussion

This method is invoked when a web view attempts to resign as the first responder.

## Parameters

- `webView`: The web view that the user is editing.
- `range`: Typically, the current selection, although it might not be. Use the   parameter to help determine whether the user can end editing.

## See Also

- [func webView(WebView!, shouldBeginEditingIn: DOMRange!) -> Bool](webeditingdelegate/webview(_:shouldbegineditingin:).md)
  Returns whether the user is allowed to edit a range of content in a web view.
- [func webViewDidEndEditing(Notification!)](webeditingdelegate/webviewdidendediting(_:).md)
  Sent by the default notification center when the user stops editing the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldendeditingin:))*