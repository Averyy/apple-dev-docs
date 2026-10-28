# selectionAffinity

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The desired location for the insertion point.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional var selectionAffinity: UITextStorageDirection { get set }
```

```objc
@property (nonatomic) UITextStorageDirection selectionAffinity;
```

## Discussion

For text selections that wrap across line boundaries, this property determines whether the insertion point appears after the last character on the line or before the first character on the following line. The selection affinity is set in response to the user navigating via the keyboard (for example, command-right-arrow). The text input system checks this property when it moves the insertion point around in a document.

In the default implementation, if the selection is not at the end of the line, or if the selection is at the start of a paragraph for an empty line, a forward direction is assumed ([`UITextStorageDirection.forward`](../uitextstoragedirection/forward.md)); otherwise, a backward direction [`UITextStorageDirection.backward`](../uitextstoragedirection/backward.md) is assumed.

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
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the currently marked text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/selectionaffinity)*