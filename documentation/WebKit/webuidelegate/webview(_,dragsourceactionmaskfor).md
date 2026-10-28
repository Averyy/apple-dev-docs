# webView(_:dragSourceActionMaskFor:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a mask indicating which drag-source actions are allowed for a drag that begins at the specified location.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, dragSourceActionMaskFor point: NSPoint) -> Int
```

```objc
- (NSUInteger) webView:(WebView *) webView dragSourceActionMaskForPoint:(NSPoint) point;
```

## Return Value

A mask indicating which drag-source actions are allowed. (Note that the return value changed from an `unsigned int` to an `NSUInteger` in OS X v10.5.) See [`WebDragSourceAction`](../webdragsourceaction.md) for a list of return values.

## Discussion

This method is called after the user has begun a drag from a point in a web view. This method can be invoked multiple times while content is dragged from the sending web view. When the content is dropped, the sender sends [`webView(_:willPerform:from:with:)`](./webview%28_,willperform,from,with%29.md) to the receiver.

If you do not implement this method, it returns `(WebDragSourceActionAny & ~WebDragSourceActionLink)` if the cursor is in an editable part of the web view; otherwise, it returns [`any`](../webdragdestinationaction/any.md).

## Parameters

- `webView`: The web view that sent the message.
- `point`: The point at which the drag began, specified in the coordinates of the web view.

## See Also

### Controlling Drag Behavior
- [func webView(WebView!, dragDestinationActionMaskFor: (any NSDraggingInfo)!) -> Int](./webview%28_,dragdestinationactionmaskfor%29.md)
  Returns a mask indicating which drag operations are allowed by the sender.
- [func webView(WebView!, willPerform: WebDragDestinationAction, for: (any NSDraggingInfo)!)](./webview%28_,willperform,for%29.md)
  Tells the receiver that the sending web view will perform the specified drag-destination action.
- [func webView(WebView!, willPerform: WebDragSourceAction, from: NSPoint, with: NSPasteboard!)](./webview%28_,willperform,from,with%29.md)
  Tells the receiver that the sending web view will perform the specified drag-source action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:dragsourceactionmaskfor:))*