# webViewDidChangeTypingStyle(_:)

**Framework**: WebKit  
**Kind**: method

Sent by the default notification center when the user changes the typing style in the web view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewDidChangeTypingStyle(_ notification: Notification!)
```

## Parameters

- `notification`: Always set to  . You can retrieve the   object by sending   to  .

## See Also

- [func webView(WebView!, shouldChangeTypingStyle: DOMCSSStyleDeclaration!, toStyle: DOMCSSStyleDeclaration!) -> Bool](webeditingdelegate/webview(_:shouldchangetypingstyle:tostyle:).md)
  Returns whether the user should be allowed to change the typing style in a web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidchangetypingstyle(_:))*