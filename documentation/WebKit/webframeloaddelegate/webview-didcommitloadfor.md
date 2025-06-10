# webView(_:didCommitLoadFor:)

**Framework**: WebKit  
**Kind**: method

Called when content starts arriving for a page load.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, didCommitLoadFor frame: WebFrame!)
```

#### Discussion

This method is invoked when a data source transitions from a provisional to committed state—that is, once the data source of `frame` has received one byte or more of data. This method is invoked after a [`webView(_:didStartProvisionalLoadFor:)`](webframeloaddelegate/webview(_:didstartprovisionalloadfor:).md) message but before a `webView:didFinishLoadForFrame:` message is sent to the delegate.

In some cases, a single frame load may be committed more than once. This happens in the case of multipart/x-mixed-replace, also known as a “server push.” In this case, a single frame load results in multiple documents loaded in sequence. This method is invoked once for each document that is successfully loaded.

## Parameters

- `sender`: The web view containing the frame.
- `frame`: The frame being loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didcommitloadfor:))*