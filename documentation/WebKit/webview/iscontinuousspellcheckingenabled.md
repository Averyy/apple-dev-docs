# isContinuousSpellCheckingEnabled

**Framework**: Webkit  
**Kind**: property

A Boolean that indicates whether the web view has continuous spell-checking enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isContinuousSpellCheckingEnabled: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the object has continuous spell-checking enabled; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isEditable: Bool](webview/iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var smartInsertDeleteEnabled: Bool](webview/smartinsertdeleteenabled.md)
  A Boolean that indicates whether smart-space insertion and deletion is enabled.
- [var spellCheckerDocumentTag: Int](webview/spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var undoManager: UndoManager!](webview/undomanager.md)
  The receiver’s undo manager.
- [var editingDelegate: (any WebEditingDelegate)!](webview/editingdelegate.md)
  The receiver’s editing delegate.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/iscontinuousspellcheckingenabled)*