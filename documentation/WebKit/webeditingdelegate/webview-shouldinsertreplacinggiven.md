# webView(_:shouldInsert:replacing:given:)

**Framework**: WebKit  
**Kind**: method

Returns whether the user should be allowed to insert a node in place of a range of content.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldInsert node: DOMNode!, replacing range: DOMRange!, given action: WebViewInsertAction) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user should be allowed to insert `node` in `webView`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method may perform an alternate action—for example, insert a different node—and return [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `webView`: The web view that the user is editing.
- `node`: The content to insert.
- `range`: The portion of the content that is replaced with  .
- `action`: Indicates the type of user action that initiated the insertion.

## See Also

- [func webViewDidChange(Notification!)](webeditingdelegate/webviewdidchange(_:).md)
  Sent by the default notification center when the user changes content in the web view.
- [func webView(WebView!, shouldInsertText: String!, replacing: DOMRange!, given: WebViewInsertAction) -> Bool](webeditingdelegate/webview(_:shouldinserttext:replacing:given:).md)
  Returns whether a user should be allowed to insert text in place of a range of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldinsert:replacing:given:))*