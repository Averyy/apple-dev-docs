# isEditable

**Framework**: WebKit  
**Kind**: property

A Boolean that indicates whether the user is allowed to edit the document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isEditable: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver allows the user to edit the HTML document, [`false`](https://developer.apple.com/documentation/Swift/false) if it doesn’t.

You can change the receiver’s document programmatically regardless of this setting.

Normally, an HTML document is not editable unless the elements within the document are editable. This property provides a low-level way to make the contents of a `WebView` object editable without altering the document or DOM structure.

## See Also

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
- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview-swift.class/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/iseditable)*