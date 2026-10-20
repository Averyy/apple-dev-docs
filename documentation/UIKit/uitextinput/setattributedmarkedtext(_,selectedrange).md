# setAttributedMarkedText(_:selectedRange:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Inserts the provided styled text and marks it to indicate that it is part of an active input session.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func setAttributedMarkedText(_ markedText: NSAttributedString?, selectedRange: NSRange)
```

```objc
- (void) setAttributedMarkedText:(NSAttributedString *) markedText selectedRange:(NSRange) selectedRange;
```

## See Also

### Working with marked and selected text
- [var selectedTextRange: UITextRange?](./selectedtextrange.md)
  The range of selected text in a document.
- [var markedTextRange: UITextRange?](./markedtextrange.md)
  The range of currently marked text in a document.
- [var markedTextStyle: [NSAttributedString.Key : Any]?](./markedtextstyle.md)
  A dictionary of attributes that describes how to draw marked text.
- [func setMarkedText(String?, selectedRange: NSRange)](./setmarkedtext%28_,selectedrange%29.md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the currently marked text.
- [var selectionAffinity: UITextStorageDirection](./selectionaffinity.md)
  The desired location for the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/setattributedmarkedtext(_:selectedrange:))*