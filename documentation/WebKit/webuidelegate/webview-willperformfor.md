# webView(_:willPerform:for:)

**Framework**: WebKit  
**Kind**: method

Tells the receiver that the sending web view will perform the specified drag-destination action.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, willPerform action: WebDragDestinationAction, for draggingInfo: (any NSDraggingInfo)!)
```

#### Discussion

This method is invoked after the last invocation of the [`webView(_:dragDestinationActionMaskFor:)`](webuidelegate/webview(_:dragdestinationactionmaskfor:).md) method, when the dragged content is dropped and the sender is about to perform the destination action. No action is taken if you do not implement this method.

## Parameters

- `webView`: The web view that sent the message.
- `action`: The drag-destination action to perform. See   for a list of actions.
- `draggingInfo`: The information object for the dragging operation.

## See Also

- [func webView(WebView!, dragDestinationActionMaskFor: (any NSDraggingInfo)!) -> Int](webuidelegate/webview(_:dragdestinationactionmaskfor:).md)
  Returns a mask indicating which drag operations are allowed by the sender.
- [func webView(WebView!, dragSourceActionMaskFor: NSPoint) -> Int](webuidelegate/webview(_:dragsourceactionmaskfor:).md)
  Returns a mask indicating which drag-source actions are allowed for a drag that begins at the specified location.
- [func webView(WebView!, willPerform: WebDragSourceAction, from: NSPoint, with: NSPasteboard!)](webuidelegate/webview(_:willperform:from:with:).md)
  Tells the receiver that the sending web view will perform the specified drag-source action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:willperform:for:))*