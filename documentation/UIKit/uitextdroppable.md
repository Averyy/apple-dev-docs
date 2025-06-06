# UITextDroppable

**Framework**: UIKit  
**Kind**: protocol

The interface that determines if a text view is a drop destination.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextDroppable : UITextInput, UITextPasteConfigurationSupporting
```

## Topics

### Checking the text drop activity status
- [var isTextDropActive: Bool](uitextdroppable/istextdropactive.md)
  A Boolean value that indicates whether the text view has at least one active drop session.
### Managing the text drop interaction
- [var textDropInteraction: UIDropInteraction?](uitextdroppable/textdropinteraction.md)
  The drop interaction object added by UIKit to the text view.
### Setting the text drop delegate
- [var textDropDelegate: (any UITextDropDelegate)?](uitextdroppable/textdropdelegate.md)
  The text drop delegate for interacting with a drop activity in the text view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIKeyInput](uikeyinput.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UITextInput](uitextinput.md)
- [UITextInputTraits](uitextinputtraits.md)
- [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md)
### Conforming Types
- [UISearchTextField](uisearchtextfield.md)
- [UITextField](uitextfield.md)
- [UITextView](uitextview.md)

## See Also

- [protocol UITextDragDelegate](uitextdragdelegate.md)
  The interface for customizing the behavior of a drag activity for a text view.
- [protocol UITextDropDelegate](uitextdropdelegate.md)
  The interface for configuring a text view’s drop behavior.
- [protocol UITextDraggable](uitextdraggable.md)
  The interface that determines if a text view is a drag source.
- [struct UITextDragOptions](uitextdragoptions.md)
  A set of options that determine the behavior of a draggable text view.
- [enum UITextDropEditability](uitextdropeditability.md)
  The text-drop editability styles for noneditable text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdroppable)*