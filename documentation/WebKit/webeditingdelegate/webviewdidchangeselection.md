# webViewDidChangeSelection(_:)

**Framework**: WebKit  
**Kind**: method

Sent by the default notification center when the user changes the selection in the web view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewDidChangeSelection(_ notification: Notification!)
```

## Parameters

- `notification`: Always set to  . You can retrieve the   object by sending   to  .

## See Also

- [func webView(WebView!, shouldChangeSelectedDOMRange: DOMRange!, to: DOMRange!, affinity: NSSelectionAffinity, stillSelecting: Bool) -> Bool](webeditingdelegate/webview(_:shouldchangeselecteddomrange:to:affinity:stillselecting:).md)
  Returns whether the user should be allowed to change the selected range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidchangeselection(_:))*