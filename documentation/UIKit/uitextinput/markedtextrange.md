# markedTextRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The range of currently marked text in a document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var markedTextRange: UITextRange? { get }
```

```objc
@property (nonatomic, readonly, nullable) UITextRange * markedTextRange;
```

## Discussion

If there is no marked text, the value of the property is `nil`. Marked text is provisionally inserted text that requires user confirmation; it occurs in multistage text input. The current selection, which can be a caret or an extended range, always occurs within the marked text.

## See Also

### Working with marked and selected text
- [var selectedTextRange: UITextRange?](./selectedtextrange.md)
  The range of selected text in a document.
- [var markedTextStyle: [NSAttributedString.Key : Any]?](./markedtextstyle.md)
  A dictionary of attributes that describes how to draw marked text.
- [func setMarkedText(String?, selectedRange: NSRange)](./setmarkedtext%28_,selectedrange%29.md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](./setattributedmarkedtext%28_,selectedrange%29.md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the currently marked text.
- [var selectionAffinity: UITextStorageDirection](./selectionaffinity.md)
  The desired location for the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/markedtextrange)*