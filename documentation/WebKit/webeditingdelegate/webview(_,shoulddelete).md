# webView(_:shouldDelete:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the user should be allowed to delete a range of content.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldDelete range: DOMRange!) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView shouldDeleteDOMRange:(DOMRange *) range;
```

## Return Value

[`true`](../../Swift/true.md) if the user should be allowed to delete the content specified by `range`; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method may perform an alternate action—for example, delete a different range—and return [`false`](../../Swift/false.md).

## Parameters

- `webView`: The web view that the user is editing.
- `range`: The range of the content to delete.

## See Also

### Related Documentation
- [func webViewDidChange(Notification!)](./webviewdidchange%28_%29.md)
  Sent by the default notification center when the user changes content in the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shoulddelete:))*