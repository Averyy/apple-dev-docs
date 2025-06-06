# webViewDidEndEditing(_:)

**Framework**: Webkit  
**Kind**: method

Sent by the default notification center when the user stops editing the web view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewDidEndEditing(_ notification: Notification!)
```

## Parameters

- `notification`: Always set to  . You can retrieve the   object by sending   to  .

## See Also

- [func webView(WebView!, shouldEndEditingIn: DOMRange!) -> Bool](webeditingdelegate/webview(_:shouldendeditingin:).md)
  Returns whether the user should be allowed to end editing.
- [func webViewDidBeginEditing(Notification!)](webeditingdelegate/webviewdidbeginediting(_:).md)
  Sent by the default notification center when the user begins editing the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidendediting(_:))*