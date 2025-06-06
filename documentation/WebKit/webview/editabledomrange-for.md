# editableDOMRange(for:)

**Framework**: Webkit  
**Kind**: method

Returns the editable DOM object located at a given point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func editableDOMRange(for point: NSPoint) -> DOMRange!
```

#### Return Value

A single range object of the editable DOM object located at `point` in the receiver’s coordinates.

## Parameters

- `point`: The location of the editable DOM object.

## See Also

- [func setSelectedDOMRange(DOMRange!, affinity: NSSelectionAffinity)](webview/setselecteddomrange(_:affinity:).md)
  Selects a range of nodes.
- [var selectedDOMRange: DOMRange!](webview/selecteddomrange.md)
  The range of the current selection.
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
- [var editingDelegate: (any WebEditingDelegate)!](webview/editingdelegate.md)
  The receiver’s editing delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/editabledomrange(for:))*