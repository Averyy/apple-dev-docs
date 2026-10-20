# webView(_:shouldInsertText:replacing:given:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns whether a user should be allowed to insert text in place of a range of content.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldInsertText text: String!, replacing range: DOMRange!, given action: WebViewInsertAction) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView shouldInsertText:(NSString *) text replacingDOMRange:(DOMRange *) range givenAction:(WebViewInsertAction) action;
```

#### Return Value

[`true`](../../Swift/true.md) if the user should be allowed to insert `text` in `webView`; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method may perform an alternate action—for example, insert different text—and return [`false`](../../Swift/false.md).

## Parameters

- `webView`: The web view that the user is editing.
- `text`: The text to insert.
- `range`: The portion of the document that will be replaced with `text`.
- `action`: Indicates the type of user action that initiated the insertion.

## See Also

### Related Documentation
- [func webViewDidChange(Notification!)](./webviewdidchange%28_%29.md)
  Sent by the default notification center when the user changes content in the web view.
- [func webView(WebView!, shouldInsert: DOMNode!, replacing: DOMRange!, given: WebViewInsertAction) -> Bool](./webview%28_,shouldinsert,replacing,given%29.md)
  Returns whether the user should be allowed to insert a node in place of a range of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldinserttext:replacing:given:))*