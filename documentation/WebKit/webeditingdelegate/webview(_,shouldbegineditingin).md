# webView(_:shouldBeginEditingIn:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the user is allowed to edit a range of content in a web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldBeginEditingIn range: DOMRange!) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView shouldBeginEditingInDOMRange:(DOMRange *) range;
```

## Return Value

[`true`](../../Swift/true.md) if the user is allowed to edit `webView`; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method is invoked when a web view attempts to become the first responder or when the user drops an object on it.

## Parameters

- `webView`: The web view that the user is editing.
- `range`: The section of the begin-editing request; used to determine if editing is allowed. Typically, `range` is not the current selection but may becomes the current selection if this method returns [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [func webView(WebView!, shouldEndEditingIn: DOMRange!) -> Bool](./webview%28_,shouldendeditingin%29.md)
  Returns whether the user should be allowed to end editing.
- [func webViewDidBeginEditing(Notification!)](./webviewdidbeginediting%28_%29.md)
  Sent by the default notification center when the user begins editing the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldbegineditingin:))*