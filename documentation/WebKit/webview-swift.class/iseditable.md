# isEditable

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the user is allowed to edit the document.

**Availability**:
- macOS

## Declaration

```swift
var isEditable: Bool { get set }
```

```objc
@property (nonatomic, getter=isEditable) BOOL editable;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver allows the user to edit the HTML document, [`false`](../../Swift/false.md) if it doesn’t.

You can change the receiver’s document programmatically regardless of this setting.

Normally, an HTML document is not editable unless the elements within the document are editable. This property provides a low-level way to make the contents of a `WebView` object editable without altering the document or DOM structure.

## See Also

### Getting and Setting Document Editing Attributes
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
- [func editableDOMRange(for: NSPoint) -> DOMRange!](./editabledomrange%28for%29.md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/iseditable)*