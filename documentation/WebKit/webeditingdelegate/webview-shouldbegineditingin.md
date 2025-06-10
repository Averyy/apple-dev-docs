# webView(_:shouldBeginEditingIn:)

**Framework**: WebKit  
**Kind**: method

Returns whether the user is allowed to edit a range of content in a web view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldBeginEditingIn range: DOMRange!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user is allowed to edit `webView`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is invoked when a web view attempts to become the first responder or when the user drops an object on it.

## Parameters

- `webView`: The web view that the user is editing.
- `range`: The section of the begin-editing request; used to determine if editing is allowed. Typically,   is not the current selection but may becomes the current selection if this method returns  .

## See Also

- [func webView(WebView!, shouldEndEditingIn: DOMRange!) -> Bool](webeditingdelegate/webview(_:shouldendeditingin:).md)
  Returns whether the user should be allowed to end editing.
- [func webViewDidBeginEditing(Notification!)](webeditingdelegate/webviewdidbeginediting(_:).md)
  Sent by the default notification center when the user begins editing the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldbegineditingin:))*