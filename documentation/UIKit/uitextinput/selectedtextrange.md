# selectedTextRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The range of selected text in a document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var selectedTextRange: UITextRange? { get set }
```

```objc
@property (copy, readwrite, nullable) UITextRange * selectedTextRange;
```

## Discussion

If the text range has a length, it indicates the currently selected text. If it has zero length, it indicates the caret (insertion point). If the text-range object is `nil`, it indicates that there is no current selection.

## See Also

### Related Documentation
- [var isEmpty: Bool](../uitextrange/isempty.md)
  A Boolean value that indicates whether the range of text represented by the receiver is zero-length.
### Working with marked and selected text
- [var markedTextRange: UITextRange?](./markedtextrange.md)
  The range of currently marked text in a document.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/selectedtextrange)*