# editingDelegate

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s editing delegate.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var editingDelegate: (any WebEditingDelegate)! { get set }
```

```objc
@property (nonatomic, assign) id<WebEditingDelegate> editingDelegate;
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
- [var undoManager: UndoManager!](./undomanager.md)
  The receiver’s undo manager.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](./editabledomrange%28for%29.md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/editingdelegate)*