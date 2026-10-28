# urlTitle(from:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns the title of a URL from the specified pasteboard.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
class func urlTitle(from pasteboard: NSPasteboard!) -> String!
```

```objc
+ (NSString *) URLTitleFromPasteboard:(NSPasteboard *) pasteboard;
```

## Return Value

The title of the URL on `pasteboard`. Returns `nil` if there’s no URL on `pasteboard` or the URL has no title.

## Parameters

- `pasteboard`: The pasteboard containing the URL.

## See Also

### Using the Pasteboard
- [class func url(from: NSPasteboard!) -> URL!](./url%28from%29.md)
  Returns a URL from the specified pasteboard.
- [func pasteboardTypes(forElement: [AnyHashable : Any]!) -> [Any]!](./pasteboardtypes%28forelement%29.md)
  Returns an array of pasteboard types for an element.
- [var pasteboardTypesForSelection: [Any]!](./pasteboardtypesforselection.md)
  An array of pasteboard types that can be used for the current selection of the receiver.
- [func writeElement([AnyHashable : Any]!, withPasteboardTypes: [Any]!, to: NSPasteboard!)](./writeelement%28_,withpasteboardtypes,to%29.md)
  Writes an element to the pasteboard using a list of types.
- [func writeSelection(withPasteboardTypes: [Any]!, to: NSPasteboard!)](./writeselection%28withpasteboardtypes,to%29.md)
  Writes the receiver’s current selection to a pasteboard using a list of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/urltitle(from:))*