# webView(_:contextMenuItemsForElement:defaultMenuItems:)

**Framework**: Webkit  
**Kind**: method

Returns menu items to display in an element’s contextual menu.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, contextMenuItemsForElement element: [AnyHashable : Any]!, defaultMenuItems: [Any]!) -> [Any]!
```

#### Return Value

An array of menu items to display in the element’s contextual menu.

#### Discussion

This method is invoked every time the user clicks the right mouse button, or control-clicks, on an element to reveal a contextual menu. The receiver typically returns a modified copy of the default menu items dictionary, adding and removing menu items as appropriate for this type of element. You can use this mechanism to remove items that are not appropriate for a particular environment or task, such as saving files to the desktop in a web kiosk. You do not need to set the actions and targets of the default items.

## Parameters

- `sender`: The web view that sent the message.
- `element`: A dictionary that describes the element that was clicked. See “Constants” in   for information about the key-value pairs in this dictionary.
- `defaultMenuItems`: The menu items included by default in the element’s contextual menu. See   for values you can use to differentiate among specific menu items.

## See Also

- [func webView(WebView!, mouseDidMoveOverElement: [AnyHashable : Any]!, modifierFlags: Int)](webuidelegate/webview(_:mousedidmoveoverelement:modifierflags:).md)
  Updates information about the element the user is mousing over.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:contextmenuitemsforelement:defaultmenuitems:))*