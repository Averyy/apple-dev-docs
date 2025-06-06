# writeElement(_:withPasteboardTypes:to:)

**Framework**: Webkit  
**Kind**: method

Writes an element to the pasteboard using a list of types.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func writeElement(_ element: [AnyHashable : Any]!, withPasteboardTypes types: [Any]!, to pasteboard: NSPasteboard!)
```

## Parameters

- `element`: The element to write to the pasteboard.
- `types`: The pasteboard types to use for the element.
- `pasteboard`: The pasteboard to use for writing.

## See Also

- [class func url(from: NSPasteboard!) -> URL!](webview/url(from:).md)
  Returns a URL from the specified pasteboard.
- [class func urlTitle(from: NSPasteboard!) -> String!](webview/urltitle(from:).md)
  Returns the title of a URL from the specified pasteboard.
- [func pasteboardTypes(forElement: [AnyHashable : Any]!) -> [Any]!](webview/pasteboardtypes(forelement:).md)
  Returns an array of pasteboard types for an element.
- [var pasteboardTypesForSelection: [Any]!](webview/pasteboardtypesforselection.md)
  An array of pasteboard types that can be used for the current selection of the receiver.
- [func writeSelection(withPasteboardTypes: [Any]!, to: NSPasteboard!)](webview/writeselection(withpasteboardtypes:to:).md)
  Writes the receiver’s current selection to a pasteboard using a list of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/writeelement(_:withpasteboardtypes:to:))*