# webViewDidBeginEditing(_:)

**Framework**: Webkit  
**Kind**: method

Sent by the default notification center when the user begins editing the web view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewDidBeginEditing(_ notification: Notification!)
```

## Parameters

- `notification`: Always set to  . You can retrieve the   object by sending   to  .

## See Also

- [func webView(WebView!, shouldBeginEditingIn: DOMRange!) -> Bool](webeditingdelegate/webview(_:shouldbegineditingin:).md)
  Returns whether the user is allowed to edit a range of content in a web view.
- [func webViewDidEndEditing(Notification!)](webeditingdelegate/webviewdidendediting(_:).md)
  Sent by the default notification center when the user stops editing the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webviewdidbeginediting(_:))*