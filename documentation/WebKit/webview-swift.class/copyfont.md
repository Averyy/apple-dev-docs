# copyFont(_:)

**Framework**: WebKit  
**Kind**: method

An action method that copies font information onto the font pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func copyFont(_ sender: Any?)
```

#### Discussion

This action method copies the font information for the first character of the selection (or for the insertion point) onto the font pasteboard as `NSFontPboardType`.

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func copy(Any?)](webview-swift.class/copy(_:).md)
  Action method that copies the selected content to the general pasteboard.
- [func cut(Any?)](webview-swift.class/cut(_:).md)
  An action method that deletes selected content and puts it on the general pasteboard.
- [func delete(Any?)](webview-swift.class/delete(_:).md)
  An action method that deletes the selected content.
- [func paste(Any?)](webview-swift.class/paste(_:).md)
  An action method that pastes content from the pasteboard at the insertion point or over the selection.
- [func pasteFont(Any?)](webview-swift.class/pastefont(_:).md)
  An action method that pastes font information from the font pasteboard.
- [func pasteAsPlainText(Any?)](webview-swift.class/pasteasplaintext(_:).md)
  An action method that pastes pasteboard content as plain text.
- [func pasteAsRichText(Any?)](webview-swift.class/pasteasrichtext(_:).md)
  An action method that pastes pasteboard content into the receiver as rich text, maintaining its attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/copyfont(_:))*