# webView(_:shouldChangeSelectedDOMRange:to:affinity:stillSelecting:)

**Framework**: Webkit  
**Kind**: method

Returns whether the user should be allowed to change the selected range.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldChangeSelectedDOMRange currentRange: DOMRange!, to proposedRange: DOMRange!, affinity selectionAffinity: NSSelectionAffinity, stillSelecting flag: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user is allowed to change the selected range; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `webView`: The web view that the user is editing.
- `currentRange`: The old range the user wants to change.
- `proposedRange`: The new range the user wants to select.
- `selectionAffinity`: The direction of the selection.
- `flag`:   if the user is still selecting; otherwise,  .

## See Also

- [func webViewDidChangeSelection(Notification!)](webeditingdelegate/webviewdidchangeselection(_:).md)
  Sent by the default notification center when the user changes the selection in the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldchangeselecteddomrange:to:affinity:stillselecting:))*