# spellCheckerDocumentTag

**Framework**: WebKit  
**Kind**: property

The spell-checker document tag for this document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var spellCheckerDocumentTag: Int { get }
```

#### Discussion

A tag identifying the receiver’s text as a document for the spell-checker server. See the [`NSSpellChecker`](https://developer.apple.com/documentation/AppKit/NSSpellChecker) and NSSpellServer class specifications for more information on how this tag is used.

## See Also

- [var spellCheckerDocumentTag: Int](../AppKit/NSTextView/spellCheckerDocumentTag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
- [var isEditable: Bool](webview-swift.class/iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var smartInsertDeleteEnabled: Bool](webview-swift.class/smartinsertdeleteenabled.md)
  A Boolean that indicates whether smart-space insertion and deletion is enabled.
- [var isContinuousSpellCheckingEnabled: Bool](webview-swift.class/iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var undoManager: UndoManager!](webview-swift.class/undomanager.md)
  The receiver’s undo manager.
- [var editingDelegate: (any WebEditingDelegate)!](webview-swift.class/editingdelegate.md)
  The receiver’s editing delegate.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview-swift.class/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/spellcheckerdocumenttag)*