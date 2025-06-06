# UITextDraggable

**Framework**: UIKit  
**Kind**: protocol

The interface that determines if a text view is a drag source.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextDraggable : UITextInput
```

## Topics

### Checking the text drag activity status
- [var isTextDragActive: Bool](uitextdraggable/istextdragactive.md)
  A Boolean value indicating whether at least one drag session for the text view is active.
### Managing the text drag interaction
- [var textDragInteraction: UIDragInteraction?](uitextdraggable/textdraginteraction.md)
  The drag interaction object added by UIKit to the text view.
### Setting the text drag delegate
- [var textDragDelegate: (any UITextDragDelegate)?](uitextdraggable/textdragdelegate.md)
  A text drag delegate object for customizing the drag source behavior of a text view.
### Setting the text drag options
- [var textDragOptions: UITextDragOptions](uitextdraggable/textdragoptions.md)
  The options for the text drag operation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIKeyInput](uikeyinput.md)
- [UITextInput](uitextinput.md)
- [UITextInputTraits](uitextinputtraits.md)
### Conforming Types
- [UISearchTextField](uisearchtextfield.md)
- [UITextField](uitextfield.md)
- [UITextView](uitextview.md)

## See Also

- [protocol UITextDragDelegate](uitextdragdelegate.md)
  The interface for customizing the behavior of a drag activity for a text view.
- [protocol UITextDropDelegate](uitextdropdelegate.md)
  The interface for configuring a text view’s drop behavior.
- [struct UITextDragOptions](uitextdragoptions.md)
  A set of options that determine the behavior of a draggable text view.
- [protocol UITextDroppable](uitextdroppable.md)
  The interface that determines if a text view is a drop destination.
- [enum UITextDropEditability](uitextdropeditability.md)
  The text-drop editability styles for noneditable text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdraggable)*