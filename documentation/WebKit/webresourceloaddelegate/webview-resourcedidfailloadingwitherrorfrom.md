# webView(_:resource:didFailLoadingWithError:from:)

**Framework**: WebKit  
**Kind**: method

Invoked when a resource failed to load.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, resource identifier: Any!, didFailLoadingWithError error: (any Error)!, from dataSource: WebDataSource!)
```

#### Discussion

Delegates might implement this method to display or log a detailed error message.

## Parameters

- `sender`: The web view that sent this message.
- `identifier`: An identifier object used to track the resource being loaded by  .
- `error`: The error that occurred loading that resource.
- `dataSource`: The data source for this web view.

## See Also

- [func webView(WebView!, resource: Any!, willSend: URLRequest!, redirectResponse: URLResponse!, from: WebDataSource!) -> URLRequest!](webresourceloaddelegate/webview(_:resource:willsend:redirectresponse:from:).md)
  Invoked before a request is initiated for a resource and returns a possibly modified request.
- [func webView(WebView!, resource: Any!, didFinishLoadingFrom: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didfinishloadingfrom:).md)
  Invoked when all of the data for a given resource is loaded.
- [func webView(WebView!, resource: Any!, didReceive: URLResponse!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didreceive:from:)-22bdg.md)
  Invoked after a resource has been loaded.
- [func webView(WebView!, resource: Any!, didReceiveContentLength: Int, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didreceivecontentlength:from:).md)
  Invoked when some of the data for a given resource has arrived.
- [func webView(WebView!, plugInFailedWithError: (any Error)!, dataSource: WebDataSource!)](webresourceloaddelegate/webview(_:pluginfailedwitherror:datasource:).md)
  Invoked when a plug-in fails to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:resource:didfailloadingwitherror:from:))*