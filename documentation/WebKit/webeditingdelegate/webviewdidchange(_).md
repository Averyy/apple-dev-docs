# webViewDidChange(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sent by the default notification center when the user changes content in the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewDidChange(_ notification: Notification!)
```

```objc
- (void) webViewDidChange:(NSNotification *) notification;
```

## Parameters

- `notification`: Always set to [`WebViewDidChangeNotification`](../webviewdidchangenotification.md). You can retrieve the `WebView` object by sending `object` to `notification`.

## See Also

### Related Documentation
- [func webView(WebView!, shouldInsert: DOMNode!, replacing: DOMRange!, given: WebViewInsertAction) -> Bool](./webview%28_,shouldinsert,replacing,given%29.md)
  Returns whether the user should be allowed to insert a node in place of a range of content.
- [func webView(WebView!, shouldInsertText: String!, replacing: DOMRange!, given: WebViewInsertAction) -> Bool](./webview%28_,shouldinserttext,replacing,given%29.md)
  Returns whether a user should be allowed to insert text in place of a range of content.
- [func webView(WebView!, shouldDelete: DOMRange!) -> Bool](./webview%28_,shoulddelete%29.md)
  Returns whether the user should be allowed to delete a range of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidchange(_:))*