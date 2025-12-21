# smartInsertDeleteEnabled

**Framework**: WebKit  
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

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver inserts or deletes space around selected words so as to preserve proper spacing and punctuation. [`false`](https://developer.apple.com/documentation/Swift/false) if it inserts and deletes exactly what’s selected.

## See Also

- [var isEditable: Bool](webview-swift.class/iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var isContinuousSpellCheckingEnabled: Bool](webview-swift.class/iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var spellCheckerDocumentTag: Int](webview-swift.class/spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var undoManager: UndoManager!](webview-swift.class/undomanager.md)
  The receiver’s undo manager.
- [var editingDelegate: (any WebEditingDelegate)!](webview-swift.class/editingdelegate.md)
  The receiver’s editing delegate.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview-swift.class/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/smartinsertdeleteenabled)*