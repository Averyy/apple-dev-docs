# webViewDidBeginEditing(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sent by the default notification center when the user begins editing the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewDidBeginEditing(_ notification: Notification!)
```

```objc
- (void) webViewDidBeginEditing:(NSNotification *) notification;
```

## Parameters

- `notification`: Always set to [`WebViewDidBeginEditingNotification`](../webviewdidbegineditingnotification.md). You can retrieve the `WebView` object by sending `object` to `notification`.

## See Also

### Related Documentation
- [func webView(WebView!, shouldBeginEditingIn: DOMRange!) -> Bool](./webview%28_,shouldbegineditingin%29.md)
  Returns whether the user is allowed to edit a range of content in a web view.
- [func webViewDidEndEditing(Notification!)](./webviewdidendediting%28_%29.md)
  Sent by the default notification center when the user stops editing the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidbeginediting(_:))*