# webViewContentRect:

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a web view window’s content rectangle.

**Availability**:
- macOS 10.3+ - Deprecated in 10.5

> **Deprecated**: Content rectangle calculations are automatic.

## Declaration

```objc
- (NSRect) webViewContentRect:(WebView *) sender;
```

## Return Value

The content rectangle of the window that contains the web view.

## Discussion

The content view is the highest accessible [`NSView`](../../AppKit/nsview.md) object in the view hierarchy displayed in the window. A web view invokes this method instead of setting the content view’s frame directly, allowing delegates to alter the size that is returned.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Moving and Resizing Content Views
- [- webView:setContentRect:](./webview_setcontentrect_.md)
  Sets the window’s content view frame to the specified content rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewcontentrect:)*