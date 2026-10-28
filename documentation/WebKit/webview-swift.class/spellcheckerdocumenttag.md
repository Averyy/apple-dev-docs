# spellCheckerDocumentTag

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The spell-checker document tag for this document.

**Availability**:
- macOS

## Declaration

```swift
var spellCheckerDocumentTag: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger spellCheckerDocumentTag;
```

## Discussion

A tag identifying the receiver’s text as a document for the spell-checker server. See the [`NSSpellChecker`](../../AppKit/nsspellchecker.md) and NSSpellServer class specifications for more information on how this tag is used.

## See Also

### Related Documentation
- [var spellCheckerDocumentTag: Int](../../AppKit/nstextview/spellcheckerdocumenttag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
### Getting and Setting Document Editing Attributes
- [var isEditable: Bool](./iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var smartInsertDeleteEnabled: Bool](./smartinsertdeleteenabled.md)
  A Boolean that indicates whether smart-space insertion and deletion is enabled.
- [var isContinuousSpellCheckingEnabled: Bool](./iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var undoManager: UndoManager!](./undomanager.md)
  The receiver’s undo manager.
- [var editingDelegate: (any WebEditingDelegate)!](./editingdelegate.md)
  The receiver’s editing delegate.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](./editabledomrange%28for%29.md)
  Returns the editable DOM object located at a given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/spellcheckerdocumenttag)*