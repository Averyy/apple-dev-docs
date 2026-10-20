# WebFrameLoadDelegate

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
protocol WebFrameLoadDelegate : NSObjectProtocol
```

```objc
@protocol WebFrameLoadDelegate <NSObject>
```

## Topics

### Instance Methods
- [func webView(WebView!, didCancelClientRedirectFor: WebFrame!)](./webframeloaddelegate/webview%28_,didcancelclientredirectfor%29.md)
  Called when a client redirect is cancelled.
- [func webView(WebView!, didChangeLocationWithinPageFor: WebFrame!)](./webframeloaddelegate/webview%28_,didchangelocationwithinpagefor%29.md)
  Called when the scroll position within a frame changes.
- [func webView(WebView!, didClearWindowObject: WebScriptObject!, for: WebFrame!)](./webframeloaddelegate/webview%28_,didclearwindowobject,for%29.md)
  Called when the JavaScript window object in a frame is ready for loading.
- [func webView(WebView!, didCommitLoadFor: WebFrame!)](./webframeloaddelegate/webview%28_,didcommitloadfor%29.md)
  Called when content starts arriving for a page load.
- [func webView(WebView!, didCreateJavaScriptContext: JSContext!, for: WebFrame!)](./webframeloaddelegate/webview%28_,didcreatejavascriptcontext,for%29.md)
  Notifies the delegate that a new JavaScript context has been created.
- [func webView(WebView!, didFailLoadWithError: (any Error)!, for: WebFrame!)](./webframeloaddelegate/webview%28_,didfailloadwitherror,for%29.md)
  Called when an error occurs loading a committed data source.
- [func webView(WebView!, didFailProvisionalLoadWithError: (any Error)!, for: WebFrame!)](./webframeloaddelegate/webview%28_,didfailprovisionalloadwitherror,for%29.md)
  Called if an error occurs when starting to load data for a page.
- [func webView(WebView!, didFinishLoadFor: WebFrame!)](./webframeloaddelegate/webview%28_,didfinishloadfor%29.md)
  Called when a page load completes.
- [func webView(WebView!, didReceiveIcon: NSImage!, for: WebFrame!)](./webframeloaddelegate/webview%28_,didreceiveicon,for%29.md)
  Called when a page icon changes.
- [func webView(WebView!, didReceiveServerRedirectForProvisionalLoadFor: WebFrame!)](./webframeloaddelegate/webview%28_,didreceiveserverredirectforprovisionalloadfor%29.md)
  Called when a provisional data source for a frame receives a server redirect.
- [func webView(WebView!, didReceiveTitle: String!, for: WebFrame!)](./webframeloaddelegate/webview%28_,didreceivetitle,for%29.md)
  Called when the page title of a frame loads or changes.
- [func webView(WebView!, didStartProvisionalLoadFor: WebFrame!)](./webframeloaddelegate/webview%28_,didstartprovisionalloadfor%29.md)
  Called when a page load is in progress in a given frame.
- [func webView(WebView!, willClose: WebFrame!)](./webframeloaddelegate/webview%28_,willclose%29.md)
  Called when a frame will be closed.
- [func webView(WebView!, willPerformClientRedirectTo: URL!, delay: TimeInterval, fire: Date!, for: WebFrame!)](./webframeloaddelegate/webview%28_,willperformclientredirectto,delay,fire,for%29.md)
  Called when a frame receives a client redirect and before it is fired.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with Frames (Legacy)
- [class WebFrame](./webframe.md)
  A `WebFrame` object encapsulates the data displayed in a `WebFrameView` object. There is one `WebFrame` object per frame displayed in a `WebView`. An entire webpage is represented by a hierarchy of `WebFrame` objects in which the root object is called the **main frame**.
- [class WebDataSource](./webdatasource.md)
  `WebDataSource` encapsulates the web content to be displayed in a web frame view. A `WebDataSource` object has a representation object, conforming to the `WebDocumentRepresentation` protocol, that holds the data in an appropriate format depending on the MIME type. You can extend WebKit to support new MIME types by implementing your own view and representation classes, and specifying the mapping between them using the  [`registerClass(_:representationClass:forMIMEType:)`](./webview-swift.class/registerclass%28_,representationclass,formimetype%29.md) `WebView` class method.
- [class WebFrameView](./webframeview.md)
  `WebFrameView` objects and their subviews display the web content contained in a frame. You never create instances of `WebFrameView` directly—`WebView` objects create and manage a hierarchy of `WebFrameView` objects, one for each frame. `WebFrameView` objects use a scroll view whose document view conforms to the [`WebDocumentView`](./webdocumentview.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate)*