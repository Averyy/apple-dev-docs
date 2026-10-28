# editableDOMRange(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the editable DOM object located at a given point.

**Availability**:
- macOS

## Declaration

```swift
func editableDOMRange(for point: NSPoint) -> DOMRange!
```

```objc
- (DOMRange *) editableDOMRangeForPoint:(NSPoint) point;
```

## Return Value

A single range object of the editable DOM object located at `point` in the receiver’s coordinates.

## Parameters

- `point`: The location of the editable DOM object.

## See Also

### Related Documentation
- [func setSelectedDOMRange(DOMRange!, affinity: NSSelectionAffinity)](./setselecteddomrange%28_,affinity%29.md)
  Selects a range of nodes.
- [var selectedDOMRange: DOMRange!](./selecteddomrange.md)
  The range of the current selection.
### Getting and Setting Document Editing Attributes
- [var isEditable: Bool](./iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var smartInsertDeleteEnabled: Bool](./smartinsertdeleteenabled.md)
  A Boolean that indicates whether smart-space insertion and deletion is enabled.
- [var isContinuousSpellCheckingEnabled: Bool](./iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var spellCheckerDocumentTag: Int](./spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var undoManager: UndoManager!](./undomanager.md)
  The receiver’s undo manager.
- [var editingDelegate: (any WebEditingDelegate)!](./editingdelegate.md)
  The receiver’s editing delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/editabledomrange(for:))*