# webView:setContentRect:

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the window’s content view frame to the specified content rectangle.

**Availability**:
- macOS 10.3+ - Deprecated in 10.5

> **Deprecated**: Content rectangle calculations are automatic.

## Declaration

```objc
- (void) webView:(WebView *) sender setContentRect:(NSRect) frame;
```

#### Discussion

The content view is the highest accessible [`NSView`](../../AppKit/nsview.md) object in the view hierarchy displayed in the window. A web view invokes this method instead of setting the content view’s frame directly, allowing delegates to augment the behavior by, for example, avoiding auto-saving of the size.

If this method is not implemented by the delegate, then [`webView(_:setFrame:)`](./webview%28_,setframe%29.md) is invoked with the rectangle returned by sending the `NSWindow` method [`frameRect(forContentRect:styleMask:)`](../../AppKit/nswindow/framerect%28forcontentrect,stylemask%29.md) to the window.

## Parameters

- `sender`: The web view that sent the message.
- `frame`: The location and size of the window’s content area.

## See Also

### Moving and Resizing Content Views
- [- webViewContentRect:](./webviewcontentrect_.md)
  Returns a web view window’s content rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview:setcontentrect:)*