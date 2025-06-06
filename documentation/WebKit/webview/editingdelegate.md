# editingDelegate

**Framework**: Webkit  
**Kind**: property

The receiver’s editing delegate.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var editingDelegate: (any WebEditingDelegate)! { get set }
```

## See Also

- [var isEditable: Bool](webview/iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var smartInsertDeleteEnabled: Bool](webview/smartinsertdeleteenabled.md)
  A Boolean that indicates whether smart-space insertion and deletion is enabled.
- [var isContinuousSpellCheckingEnabled: Bool](webview/iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var spellCheckerDocumentTag: Int](webview/spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var undoManager: UndoManager!](webview/undomanager.md)
  The receiver’s undo manager.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/editingdelegate)*