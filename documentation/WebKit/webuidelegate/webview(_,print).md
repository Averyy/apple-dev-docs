# webView(_:print:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Prints the contents of a web frame view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, print frameView: WebFrameView!)
```

```objc
- (void) webView:(WebView *) sender printFrameView:(WebFrameView *) frameView;
```

#### Discussion

This method is invoked when a script or a user wants to print a webpage. Typically, the delegate implements this method to prepare the web frame view content for printing. The web frame view can handle some content without intervention by the delegate. Send the [`documentViewShouldHandlePrint`](../webframeview/documentviewshouldhandleprint.md) message to the web frame view to determine if it can handle printing. If this method returns [`true`](../../Swift/true.md), then the delegate can print the content by sending the [`printDocumentView()`](../webframeview/printdocumentview%28%29.md) message to the web frame view. Otherwise, the delegate can use [`printOperation(with:)`](../webframeview/printoperation%28with%29.md) to get an [`NSPrintOperation`](../../AppKit/nsprintoperation.md) object to print the web frame view.

## Parameters

- `sender`: The web view that sent the message.
- `frameView`: The web frame view whose contents to print.

## See Also

### Printing
- [func webViewHeaderHeight(WebView!) -> Float](./webviewheaderheight%28_%29.md)
  Returns the height of the web view’s printed page header.
- [func webViewFooterHeight(WebView!) -> Float](./webviewfooterheight%28_%29.md)
  Returns the height of the web view’s printed page footer.
- [func webView(WebView!, drawHeaderIn: NSRect)](./webview%28_,drawheaderin%29.md)
  Draws the web view’s header in the specified rectangle.
- [func webView(WebView!, drawFooterIn: NSRect)](./webview%28_,drawfooterin%29.md)
  Draws the web view’s footer in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:print:))*