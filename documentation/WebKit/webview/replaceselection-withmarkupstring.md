# replaceSelection(withMarkupString:)

**Framework**: Webkit  
**Kind**: method

Replaces the current selection with mixed text and markup.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func replaceSelection(withMarkupString markupString: String!)
```

#### Discussion

If the current selection is collapsed (a range is selected with the same nodes and offsets for the start and end) then no content is removed when inserting the markup, and the selection is collapsed and moved to the end of the inserted content. If no content is selected, the markup is not inserted.

See [`HTML Clipboard Format`](https://developer.apple.comhttp://msdn.microsoft.com/en-us/library/aa767917.aspx) for a specification of the supported HTML markup.

## Parameters

- `markupString`: The markup string that replaces the current selection.

## See Also

- [func replaceSelection(with: DOMNode!)](webview/replaceselection(with:)-5px9m.md)
  Replaces the receiver’s current selection with the specified DOM node.
- [func replaceSelection(withText: String!)](webview/replaceselection(withtext:).md)
  Replaces the current selection with a string of text.
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
- [func toggleContinuousSpellChecking(Any?)](webview/togglecontinuousspellchecking(_:).md)
  Toggles whether continuous spell checking is available.
- [func toggleSmartInsertDelete(Any?)](webview/togglesmartinsertdelete(_:).md)
  Toggles whether spaces around selected words are inserted or deleted to preserve proper spacing and punctuation.
- [var canMakeTextStandardSize: Bool](webview/canmaketextstandardsize.md)
  A Boolean that indicates whether the current text size is a multiple of 1.
- [func makeTextStandardSize(Any?)](webview/maketextstandardsize(_:).md)
  Resets the text size to a multiple of 1.
- [var maintainsInactiveSelection: Bool](webview/maintainsinactiveselection.md)
  A Boolean that indicates whether the selection is maintained when focus is lost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/replaceselection(withmarkupstring:))*