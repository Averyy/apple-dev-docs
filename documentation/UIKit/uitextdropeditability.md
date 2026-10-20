# UITextDropEditability

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The text-drop editability styles for noneditable text views.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum UITextDropEditability
```

```c
enum UITextDropEditability : NSUInteger;
```

## Topics

### Editability styles
- [UITextDropEditability.no](./uitextdropeditability/no.md)
  A text-drop editability specifier indicating that a noneditable text view does not accept drops.
- [UITextDropEditability.temporary](./uitextdropeditability/temporary.md)
  A text-drop editability specifier indicating that a noneditable text view does accept drops but reverts to its noneditable status immediately afterward.
- [UITextDropEditability.yes](./uitextdropeditability/yes.md)
  A text-drop editability specifier indicating that a noneditable text view does accept drops, and that the dropped text remains editable after the drop is finished.
### Initializers
- [init?(rawValue: UInt)](./uitextdropeditability/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Text view additions
- [protocol UITextDragDelegate](./uitextdragdelegate.md)
  The interface for customizing the behavior of a drag activity for a text view.
- [protocol UITextDropDelegate](./uitextdropdelegate.md)
  The interface for configuring a text view’s drop behavior.
- [protocol UITextDraggable](./uitextdraggable.md)
  The interface that determines if a text view is a drag source.
- [struct UITextDragOptions](./uitextdragoptions.md)
  A set of options that determine the behavior of a draggable text view.
- [protocol UITextDroppable](./uitextdroppable.md)
  The interface that determines if a text view is a drop destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropeditability)*