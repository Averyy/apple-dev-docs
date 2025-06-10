# webView(_:shouldChangeTypingStyle:toStyle:)

**Framework**: WebKit  
**Kind**: method

Returns whether the user should be allowed to change the typing style in a web view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldChangeTypingStyle currentStyle: DOMCSSStyleDeclaration!, toStyle proposedStyle: DOMCSSStyleDeclaration!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user should be allowed to change the typing style in `webView` to `proposedStyle`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

You can implement this method to take some other action—for example, set the typing style to a different style—and return [`false`](https://developer.apple.com/documentation/swift/false) .

## Parameters

- `webView`: The web view that the user is editing.
- `currentStyle`: The old style the user wants to change.
- `proposedStyle`: The new style the user wants to set.

## See Also

- [func webViewDidChangeTypingStyle(Notification!)](webeditingdelegate/webviewdidchangetypingstyle(_:).md)
  Sent by the default notification center when the user changes the typing style in the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldchangetypingstyle:tostyle:))*