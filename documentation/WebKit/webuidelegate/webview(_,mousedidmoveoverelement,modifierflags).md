# webView(_:mouseDidMoveOverElement:modifierFlags:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Updates information about the element the user is mousing over.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, mouseDidMoveOverElement elementInformation: [AnyHashable : Any]!, modifierFlags: Int)
```

```objc
- (void) webView:(WebView *) sender mouseDidMoveOverElement:(NSDictionary *) elementInformation modifierFlags:(NSUInteger) modifierFlags;
```

## Parameters

- `sender`: The web view that sent the message.
- `elementInformation`: A dictionary that describes the element under the mouse, or `nil`. See “Constants” in [`WebView`](../webview-swift.class.md) for information about the key-value pairs in this dictionary.
- `modifierFlags`: An integer bit field that indicates the modifier keys in effect during the event. See “Modifier Flags” in [`NSEvent`](../../AppKit/nsevent.md) for information about possible modifiers. Note that this parameter was changed from an `unsigned int` to an `NSUInteger` in OS X v10.5.

## See Also

### Handling Mouse Events
- [func webView(WebView!, contextMenuItemsForElement: [AnyHashable : Any]!, defaultMenuItems: [Any]!) -> [Any]!](./webview%28_,contextmenuitemsforelement,defaultmenuitems%29.md)
  Returns menu items to display in an element’s contextual menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:mousedidmoveoverelement:modifierflags:))*