# WebResourceLoadDelegate

**Framework**: WebKit  
**Kind**: protocol

Web view resource load delegates implement this protocol to be notified on the progress of loading individual resources. Note that there can be hundreds of resources, such as images and other media, per page. So, if you just want to get page loading status see the WebFrameLoadDelegate protocol.

**Availability**:
- macOS 10.3+

## Declaration

```swift
protocol WebResourceLoadDelegate : NSObjectProtocol
```

#### Overview

There’s a separate client request and server response made for each resource on a page. By implementing the [`webView(_:identifierForInitialRequest:from:)`](webresourceloaddelegate/webview(_:identifierforinitialrequest:from:).md) method, resource load delegates provide a tracking object used to identify individual resources in subsequent calls to delegate methods. Delegates are then notified when resource loading starts, when data is incrementally received, when any load errors occur, and when the load is complete. Delegates may also change a request before it is sent. In some cases, depending on the page content and server redirects, methods defined in this protocol may be invoked multiple times (see individual method descriptions for more details). All the methods in this protocol are optional.

## Topics

### Setting Identifiers
- [func webView(WebView!, identifierForInitialRequest: URLRequest!, from: WebDataSource!) -> Any!](webresourceloaddelegate/webview(_:identifierforinitialrequest:from:).md)
  Returns an identifier object used to track the progress of loading a single resource.
### Loading Content
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
- [func webView(WebView!, plugInFailedWithError: (any Error)!, dataSource: WebDataSource!)](webresourceloaddelegate/webview(_:pluginfailedwitherror:datasource:).md)
  Invoked when a plug-in fails to load.
### Authenticating Resources
- [func webView(WebView!, resource: Any!, didReceive: URLAuthenticationChallenge!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didreceive:from:)-54xbd.md)
  Invoked when an authentication challenge has been received for a resource.
- [func webView(WebView!, resource: Any!, didCancel: URLAuthenticationChallenge!, from: WebDataSource!)](webresourceloaddelegate/webview(_:resource:didcancel:from:).md)
  Invoked when an authentication challenge for a resource was canceled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WebResource](webresource.md)
  A `WebResource` object represents a downloaded URL. It encapsulates the data of the download as well as other resource properties such as the URL, MIME type, and frame name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate)*