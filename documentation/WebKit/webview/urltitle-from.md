# urlTitle(from:)

**Framework**: Webkit  
**Kind**: method

Returns the title of a URL from the specified pasteboard.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func urlTitle(from pasteboard: NSPasteboard!) -> String!
```

#### Return Value

The title of the URL on `pasteboard`. Returns `nil` if there’s no URL on `pasteboard` or the URL has no title.

## Parameters

- `pasteboard`: The pasteboard containing the URL.

## See Also

- [class func url(from: NSPasteboard!) -> URL!](webview/url(from:).md)
  Returns a URL from the specified pasteboard.
- [func pasteboardTypes(forElement: [AnyHashable : Any]!) -> [Any]!](webview/pasteboardtypes(forelement:).md)
  Returns an array of pasteboard types for an element.
- [var pasteboardTypesForSelection: [Any]!](webview/pasteboardtypesforselection.md)
  An array of pasteboard types that can be used for the current selection of the receiver.
- [func writeElement([AnyHashable : Any]!, withPasteboardTypes: [Any]!, to: NSPasteboard!)](webview/writeelement(_:withpasteboardtypes:to:).md)
  Writes an element to the pasteboard using a list of types.
- [func writeSelection(withPasteboardTypes: [Any]!, to: NSPasteboard!)](webview/writeselection(withpasteboardtypes:to:).md)
  Writes the receiver’s current selection to a pasteboard using a list of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/urltitle(from:))*