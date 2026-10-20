# webView(_:resource:didReceive:from:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Invoked when an authentication challenge has been received for a resource.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, resource identifier: Any!, didReceive challenge: URLAuthenticationChallenge!, from dataSource: WebDataSource!)
```

```objc
- (void) webView:(WebView *) sender resource:(id) identifier didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *) challenge fromDataSource:(WebDataSource *) dataSource;
```

## Parameters

- `sender`: The web view that sent this message.
- `identifier`: An identifier object used to track the resource being loaded by `dataSource`.
- `challenge`: The authentication challenge that was received.
- `dataSource`: The data source for this web view.

## See Also

### Authenticating Resources
- [func webView(WebView!, resource: Any!, didCancel: URLAuthenticationChallenge!, from: WebDataSource!)](./webview%28_,resource,didcancel,from%29.md)
  Invoked when an authentication challenge for a resource was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:resource:didreceive:from:)-54xbd)*