# pasteAsPlainText(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

An action method that pastes pasteboard content as plain text.

**Availability**:
- macOS

## Declaration

```swift
func pasteAsPlainText(_ sender: Any?)
```

```objc
- (void) pasteAsPlainText:(id) sender;
```

## Parameters

- `sender`: The object that sent this message.

## See Also

### Cut, Copy and Paste Action Methods
- [func copy(Any?)](./copy%28_%29.md)
  Action method that copies the selected content to the general pasteboard.
- [func copyFont(Any?)](./copyfont%28_%29.md)
  An action method that copies font information onto the font pasteboard.
- [func cut(Any?)](./cut%28_%29.md)
  An action method that deletes selected content and puts it on the general pasteboard.
- [func delete(Any?)](./delete%28_%29.md)
  An action method that deletes the selected content.
- [func paste(Any?)](./paste%28_%29.md)
  An action method that pastes content from the pasteboard at the insertion point or over the selection.
- [func pasteFont(Any?)](./pastefont%28_%29.md)
  An action method that pastes font information from the font pasteboard.
- [func pasteAsRichText(Any?)](./pasteasrichtext%28_%29.md)
  An action method that pastes pasteboard content into the receiver as rich text, maintaining its attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/pasteasplaintext(_:))*