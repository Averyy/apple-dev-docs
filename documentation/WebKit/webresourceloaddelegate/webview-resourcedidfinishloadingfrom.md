# webView(_:resource:didFinishLoadingFrom:)

**Framework**: Webkit  
**Kind**: method

Invoked when all of the data for a given resource is loaded.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, resource identifier: Any!, didFinishLoadingFrom dataSource: WebDataSource!)
```

#### Discussion

The `identifier` parameter is used to track the resource being loaded by `dataSource`. Delegates might implement this method to update the load status of an individual resource.

## Parameters

- `sender`: The web view that sent this message.
- `identifier`: An identifier object used to track the resource being loaded by  .
- `dataSource`: The data source for this web view.

## See Also

- [func webView(WebView!, resource: Any!, willSend: URLRequest!, redirectResponse: URLResponse!, from: WebDataSource!) -> URLRequest!](webresourceloaddelegate/webview(_:resource:willsend:redirectresponse:from:).md)
  Invoked before a request is initiated for a resource and returns a possibly modified request.
- [func webView(WebView!, resource: Any!, didReceive: URLResponse!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didreceive:from:)-22bdg.md)
  Invoked after a resource has been loaded.
- [func webView(WebView!, resource: Any!, didReceiveContentLength: Int, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didreceivecontentlength:from:).md)
  Invoked when some of the data for a given resource has arrived.
- [func webView(WebView!, resource: Any!, didFailLoadingWithError: (any Error)!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didfailloadingwitherror:from:).md)
  Invoked when a resource failed to load.
- [func webView(WebView!, plugInFailedWithError: (any Error)!, dataSource: WebDataSource!)](webresourceloaddelegate/webview(_:pluginfailedwitherror:datasource:).md)
  Invoked when a plug-in fails to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:resource:didfinishloadingfrom:))*