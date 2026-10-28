# unmarkText()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Unmarks the currently marked text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func unmarkText()
```

```objc
- (void) unmarkText;
```

## Discussion

After this method is called, the value of [`markedTextRange`](./markedtextrange.md) is `nil`.

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
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](./setattributedmarkedtext%28_,selectedrange%29.md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [var selectionAffinity: UITextStorageDirection](./selectionaffinity.md)
  The desired location for the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/unmarktext())*