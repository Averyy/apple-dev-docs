# toggleContinuousSpellChecking(_:)

**Framework**: Webkit  
**Kind**: method

Toggles whether continuous spell checking is available.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func toggleContinuousSpellChecking(_ sender: Any?)
```

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func replaceSelection(with: DOMNode!)](webview/replaceselection(with:)-5px9m.md)
  Replaces the receiver’s current selection with the specified DOM node.
- [func replaceSelection(withText: String!)](webview/replaceselection(withtext:).md)
  Replaces the current selection with a string of text.
- [func replaceSelection(withMarkupString: String!)](webview/replaceselection(withmarkupstring:).md)
  Replaces the current selection with mixed text and markup.
- [func replaceSelection(with: WebArchive!)](webview/replaceselection(with:)-3vj8l.md)
  Replaces the current selection with an archive’s contents.
- [func deleteSelection()](webview/deleteselection.md)
  Deletes the receiver’s current selection unless it’s collapsed.
- [func moveToBeginningOfSentence(Any?)](webview/movetobeginningofsentence(_:).md)
  Moves the insertion point to the beginning of the current sentence.
- [func moveToBeginningOfSentenceAndModifySelection(Any?)](webview/movetobeginningofsentenceandmodifyselection(_:).md)
  Moves the insertion point and extends the selection to the beginning of the current sentence.
- [func moveToEndOfSentence(Any?)](webview/movetoendofsentence(_:).md)
  Moves the insertion point to the end of the current sentence.
- [func moveToEndOfSentenceAndModifySelection(Any?)](webview/movetoendofsentenceandmodifyselection(_:).md)
  Moves the insertion point and extends the selection to the end of the current sentence.
- [func selectSentence(Any?)](webview/selectsentence(_:).md)
  Selects the entire sentence around the insertion point.
- [func toggleSmartInsertDelete(Any?)](webview/togglesmartinsertdelete(_:).md)
  Toggles whether spaces around selected words are inserted or deleted to preserve proper spacing and punctuation.
- [var canMakeTextStandardSize: Bool](webview/canmaketextstandardsize.md)
  A Boolean that indicates whether the current text size is a multiple of 1.
- [func makeTextStandardSize(Any?)](webview/maketextstandardsize(_:).md)
  Resets the text size to a multiple of 1.
- [var maintainsInactiveSelection: Bool](webview/maintainsinactiveselection.md)
  A Boolean that indicates whether the selection is maintained when focus is lost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/togglecontinuousspellchecking(_:))*