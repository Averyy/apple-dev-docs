# pasteboardTypes(forElement:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of pasteboard types for an element.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
func pasteboardTypes(forElement element: [AnyHashable : Any]!) -> [Any]!
```

```objc
- (NSArray *) pasteboardTypesForElement:(NSDictionary *) element;
```

#### Return Value

An array of pasteboard types for an element.

## Parameters

- `element`: The element whose pasteboard types you want.

## See Also

### Using the Pasteboard
- [class func url(from: NSPasteboard!) -> URL!](./url%28from%29.md)
  Returns a URL from the specified pasteboard.
- [class func urlTitle(from: NSPasteboard!) -> String!](./urltitle%28from%29.md)
  Returns the title of a URL from the specified pasteboard.
- [var pasteboardTypesForSelection: [Any]!](./pasteboardtypesforselection.md)
  An array of pasteboard types that can be used for the current selection of the receiver.
- [func writeElement([AnyHashable : Any]!, withPasteboardTypes: [Any]!, to: NSPasteboard!)](./writeelement%28_,withpasteboardtypes,to%29.md)
  Writes an element to the pasteboard using a list of types.
- [func writeSelection(withPasteboardTypes: [Any]!, to: NSPasteboard!)](./writeselection%28withpasteboardtypes,to%29.md)
  Writes the receiver’s current selection to a pasteboard using a list of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/pasteboardtypes(forelement:))*