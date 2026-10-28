# maintainsInactiveSelection

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the selection is maintained when focus is lost.

**Availability**:
- macOS

## Declaration

```swift
var maintainsInactiveSelection: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL maintainsInactiveSelection;
```

## Discussion

[`true`](../../Swift/true.md) if the selection is maintained when focus is lost; otherwise, [`false`](../../Swift/false.md).

## See Also

### Editing Documents
- [func replaceSelection(with: DOMNode!)](./replaceselection%28with%29-5px9m.md)
  Replaces the receiver’s current selection with the specified DOM node.
- [func replaceSelection(withText: String!)](./replaceselection%28withtext%29.md)
  Replaces the current selection with a string of text.
- [func replaceSelection(withMarkupString: String!)](./replaceselection%28withmarkupstring%29.md)
  Replaces the current selection with mixed text and markup.
- [func replaceSelection(with: WebArchive!)](./replaceselection%28with%29-3vj8l.md)
  Replaces the current selection with an archive’s contents.
- [func deleteSelection()](./deleteselection%28%29.md)
  Deletes the receiver’s current selection unless it’s collapsed.
- [func moveToBeginningOfSentence(Any?)](./movetobeginningofsentence%28_%29.md)
  Moves the insertion point to the beginning of the current sentence.
- [func moveToBeginningOfSentenceAndModifySelection(Any?)](./movetobeginningofsentenceandmodifyselection%28_%29.md)
  Moves the insertion point and extends the selection to the beginning of the current sentence.
- [func moveToEndOfSentence(Any?)](./movetoendofsentence%28_%29.md)
  Moves the insertion point to the end of the current sentence.
- [func moveToEndOfSentenceAndModifySelection(Any?)](./movetoendofsentenceandmodifyselection%28_%29.md)
  Moves the insertion point and extends the selection to the end of the current sentence.
- [func selectSentence(Any?)](./selectsentence%28_%29.md)
  Selects the entire sentence around the insertion point.
- [func toggleContinuousSpellChecking(Any?)](./togglecontinuousspellchecking%28_%29.md)
  Toggles whether continuous spell checking is available.
- [func toggleSmartInsertDelete(Any?)](./togglesmartinsertdelete%28_%29.md)
  Toggles whether spaces around selected words are inserted or deleted to preserve proper spacing and punctuation.
- [var canMakeTextStandardSize: Bool](./canmaketextstandardsize.md)
  A Boolean that indicates whether the current text size is a multiple of 1.
- [func makeTextStandardSize(Any?)](./maketextstandardsize%28_%29.md)
  Resets the text size to a multiple of 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/maintainsinactiveselection)*