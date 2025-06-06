# webViewDidChange(_:)

**Framework**: Webkit  
**Kind**: method

Sent by the default notification center when the user changes content in the web view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewDidChange(_ notification: Notification!)
```

## Parameters

- `notification`: Always set to  . You can retrieve the   object by sending   to  .

## See Also

- [func webView(WebView!, shouldInsert: DOMNode!, replacing: DOMRange!, given: WebViewInsertAction) -> Bool](webeditingdelegate/webview(_:shouldinsert:replacing:given:).md)
  Returns whether the user should be allowed to insert a node in place of a range of content.
- [func webView(WebView!, shouldInsertText: String!, replacing: DOMRange!, given: WebViewInsertAction) -> Bool](webeditingdelegate/webview(_:shouldinserttext:replacing:given:).md)
  Returns whether a user should be allowed to insert text in place of a range of content.
- [func webView(WebView!, shouldDelete: DOMRange!) -> Bool](webeditingdelegate/webview(_:shoulddelete:).md)
  Returns whether the user should be allowed to delete a range of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidchange(_:))*