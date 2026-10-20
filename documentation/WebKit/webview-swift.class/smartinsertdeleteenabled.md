# smartInsertDeleteEnabled

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether smart-space insertion and deletion is enabled.

**Availability**:
- macOS

## Declaration

```swift
var smartInsertDeleteEnabled: Bool { get set }
```

```objc
@property (nonatomic) BOOL smartInsertDeleteEnabled;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver inserts or deletes space around selected words so as to preserve proper spacing and punctuation. [`false`](../../Swift/false.md) if it inserts and deletes exactly what’s selected.

## See Also

### Getting and Setting Document Editing Attributes
- [var isEditable: Bool](./iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var isContinuousSpellCheckingEnabled: Bool](./iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var spellCheckerDocumentTag: Int](./spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var undoManager: UndoManager!](./undomanager.md)
  The receiver’s undo manager.
- [var editingDelegate: (any WebEditingDelegate)!](./editingdelegate.md)
  The receiver’s editing delegate.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](./editabledomrange%28for%29.md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/smartinsertdeleteenabled)*