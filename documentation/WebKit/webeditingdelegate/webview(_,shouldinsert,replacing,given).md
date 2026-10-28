# webView(_:shouldInsert:replacing:given:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the user should be allowed to insert a node in place of a range of content.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldInsert node: DOMNode!, replacing range: DOMRange!, given action: WebViewInsertAction) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView shouldInsertNode:(DOMNode *) node replacingDOMRange:(DOMRange *) range givenAction:(WebViewInsertAction) action;
```

## Return Value

[`true`](../../Swift/true.md) if the user should be allowed to insert `node` in `webView`; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method may perform an alternate action—for example, insert a different node—and return [`false`](../../Swift/false.md).

## Parameters

- `webView`: The web view that the user is editing.
- `node`: The content to insert.
- `range`: The portion of the content that is replaced with `node`.
- `action`: Indicates the type of user action that initiated the insertion.

## See Also

### Related Documentation
- [func webViewDidChange(Notification!)](./webviewdidchange%28_%29.md)
  Sent by the default notification center when the user changes content in the web view.
- [func webView(WebView!, shouldInsertText: String!, replacing: DOMRange!, given: WebViewInsertAction) -> Bool](./webview%28_,shouldinserttext,replacing,given%29.md)
  Returns whether a user should be allowed to insert text in place of a range of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldinsert:replacing:given:))*