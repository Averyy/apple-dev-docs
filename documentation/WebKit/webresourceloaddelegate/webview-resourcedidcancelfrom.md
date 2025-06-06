# webView(_:resource:didCancel:from:)

**Framework**: Webkit  
**Kind**: method

Invoked when an authentication challenge for a resource was canceled.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, resource identifier: Any!, didCancel challenge: URLAuthenticationChallenge!, from dataSource: WebDataSource!)
```

## Parameters

- `sender`: The web view that sent this message.
- `identifier`: An identifier object used to track the resource being loaded by  .
- `challenge`: The authentication challenge that was canceled.
- `dataSource`: The data source for this web view.

## See Also

- [func webView(WebView!, resource: Any!, didReceive: URLAuthenticationChallenge!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didreceive:from:)-54xbd.md)
  Invoked when an authentication challenge has been received for a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:resource:didcancel:from:))*