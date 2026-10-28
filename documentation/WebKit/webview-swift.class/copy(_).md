# copy(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Action method that copies the selected content to the general pasteboard.

**Availability**:
- macOS

## Declaration

```swift
func copy(_ sender: Any?)
```

```objc
- (void) copy:(id) sender;
```

## Discussion

This action method copies the selected content onto the general pasteboard, in as many formats as the receiver supports. For example, a plain text object uses `NSStringPboardType` for plain text, and a rich text object also uses `NSRTFPboardType`.

## Parameters

- `sender`: The object that sent this message.

## See Also

### Cut, Copy and Paste Action Methods
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
- [func pasteAsPlainText(Any?)](./pasteasplaintext%28_%29.md)
  An action method that pastes pasteboard content as plain text.
- [func pasteAsRichText(Any?)](./pasteasrichtext%28_%29.md)
  An action method that pastes pasteboard content into the receiver as rich text, maintaining its attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/copy(_:))*