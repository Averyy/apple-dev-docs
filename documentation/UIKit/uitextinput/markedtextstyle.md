# markedTextStyle

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A dictionary of attributes that describes how to draw marked text.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var markedTextStyle: [NSAttributedString.Key : Any]? { get set }
```

#### Discussion

Marked text requires a unique visual treatment when displayed to users. See [`Style dictionary keys`](style-dictionary-keys.md) for descriptions of the valid keys and values for this dictionary.

## See Also

- [var selectedTextRange: UITextRange?](uitextinput/selectedtextrange.md)
  The range of selected text in a document.
- [var markedTextRange: UITextRange?](uitextinput/markedtextrange.md)
  The range of currently marked text in a document.
- [func setMarkedText(String?, selectedRange: NSRange)](uitextinput/setmarkedtext(_:selectedrange:).md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](uitextinput/setattributedmarkedtext(_:selectedrange:).md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](uitextinput/unmarktext.md)
  Unmarks the currently marked text.
- [var selectionAffinity: UITextStorageDirection](uitextinput/selectionaffinity.md)
  The desired location for the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/markedtextstyle)*