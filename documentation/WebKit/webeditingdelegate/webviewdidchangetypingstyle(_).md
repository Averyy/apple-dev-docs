# webViewDidChangeTypingStyle(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sent by the default notification center when the user changes the typing style in the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewDidChangeTypingStyle(_ notification: Notification!)
```

```objc
- (void) webViewDidChangeTypingStyle:(NSNotification *) notification;
```

## Parameters

- `notification`: Always set to [`WebViewDidChangeTypingStyleNotification`](../webviewdidchangetypingstylenotification.md). You can retrieve the `WebView` object by sending `object` to `notification`.

## See Also

### Related Documentation
- [func webView(WebView!, shouldChangeTypingStyle: DOMCSSStyleDeclaration!, toStyle: DOMCSSStyleDeclaration!) -> Bool](./webview%28_,shouldchangetypingstyle,tostyle%29.md)
  Returns whether the user should be allowed to change the typing style in a web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidchangetypingstyle(_:))*