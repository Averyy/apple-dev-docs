# setMarkedText(_:selectedRange:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Inserts the provided text and marks it to indicate that it is part of an active input session.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func setMarkedText(_ markedText: String?, selectedRange: NSRange)
```

```objc
- (void) setMarkedText:(NSString *) markedText selectedRange:(NSRange) selectedRange;
```

#### Discussion

Setting marked text either replaces the existing marked text or, if none is present, inserts it in place of the current selection.

## Parameters

- `markedText`: The text to be marked.
- `selectedRange`: A range within `markedText` that indicates the current selection. This range is always relative to `markedText`.

## See Also

### Working with marked and selected text
- [var selectedTextRange: UITextRange?](./selectedtextrange.md)
  The range of selected text in a document.
- [var markedTextRange: UITextRange?](./markedtextrange.md)
  The range of currently marked text in a document.
- [var markedTextStyle: [NSAttributedString.Key : Any]?](./markedtextstyle.md)
  A dictionary of attributes that describes how to draw marked text.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](./setattributedmarkedtext%28_,selectedrange%29.md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the currently marked text.
- [var selectionAffinity: UITextStorageDirection](./selectionaffinity.md)
  The desired location for the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/setmarkedtext(_:selectedrange:))*