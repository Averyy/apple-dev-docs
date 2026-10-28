# webView(_:shouldChangeSelectedDOMRange:to:affinity:stillSelecting:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the user should be allowed to change the selected range.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldChangeSelectedDOMRange currentRange: DOMRange!, to proposedRange: DOMRange!, affinity selectionAffinity: NSSelectionAffinity, stillSelecting flag: Bool) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView shouldChangeSelectedDOMRange:(DOMRange *) currentRange toDOMRange:(DOMRange *) proposedRange affinity:(NSSelectionAffinity) selectionAffinity stillSelecting:(BOOL) flag;
```

## Return Value

[`true`](../../Swift/true.md) if the user is allowed to change the selected range; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `webView`: The web view that the user is editing.
- `currentRange`: The old range the user wants to change.
- `proposedRange`: The new range the user wants to select.
- `selectionAffinity`: The direction of the selection.
- `flag`: [`true`](../../Swift/true.md) if the user is still selecting; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [func webViewDidChangeSelection(Notification!)](./webviewdidchangeselection%28_%29.md)
  Sent by the default notification center when the user changes the selection in the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldchangeselecteddomrange:to:affinity:stillselecting:))*