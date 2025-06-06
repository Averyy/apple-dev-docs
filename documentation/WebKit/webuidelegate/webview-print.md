# webView(_:print:)

**Framework**: Webkit  
**Kind**: method

Prints the contents of a web frame view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, print frameView: WebFrameView!)
```

#### Discussion

This method is invoked when a script or a user wants to print a webpage. Typically, the delegate implements this method to prepare the web frame view content for printing. The web frame view can handle some content without intervention by the delegate. Send the [`documentViewShouldHandlePrint`](webframeview/documentviewshouldhandleprint.md) message to the web frame view to determine if it can handle printing. If this method returns [`true`](https://developer.apple.com/documentation/swift/true), then the delegate can print the content by sending the [`printDocumentView()`](webframeview/printdocumentview().md) message to the web frame view. Otherwise, the delegate can use [`printOperation(with:)`](webframeview/printoperation(with:).md) to get an [`NSPrintOperation`](https://developer.apple.com/documentation/AppKit/NSPrintOperation) object to print the web frame view.

## Parameters

- `sender`: The web view that sent the message.
- `frameView`: The web frame view whose contents to print.

## See Also

- [func webViewHeaderHeight(WebView!) -> Float](webuidelegate/webviewheaderheight(_:).md)
  Returns the height of the web view’s printed page header.
- [func webViewFooterHeight(WebView!) -> Float](webuidelegate/webviewfooterheight(_:).md)
  Returns the height of the web view’s printed page footer.
- [func webView(WebView!, drawHeaderIn: NSRect)](webuidelegate/webview(_:drawheaderin:).md)
  Draws the web view’s header in the specified rectangle.
- [func webView(WebView!, drawFooterIn: NSRect)](webuidelegate/webview(_:drawfooterin:).md)
  Draws the web view’s footer in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:print:))*