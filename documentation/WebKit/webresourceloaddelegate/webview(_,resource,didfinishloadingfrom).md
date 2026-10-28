# webView(_:resource:didFinishLoadingFrom:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Invoked when all of the data for a given resource is loaded.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, resource identifier: Any!, didFinishLoadingFrom dataSource: WebDataSource!)
```

```objc
- (void) webView:(WebView *) sender resource:(id) identifier didFinishLoadingFromDataSource:(WebDataSource *) dataSource;
```

## Discussion

The `identifier` parameter is used to track the resource being loaded by `dataSource`. Delegates might implement this method to update the load status of an individual resource.

## Parameters

- `sender`: The web view that sent this message.
- `identifier`: An identifier object used to track the resource being loaded by `dataSource`.
- `dataSource`: The data source for this web view.

## See Also

### Loading Content
- [func webView(WebView!, resource: Any!, willSend: URLRequest!, redirectResponse: URLResponse!, from: WebDataSource!) -> URLRequest!](./webview%28_,resource,willsend,redirectresponse,from%29.md)
  Invoked before a request is initiated for a resource and returns a possibly modified request.
- [func webView(WebView!, resource: Any!, didReceive: URLResponse!, from: WebDataSource!)](./webview%28_,resource,didreceive,from%29-22bdg.md)
  Invoked after a resource has been loaded.
- [func webView(WebView!, resource: Any!, didReceiveContentLength: Int, from: WebDataSource!)](./webview%28_,resource,didreceivecontentlength,from%29.md)
  Invoked when some of the data for a given resource has arrived.
- [func webView(WebView!, resource: Any!, didFailLoadingWithError: (any Error)!, from: WebDataSource!)](./webview%28_,resource,didfailloadingwitherror,from%29.md)
  Invoked when a resource failed to load.
- [func webView(WebView!, plugInFailedWithError: (any Error)!, dataSource: WebDataSource!)](./webview%28_,pluginfailedwitherror,datasource%29.md)
  Invoked when a plug-in fails to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:resource:didfinishloadingfrom:))*