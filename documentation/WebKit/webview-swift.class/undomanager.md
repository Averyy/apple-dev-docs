# undoManager

**Framework**: WebKit  
**Kind**: property

The receiver’s undo manager.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var undoManager: UndoManager! { get }
```

## See Also

- [var isEditable: Bool](webview-swift.class/iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var smartInsertDeleteEnabled: Bool](webview-swift.class/smartinsertdeleteenabled.md)
  A Boolean that indicates whether smart-space insertion and deletion is enabled.
- [var isContinuousSpellCheckingEnabled: Bool](webview-swift.class/iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var spellCheckerDocumentTag: Int](webview-swift.class/spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var editingDelegate: (any WebEditingDelegate)!](webview-swift.class/editingdelegate.md)
  The receiver’s editing delegate.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview-swift.class/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/undomanager)*