# UITextPosition

**Framework**: UIKit  
**Kind**: class

A position in a text container—that is, an index into the backing string in a text-display view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextPosition
```

#### Overview

Classes that adopt the [`UITextInput`](uitextinput.md) protocol must create custom [`UITextPosition`](uitextposition.md) objects for representing specific locations within the text managed by the class. The text input system uses both these objects and [`UITextRange`](uitextrange.md) objects for communicating text-layout information. There are two reasons for using objects for text positions rather than primitive types such as [`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger):

- Some documents contain nested elements (for example, HTML tags and embedded objects) and you need to track both absolute position and position in the visible text.
- The WebKit framework requires that text indexes and offsets be represented by objects.

The simplest of [`UITextPosition`](uitextposition.md) objects—for example, one used in plain text—might have a single integer property that represents an offset into a string. If you adopt the [`UITextInput`](uitextinput.md) protocol, you must create a custom [`UITextRange`](uitextrange.md) subclass as well as a custom [`UITextPosition`](uitextposition.md) subclass.

This class declares no methods of its own.

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

- [class UITextRange](uitextrange.md)
  A range of characters in a text container with a starting index and an ending index in string backing a text-entry object.
- [class UITextSelectionRect](uitextselectionrect.md)
  An encapsulation of information about a selected range of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextposition)*