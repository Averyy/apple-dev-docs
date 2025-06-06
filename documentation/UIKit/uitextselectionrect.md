# UITextSelectionRect

**Framework**: UIKit  
**Kind**: class

An encapsulation of information about a selected range of text in a document.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextSelectionRect
```

#### Overview

This class is an abstract class and must be subclassed to be used. The system text input views provide their own concrete implementations of this class.

##### Subclassing Notes

If you are implementing a custom text input view, you can subclass and use your custom class to return selection-related information. When subclassing, you should override and reimplement all properties. In your custom implementations, do not call `super`.

## Topics

### Accessing the Selection Rectangle
- [var rect: CGRect](uitextselectionrect/rect.md)
  The rectangle that encloses the text selection rectangle’s text range.
### Accessing Text-Related Attributes
- [var writingDirection: NSWritingDirection](uitextselectionrect/writingdirection.md)
  The writing direction of text in the text selection rectangle’s text range.
- [var isVertical: Bool](uitextselectionrect/isvertical.md)
  A Boolean value that indicates whether the text is vertical.
### Determining the Selection Status
- [var containsStart: Bool](uitextselectionrect/containsstart.md)
  A Boolean value that indicates whether the rectangle contains the start of the selection.
- [var containsEnd: Bool](uitextselectionrect/containsend.md)
  A Boolean value that indicates whether the rectangle contains the end of the selection.
### Instance Properties
- [var transform: CGAffineTransform](uitextselectionrect/transform.md)

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
- [class UITextRange](uitextrange.md)
  A range of characters in a text container with a starting index and an ending index in string backing a text-entry object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectionrect)*