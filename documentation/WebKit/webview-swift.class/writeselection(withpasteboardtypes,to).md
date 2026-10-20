# writeSelection(withPasteboardTypes:to:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Writes the receiver’s current selection to a pasteboard using a list of types.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
func writeSelection(withPasteboardTypes types: [Any]!, to pasteboard: NSPasteboard!)
```

```objc
- (void) writeSelectionWithPasteboardTypes:(NSArray *) types toPasteboard:(NSPasteboard *) pasteboard;
```

## Parameters

- `types`: The pasteboard types to use for the selection.
- `pasteboard`: The pasteboard to use for writing.

## See Also

### Using the Pasteboard
- [class func url(from: NSPasteboard!) -> URL!](./url%28from%29.md)
  Returns a URL from the specified pasteboard.
- [class func urlTitle(from: NSPasteboard!) -> String!](./urltitle%28from%29.md)
  Returns the title of a URL from the specified pasteboard.
- [func pasteboardTypes(forElement: [AnyHashable : Any]!) -> [Any]!](./pasteboardtypes%28forelement%29.md)
  Returns an array of pasteboard types for an element.
- [var pasteboardTypesForSelection: [Any]!](./pasteboardtypesforselection.md)
  An array of pasteboard types that can be used for the current selection of the receiver.
- [func writeElement([AnyHashable : Any]!, withPasteboardTypes: [Any]!, to: NSPasteboard!)](./writeelement%28_,withpasteboardtypes,to%29.md)
  Writes an element to the pasteboard using a list of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/writeselection(withpasteboardtypes:to:))*