# webView(_:shouldChangeTypingStyle:toStyle:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the user should be allowed to change the typing style in a web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldChangeTypingStyle currentStyle: DOMCSSStyleDeclaration!, toStyle proposedStyle: DOMCSSStyleDeclaration!) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView shouldChangeTypingStyle:(DOMCSSStyleDeclaration *) currentStyle toStyle:(DOMCSSStyleDeclaration *) proposedStyle;
```

#### Return Value

[`true`](../../Swift/true.md) if the user should be allowed to change the typing style in `webView` to `proposedStyle`; otherwise, [`false`](../../Swift/false.md).

#### Discussion

You can implement this method to take some other action—for example, set the typing style to a different style—and return [`false`](../../Swift/false.md) .

## Parameters

- `webView`: The web view that the user is editing.
- `currentStyle`: The old style the user wants to change.
- `proposedStyle`: The new style the user wants to set.

## See Also

### Related Documentation
- [func webViewDidChangeTypingStyle(Notification!)](./webviewdidchangetypingstyle%28_%29.md)
  Sent by the default notification center when the user changes the typing style in the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldchangetypingstyle:tostyle:))*