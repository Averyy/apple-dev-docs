# url(from:)

**Framework**: WebKit  
**Kind**: method

Returns a URL from the specified pasteboard.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func url(from pasteboard: NSPasteboard!) -> URL!
```

#### Return Value

The URL from the specified pasteboard or `nil` if there’s no URL on `pasteboard`.

#### Discussion

This method supports multiple pasteboard types including `NSRULPboardType`.

## Parameters

- `pasteboard`: The pasteboard containing a URL.

## See Also

- [class func urlTitle(from: NSPasteboard!) -> String!](webview-swift.class/urltitle(from:).md)
  Returns the title of a URL from the specified pasteboard.
- [func pasteboardTypes(forElement: [AnyHashable : Any]!) -> [Any]!](webview-swift.class/pasteboardtypes(forelement:).md)
  Returns an array of pasteboard types for an element.
- [var pasteboardTypesForSelection: [Any]!](webview-swift.class/pasteboardtypesforselection.md)
  An array of pasteboard types that can be used for the current selection of the receiver.
- [func writeElement([AnyHashable : Any]!, withPasteboardTypes: [Any]!, to: NSPasteboard!)](webview-swift.class/writeelement(_:withpasteboardtypes:to:).md)
  Writes an element to the pasteboard using a list of types.
- [func writeSelection(withPasteboardTypes: [Any]!, to: NSPasteboard!)](webview-swift.class/writeselection(withpasteboardtypes:to:).md)
  Writes the receiver’s current selection to a pasteboard using a list of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/url(from:))*