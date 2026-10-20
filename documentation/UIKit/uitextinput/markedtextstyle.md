# markedTextStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
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
var markedTextStyle: [NSAttributedString.Key : Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary<NSString *,id> * markedTextStyle;
```

#### Discussion

Marked text requires a unique visual treatment when displayed to users. See [Style dictionary keys](../style-dictionary-keys.md) for descriptions of the valid keys and values for this dictionary.

## See Also

### Working with marked and selected text
- [var selectedTextRange: UITextRange?](./selectedtextrange.md)
  The range of selected text in a document.
- [var markedTextRange: UITextRange?](./markedtextrange.md)
  The range of currently marked text in a document.
- [func setMarkedText(String?, selectedRange: NSRange)](./setmarkedtext%28_,selectedrange%29.md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](./setattributedmarkedtext%28_,selectedrange%29.md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the currently marked text.
- [var selectionAffinity: UITextStorageDirection](./selectionaffinity.md)
  The desired location for the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/markedtextstyle)*