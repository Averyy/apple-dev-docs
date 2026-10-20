# undoManager

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s undo manager.

**Availability**:
- macOS

## Declaration

```swift
var undoManager: UndoManager! { get }
```

```objc
@property (nonatomic, strong, readonly) NSUndoManager * undoManager;
```

## See Also

### Getting and Setting Document Editing Attributes
- [var isEditable: Bool](./iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var smartInsertDeleteEnabled: Bool](./smartinsertdeleteenabled.md)
  A Boolean that indicates whether smart-space insertion and deletion is enabled.
- [var isContinuousSpellCheckingEnabled: Bool](./iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var spellCheckerDocumentTag: Int](./spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var editingDelegate: (any WebEditingDelegate)!](./editingdelegate.md)
  The receiver’s editing delegate.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](./editabledomrange%28for%29.md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/undomanager)*