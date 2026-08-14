# webView(_:shouldDelete:)

**Framework**: WebKit  
**Kind**: method

Returns whether the user should be allowed to delete a range of content.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldDelete range: DOMRange!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user should be allowed to delete the content specified by `range`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method may perform an alternate action—for example, delete a different range—and return [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `webView`: The web view that the user is editing.
- `range`: The range of the content to delete.

## See Also

- [func webViewDidChange(Notification!)](webeditingdelegate/webviewdidchange(_:).md)
  Sent by the default notification center when the user changes content in the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shoulddelete:))*