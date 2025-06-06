# pasteboardTypesForSelection

**Framework**: Webkit  
**Kind**: property

An array of pasteboard types that can be used for the current selection of the receiver.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var pasteboardTypesForSelection: [Any]! { get }
```

## See Also

- [class func url(from: NSPasteboard!) -> URL!](webview/url(from:).md)
  Returns a URL from the specified pasteboard.
- [class func urlTitle(from: NSPasteboard!) -> String!](webview/urltitle(from:).md)
  Returns the title of a URL from the specified pasteboard.
- [func pasteboardTypes(forElement: [AnyHashable : Any]!) -> [Any]!](webview/pasteboardtypes(forelement:).md)
  Returns an array of pasteboard types for an element.
- [func writeElement([AnyHashable : Any]!, withPasteboardTypes: [Any]!, to: NSPasteboard!)](webview/writeelement(_:withpasteboardtypes:to:).md)
  Writes an element to the pasteboard using a list of types.
- [func writeSelection(withPasteboardTypes: [Any]!, to: NSPasteboard!)](webview/writeselection(withpasteboardtypes:to:).md)
  Writes the receiver’s current selection to a pasteboard using a list of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/pasteboardtypesforselection)*