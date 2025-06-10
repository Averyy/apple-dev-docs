# webView(_:plugInFailedWithError:dataSource:)

**Framework**: WebKit  
**Kind**: method

Invoked when a plug-in fails to load.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, plugInFailedWithError error: (any Error)!, dataSource: WebDataSource!)
```

#### Discussion

This method might be invoked if a plug-in is not found, fails to load, or is not available for some reason. Delegates might implement this method to display or log a detailed error message. If you do not implement this method, no action is taken.

## Parameters

- `sender`: The web view that sent this message.
- `error`: The   dictionary of   may contain additional information about the failure. If the   dictionary is not  , it may contain some or all of these key-value pairs. The value of the   key is a URL string of the   attribute. The value of the   key is a string containing the plug-in’s name. The value for the   key is a URL string of the   attribute. The value of the   key is a string of the   attribute.
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
- [func webView(WebView!, resource: Any!, didFailLoadingWithError: (any Error)!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didfailloadingwitherror:from:).md)
  Invoked when a resource failed to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:pluginfailedwitherror:datasource:))*