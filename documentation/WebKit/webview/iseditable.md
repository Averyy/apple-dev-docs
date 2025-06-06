# isEditable

**Framework**: Webkit  
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

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver allows the user to edit the HTML document, [`false`](https://developer.apple.com/documentation/swift/false) if it doesn’t.

You can change the receiver’s document programmatically regardless of this setting.

Normally, an HTML document is not editable unless the elements within the document are editable. This property provides a low-level way to make the contents of a `WebView` object editable without altering the document or DOM structure.

## See Also

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
- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/iseditable)*