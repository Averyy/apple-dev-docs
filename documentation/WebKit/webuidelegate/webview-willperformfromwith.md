# webView(_:willPerform:from:with:)

**Framework**: WebKit  
**Kind**: method

Tells the receiver that the sending web view will perform the specified drag-source action.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, willPerform action: WebDragSourceAction, from point: NSPoint, with pasteboard: NSPasteboard!)
```

#### Discussion

This method is invoked after the last invocation of the [`webView(_:dragSourceActionMaskFor:)`](webuidelegate/webview(_:dragsourceactionmaskfor:).md) method, when the dragged content is dropped and the sender is about to perform the drag-source action. The delegate has the opportunity to modify the contents of the object on the pasteboard before completing the drag-source action. No action is taken if you do not implement this method.

## Parameters

- `webView`: The web view that sent the message.
- `action`: The drag-source action to perform. See   for a list of actions.
- `point`: The point at which the drag began, specified in the coordinates of the web view.
- `pasteboard`: The drag pasteboard.

## See Also

- [func webView(WebView!, dragDestinationActionMaskFor: (any NSDraggingInfo)!) -> Int](webuidelegate/webview(_:dragdestinationactionmaskfor:).md)
  Returns a mask indicating which drag operations are allowed by the sender.
- [func webView(WebView!, dragSourceActionMaskFor: NSPoint) -> Int](webuidelegate/webview(_:dragsourceactionmaskfor:).md)
  Returns a mask indicating which drag-source actions are allowed for a drag that begins at the specified location.
- [func webView(WebView!, willPerform: WebDragDestinationAction, for: (any NSDraggingInfo)!)](webuidelegate/webview(_:willperform:for:).md)
  Tells the receiver that the sending web view will perform the specified drag-destination action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:willperform:from:with:))*