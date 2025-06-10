# UITextRange

**Framework**: UIKit  
**Kind**: class

A range of characters in a text container with a starting index and an ending index in string backing a text-entry object.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextRange
```

#### Overview

Classes that adopt the [`UITextInput`](uitextinput.md) protocol must create custom [`UITextRange`](uitextrange.md) objects for representing ranges within the text managed by the class. The starting and ending indexes of the range are represented by [`UITextPosition`](uitextposition.md) objects. The text system uses both [`UITextRange`](uitextrange.md) and [`UITextPosition`](uitextposition.md) objects for communicating text-layout information. There are two reasons for using objects for text ranges rather than primitive types such as [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange-c.struct):

- Some documents contain nested elements (for example, HTML tags and embedded objects) and you need to track both absolute position and position in the visible text.
- The WebKit framework requires that text indexes and offsets be represented by objects.

If you adopt the [`UITextInput`](uitextinput.md) protocol, you must create a custom [`UITextRange`](uitextrange.md) subclass as well as a custom [`UITextPosition`](uitextposition.md) subclass.

## Topics

### Defining Ranges of Text
- [var start: UITextPosition](uitextrange/start.md)
  The start of a range of text.
- [var end: UITextPosition](uitextrange/end.md)
  The end of the range of text.
- [var isEmpty: Bool](uitextrange/isempty.md)
  A Boolean value that indicates whether the range of text represented by the receiver is zero-length.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UITextPosition](uitextposition.md)
  A position in a text container—that is, an index into the backing string in a text-display view.
- [class UITextSelectionRect](uitextselectionrect.md)
  An encapsulation of information about a selected range of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextrange)*