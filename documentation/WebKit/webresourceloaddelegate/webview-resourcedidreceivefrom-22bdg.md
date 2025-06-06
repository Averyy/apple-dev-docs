# webView(_:resource:didReceive:from:)

**Framework**: Webkit  
**Kind**: method

Invoked after a resource has been loaded.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, resource identifier: Any!, didReceive response: URLResponse!, from dataSource: WebDataSource!)
```

#### Discussion

In some rare cases, multiple responses may be received for a single resource. This happens in the case of multipart/x-mixed-replace, also known as a . In this case, delegates should assume that the progress of loading this resource restarts, and the expected content length may change.

## Parameters

- `sender`: The web view that sent this message.
- `identifier`: An identifier object used to track the resource being loaded by  .
- `response`: The reply that was received.
- `dataSource`: The data source for this web view.

## See Also

- [func webView(WebView!, resource: Any!, willSend: URLRequest!, redirectResponse: URLResponse!, from: WebDataSource!) -> URLRequest!](webresourceloaddelegate/webview(_:resource:willsend:redirectresponse:from:).md)
  Invoked before a request is initiated for a resource and returns a possibly modified request.
- [func webView(WebView!, resource: Any!, didFinishLoadingFrom: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didfinishloadingfrom:).md)
  Invoked when all of the data for a given resource is loaded.
- [func webView(WebView!, resource: Any!, didReceiveContentLength: Int, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didreceivecontentlength:from:).md)
  Invoked when some of the data for a given resource has arrived.
- [func webView(WebView!, resource: Any!, didFailLoadingWithError: (any Error)!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didfailloadingwitherror:from:).md)
  Invoked when a resource failed to load.
- [func webView(WebView!, plugInFailedWithError: (any Error)!, dataSource: WebDataSource!)](webresourceloaddelegate/webview(_:pluginfailedwitherror:datasource:).md)
  Invoked when a plug-in fails to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:resource:didreceive:from:)-22bdg)*