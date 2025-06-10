# editableDOMRange(for:)

**Framework**: WebKit  
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

- [func setSelectedDOMRange(DOMRange!, affinity: NSSelectionAffinity)](webview-swift.class/setselecteddomrange(_:affinity:).md)
  Selects a range of nodes.
- [var selectedDOMRange: DOMRange!](webview-swift.class/selecteddomrange.md)
  The range of the current selection.
- [var isEditable: Bool](webview-swift.class/iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var smartInsertDeleteEnabled: Bool](webview-swift.class/smartinsertdeleteenabled.md)
  A Boolean that indicates whether smart-space insertion and deletion is enabled.
- [var isContinuousSpellCheckingEnabled: Bool](webview-swift.class/iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var spellCheckerDocumentTag: Int](webview-swift.class/spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var undoManager: UndoManager!](webview-swift.class/undomanager.md)
  The receiver’s undo manager.
- [var editingDelegate: (any WebEditingDelegate)!](webview-swift.class/editingdelegate.md)
  The receiver’s editing delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/editabledomrange(for:))*