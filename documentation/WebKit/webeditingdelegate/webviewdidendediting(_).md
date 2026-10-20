# webViewDidEndEditing(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sent by the default notification center when the user stops editing the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewDidEndEditing(_ notification: Notification!)
```

```objc
- (void) webViewDidEndEditing:(NSNotification *) notification;
```

## Parameters

- `notification`: Always set to [`WebViewDidEndEditingNotification`](../webviewdidendeditingnotification.md). You can retrieve the `WebView` object by sending `object` to `notification`.

## See Also

### Related Documentation
- [func webView(WebView!, shouldEndEditingIn: DOMRange!) -> Bool](./webview%28_,shouldendeditingin%29.md)
  Returns whether the user should be allowed to end editing.
- [func webViewDidBeginEditing(Notification!)](./webviewdidbeginediting%28_%29.md)
  Sent by the default notification center when the user begins editing the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidendediting(_:))*