# markedTextRange

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The range of currently marked text in a document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var markedTextRange: UITextRange? { get }
```

#### Discussion

If there is no marked text, the value of the property is `nil`. Marked text is provisionally inserted text that requires user confirmation; it occurs in multistage text input. The current selection, which can be a caret or an extended range, always occurs within the marked text.

## See Also

- [var selectedTextRange: UITextRange?](uitextinput/selectedtextrange.md)
  The range of selected text in a document.
- [var markedTextStyle: [NSAttributedString.Key : Any]?](uitextinput/markedtextstyle.md)
  A dictionary of attributes that describes how to draw marked text.
- [func setMarkedText(String?, selectedRange: NSRange)](uitextinput/setmarkedtext(_:selectedrange:).md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](uitextinput/setattributedmarkedtext(_:selectedrange:).md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](uitextinput/unmarktext.md)
  Unmarks the currently marked text.
- [var selectionAffinity: UITextStorageDirection](uitextinput/selectionaffinity.md)
  The desired location for the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/markedtextrange)*