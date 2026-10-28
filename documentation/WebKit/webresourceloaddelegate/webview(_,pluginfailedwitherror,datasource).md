# webView(_:plugInFailedWithError:dataSource:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Invoked when a plug-in fails to load.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, plugInFailedWithError error: (any Error)!, dataSource: WebDataSource!)
```

```objc
- (void) webView:(WebView *) sender plugInFailedWithError:(NSError *) error dataSource:(WebDataSource *) dataSource;
```

## Discussion

This method might be invoked if a plug-in is not found, fails to load, or is not available for some reason. Delegates might implement this method to display or log a detailed error message. If you do not implement this method, no action is taken.

## Parameters

- `sender`: The web view that sent this message.
- `error`: The error that occurred during the process of loading that resource.

  The `userInfo` dictionary of `error` may contain additional information about the failure. If the `userInfo` dictionary is not `nil`, it may contain some or all of these key-value pairs. The value of the `NSErrorFailingURLKey` key is a URL string of the `SRC` attribute. The value of the [`WebKitErrorPlugInNameKey`](../webkiterrorpluginnamekey.md) key is a string containing the plug-in’s name. The value for the [`WebKitErrorPlugInPageURLStringKey`](../webkiterrorpluginpageurlstringkey.md) key is a URL string of the `PLUGINSPAGE` attribute. The value of the [`WebKitErrorMIMETypeKey`](../webkiterrormimetypekey.md) key is a string of the `TYPE` attribute.
- `dataSource`: The data source for this web view.

## See Also

### Loading Content
- [func webView(WebView!, resource: Any!, willSend: URLRequest!, redirectResponse: URLResponse!, from: WebDataSource!) -> URLRequest!](./webview%28_,resource,willsend,redirectresponse,from%29.md)
  Invoked before a request is initiated for a resource and returns a possibly modified request.
- [func webView(WebView!, resource: Any!, didFinishLoadingFrom: WebDataSource!)](./webview%28_,resource,didfinishloadingfrom%29.md)
  Invoked when all of the data for a given resource is loaded.
- [func webView(WebView!, resource: Any!, didReceive: URLResponse!, from: WebDataSource!)](./webview%28_,resource,didreceive,from%29-22bdg.md)
  Invoked after a resource has been loaded.
- [func webView(WebView!, resource: Any!, didReceiveContentLength: Int, from: WebDataSource!)](./webview%28_,resource,didreceivecontentlength,from%29.md)
  Invoked when some of the data for a given resource has arrived.
- [func webView(WebView!, resource: Any!, didFailLoadingWithError: (any Error)!, from: WebDataSource!)](./webview%28_,resource,didfailloadingwitherror,from%29.md)
  Invoked when a resource failed to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:pluginfailedwitherror:datasource:))*