# webView(_:dragDestinationActionMaskFor:)

**Framework**: WebKit  
**Kind**: method

Returns a mask indicating which drag operations are allowed by the sender.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, dragDestinationActionMaskFor draggingInfo: (any NSDraggingInfo)!) -> Int
```

#### Return Value

A mask that indicates which drag operations are allowed when content is dragged over the sending web view. (Note that the return value changed from an `unsigned int` to an `NSUInteger` in OS X v10.5.) See [`WebDragDestinationAction`](webdragdestinationaction.md) for a list of return values.

#### Discussion

This method can be invoked multiple times while content is dragged over the sending web view. When the content is dropped, the web view sends a notification ([`webView(_:willPerform:for:)`](webuidelegate/webview(_:willperform:for:).md)) to the receiver.

If you do not implement this method, it returns [`any`](webdragdestinationaction/any.md) by default.

## Parameters

- `webView`: The web view that sent the message.
- `draggingInfo`: The information object for the dragging operation.

## See Also

- [func webView(WebView!, dragSourceActionMaskFor: NSPoint) -> Int](webuidelegate/webview(_:dragsourceactionmaskfor:).md)
  Returns a mask indicating which drag-source actions are allowed for a drag that begins at the specified location.
- [func webView(WebView!, willPerform: WebDragDestinationAction, for: (any NSDraggingInfo)!)](webuidelegate/webview(_:willperform:for:).md)
  Tells the receiver that the sending web view will perform the specified drag-destination action.
- [func webView(WebView!, willPerform: WebDragSourceAction, from: NSPoint, with: NSPasteboard!)](webuidelegate/webview(_:willperform:from:with:).md)
  Tells the receiver that the sending web view will perform the specified drag-source action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:dragdestinationactionmaskfor:))*