# cut(_:)

**Framework**: Webkit  
**Kind**: method

An action method that deletes selected content and puts it on the general pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func cut(_ sender: Any?)
```

#### Discussion

This action method deletes the selected content and places it onto the general pasteboard, in as many formats as the receiver supports. For example, a plain text object uses `NSStringPboardType` for plain text, and a rich text object also uses `NSRTFPboardType`.

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func copy(Any?)](webview/copy(_:).md)
  Action method that copies the selected content to the general pasteboard.
- [func copyFont(Any?)](webview/copyfont(_:).md)
  An action method that copies font information onto the font pasteboard.
- [func delete(Any?)](webview/delete(_:).md)
  An action method that deletes the selected content.
- [func paste(Any?)](webview/paste(_:).md)
  An action method that pastes content from the pasteboard at the insertion point or over the selection.
- [func pasteFont(Any?)](webview/pastefont(_:).md)
  An action method that pastes font information from the font pasteboard.
- [func pasteAsPlainText(Any?)](webview/pasteasplaintext(_:).md)
  An action method that pastes pasteboard content as plain text.
- [func pasteAsRichText(Any?)](webview/pasteasrichtext(_:).md)
  An action method that pastes pasteboard content into the receiver as rich text, maintaining its attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/cut(_:))*