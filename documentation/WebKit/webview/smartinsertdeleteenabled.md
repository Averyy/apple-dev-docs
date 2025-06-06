# smartInsertDeleteEnabled

**Framework**: Webkit  
**Kind**: property

A Boolean that indicates whether smart-space insertion and deletion is enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var smartInsertDeleteEnabled: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver inserts or deletes space around selected words so as to preserve proper spacing and punctuation. [`false`](https://developer.apple.com/documentation/swift/false) if it inserts and deletes exactly what’s selected.

## See Also

- [var isEditable: Bool](webview/iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var isContinuousSpellCheckingEnabled: Bool](webview/iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var spellCheckerDocumentTag: Int](webview/spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var undoManager: UndoManager!](webview/undomanager.md)
  The receiver’s undo manager.
- [var editingDelegate: (any WebEditingDelegate)!](webview/editingdelegate.md)
  The receiver’s editing delegate.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/smartinsertdeleteenabled)*