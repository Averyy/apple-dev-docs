# delete(_:)

**Framework**: Webkit  
**Kind**: method

An action method that deletes the selected content.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func delete(_ sender: Any?)
```

#### Discussion

The pasteboard is unaffected by invoking this method.

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func copy(Any?)](webview/copy(_:).md)
  Action method that copies the selected content to the general pasteboard.
- [func copyFont(Any?)](webview/copyfont(_:).md)
  An action method that copies font information onto the font pasteboard.
- [func cut(Any?)](webview/cut(_:).md)
  An action method that deletes selected content and puts it on the general pasteboard.
- [func paste(Any?)](webview/paste(_:).md)
  An action method that pastes content from the pasteboard at the insertion point or over the selection.
- [func pasteFont(Any?)](webview/pastefont(_:).md)
  An action method that pastes font information from the font pasteboard.
- [func pasteAsPlainText(Any?)](webview/pasteasplaintext(_:).md)
  An action method that pastes pasteboard content as plain text.
- [func pasteAsRichText(Any?)](webview/pasteasrichtext(_:).md)
  An action method that pastes pasteboard content into the receiver as rich text, maintaining its attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/delete(_:))*