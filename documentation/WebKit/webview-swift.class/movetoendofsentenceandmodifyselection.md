# moveToEndOfSentenceAndModifySelection(_:)

**Framework**: WebKit  
**Kind**: method

Moves the insertion point and extends the selection to the end of the current sentence.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func moveToEndOfSentenceAndModifySelection(_ sender: Any?)
```

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func replaceSelection(with: DOMNode!)](webview-swift.class/replaceselection(with:)-5px9m.md)
  Replaces the receiver’s current selection with the specified DOM node.
- [func replaceSelection(withText: String!)](webview-swift.class/replaceselection(withtext:).md)
  Replaces the current selection with a string of text.
- [func replaceSelection(withMarkupString: String!)](webview-swift.class/replaceselection(withmarkupstring:).md)
  Replaces the current selection with mixed text and markup.
- [func replaceSelection(with: WebArchive!)](webview-swift.class/replaceselection(with:)-3vj8l.md)
  Replaces the current selection with an archive’s contents.
- [func deleteSelection()](webview-swift.class/deleteselection.md)
  Deletes the receiver’s current selection unless it’s collapsed.
- [func moveToBeginningOfSentence(Any?)](webview-swift.class/movetobeginningofsentence(_:).md)
  Moves the insertion point to the beginning of the current sentence.
- [func moveToBeginningOfSentenceAndModifySelection(Any?)](webview-swift.class/movetobeginningofsentenceandmodifyselection(_:).md)
  Moves the insertion point and extends the selection to the beginning of the current sentence.
- [func moveToEndOfSentence(Any?)](webview-swift.class/movetoendofsentence(_:).md)
  Moves the insertion point to the end of the current sentence.
- [func selectSentence(Any?)](webview-swift.class/selectsentence(_:).md)
  Selects the entire sentence around the insertion point.
- [func toggleContinuousSpellChecking(Any?)](webview-swift.class/togglecontinuousspellchecking(_:).md)
  Toggles whether continuous spell checking is available.
- [func toggleSmartInsertDelete(Any?)](webview-swift.class/togglesmartinsertdelete(_:).md)
  Toggles whether spaces around selected words are inserted or deleted to preserve proper spacing and punctuation.
- [var canMakeTextStandardSize: Bool](webview-swift.class/canmaketextstandardsize.md)
  A Boolean that indicates whether the current text size is a multiple of 1.
- [func makeTextStandardSize(Any?)](webview-swift.class/maketextstandardsize(_:).md)
  Resets the text size to a multiple of 1.
- [var maintainsInactiveSelection: Bool](webview-swift.class/maintainsinactiveselection.md)
  A Boolean that indicates whether the selection is maintained when focus is lost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/movetoendofsentenceandmodifyselection(_:))*