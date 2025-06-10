# webView(_:resource:didReceive:from:)

**Framework**: WebKit  
**Kind**: method

Invoked when an authentication challenge has been received for a resource.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, resource identifier: Any!, didReceive challenge: URLAuthenticationChallenge!, from dataSource: WebDataSource!)
```

## Parameters

- `sender`: The web view that sent this message.
- `identifier`: An identifier object used to track the resource being loaded by  .
- `challenge`: The authentication challenge that was received.
- `dataSource`: The data source for this web view.

## See Also

- [func webView(WebView!, resource: Any!, didCancel: URLAuthenticationChallenge!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didcancel:from:).md)
  Invoked when an authentication challenge for a resource was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:resource:didreceive:from:)-54xbd)*