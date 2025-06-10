# webView(_:mouseDidMoveOverElement:modifierFlags:)

**Framework**: WebKit  
**Kind**: method

Updates information about the element the user is mousing over.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, mouseDidMoveOverElement elementInformation: [AnyHashable : Any]!, modifierFlags: Int)
```

## Parameters

- `sender`: The web view that sent the message.
- `elementInformation`: A dictionary that describes the element under the mouse, or  . See “Constants” in   for information about the key-value pairs in this dictionary.
- `modifierFlags`: An integer bit field that indicates the modifier keys in effect during the event. See “Modifier Flags” in   for information about possible modifiers. Note that this parameter was changed from an   to an   in OS X v10.5.

## See Also

- [func webView(WebView!, contextMenuItemsForElement: [AnyHashable : Any]!, defaultMenuItems: [Any]!) -> [Any]!](webuidelegate/webview(_:contextmenuitemsforelement:defaultmenuitems:).md)
  Returns menu items to display in an element’s contextual menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:mousedidmoveoverelement:modifierflags:))*