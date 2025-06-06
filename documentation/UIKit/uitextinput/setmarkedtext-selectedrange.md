# setMarkedText(_:selectedRange:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Inserts the provided text and marks it to indicate that it is part of an active input session.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func setMarkedText(_ markedText: String?, selectedRange: NSRange)
```

#### Discussion

Setting marked text either replaces the existing marked text or, if none is present, inserts it in place of the current selection.

## Parameters

- `markedText`: The text to be marked.
- `selectedRange`: A range within   that indicates the current selection. This range is always relative to  .

## See Also

- [var selectedTextRange: UITextRange?](uitextinput/selectedtextrange.md)
  The range of selected text in a document.
- [var markedTextRange: UITextRange?](uitextinput/markedtextrange.md)
  The range of currently marked text in a document.
- [var markedTextStyle: [NSAttributedString.Key : Any]?](uitextinput/markedtextstyle.md)
  A dictionary of attributes that describes how to draw marked text.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](uitextinput/setattributedmarkedtext(_:selectedrange:).md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](uitextinput/unmarktext.md)
  Unmarks the currently marked text.
- [var selectionAffinity: UITextStorageDirection](uitextinput/selectionaffinity.md)
  The desired location for the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/setmarkedtext(_:selectedrange:))*