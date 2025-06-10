# webView(_:resource:willSend:redirectResponse:from:)

**Framework**: WebKit  
**Kind**: method

Invoked before a request is initiated for a resource and returns a possibly modified request.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, resource identifier: Any!, willSend request: URLRequest!, redirectResponse: URLResponse!, from dataSource: WebDataSource!) -> URLRequest!
```

#### Return Value

A possibly modified request.

#### Discussion

Delegates might implement this method to modify resource requests before they are sent. Note that this method might be invoked multiple times per load (as a result of a server redirect) where as the  [`webView(_:identifierForInitialRequest:from:)`](webresourceloaddelegate/webview(_:identifierforinitialrequest:from:).md) method is invoked once.

## Parameters

- `sender`: The web view that sent this message.
- `identifier`: An identifier object used to track the resource being loaded by  .
- `request`: The request that is sent.
- `redirectResponse`: The redirect server response. If  , there is no redirect in progress.
- `dataSource`: The data source for this web view.

## See Also

- [func webView(WebView!, resource: Any!, didFinishLoadingFrom: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didfinishloadingfrom:).md)
  Invoked when all of the data for a given resource is loaded.
- [func webView(WebView!, resource: Any!, didReceive: URLResponse!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didreceive:from:)-22bdg.md)
  Invoked after a resource has been loaded.
- [func webView(WebView!, resource: Any!, didReceiveContentLength: Int, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didreceivecontentlength:from:).md)
  Invoked when some of the data for a given resource has arrived.
- [func webView(WebView!, resource: Any!, didFailLoadingWithError: (any Error)!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didfailloadingwitherror:from:).md)
  Invoked when a resource failed to load.
- [func webView(WebView!, plugInFailedWithError: (any Error)!, dataSource: WebDataSource!)](webresourceloaddelegate/webview(_:pluginfailedwitherror:datasource:).md)
  Invoked when a plug-in fails to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:resource:willsend:redirectresponse:from:))*