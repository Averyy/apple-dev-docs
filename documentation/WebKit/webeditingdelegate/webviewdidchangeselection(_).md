# webViewDidChangeSelection(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sent by the default notification center when the user changes the selection in the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewDidChangeSelection(_ notification: Notification!)
```

```objc
- (void) webViewDidChangeSelection:(NSNotification *) notification;
```

## Parameters

- `notification`: Always set to [`WebViewDidChangeSelectionNotification`](../webviewdidchangeselectionnotification.md). You can retrieve the `WebView` object by sending `object` to `notification`.

## See Also

### Related Documentation
- [func webView(WebView!, shouldChangeSelectedDOMRange: DOMRange!, to: DOMRange!, affinity: NSSelectionAffinity, stillSelecting: Bool) -> Bool](./webview%28_,shouldchangeselecteddomrange,to,affinity,stillselecting%29.md)
  Returns whether the user should be allowed to change the selected range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidchangeselection(_:))*