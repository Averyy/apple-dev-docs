# url(from:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns a URL from the specified pasteboard.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
class func url(from pasteboard: NSPasteboard!) -> URL!
```

```objc
+ (NSURL *) URLFromPasteboard:(NSPasteboard *) pasteboard;
```

#### Return Value

The URL from the specified pasteboard or `nil` if there’s no URL on `pasteboard`.

#### Discussion

This method supports multiple pasteboard types including `NSRULPboardType`.

## Parameters

- `pasteboard`: The pasteboard containing a URL.

## See Also

### Using the Pasteboard
- [class func urlTitle(from: NSPasteboard!) -> String!](./urltitle%28from%29.md)
  Returns the title of a URL from the specified pasteboard.
- [func pasteboardTypes(forElement: [AnyHashable : Any]!) -> [Any]!](./pasteboardtypes%28forelement%29.md)
  Returns an array of pasteboard types for an element.
- [var pasteboardTypesForSelection: [Any]!](./pasteboardtypesforselection.md)
  An array of pasteboard types that can be used for the current selection of the receiver.
- [func writeElement([AnyHashable : Any]!, withPasteboardTypes: [Any]!, to: NSPasteboard!)](./writeelement%28_,withpasteboardtypes,to%29.md)
  Writes an element to the pasteboard using a list of types.
- [func writeSelection(withPasteboardTypes: [Any]!, to: NSPasteboard!)](./writeselection%28withpasteboardtypes,to%29.md)
  Writes the receiver’s current selection to a pasteboard using a list of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/url(from:))*