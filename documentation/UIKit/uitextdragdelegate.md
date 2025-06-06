# UITextDragDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for customizing the behavior of a drag activity for a text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextDragDelegate : NSObjectProtocol
```

## Topics

### Handling drag session notifications
- [func textDraggableView(any UIView & UITextDraggable, dragSessionWillBegin: any UIDragSession)](uitextdragdelegate/textdraggableview(_:dragsessionwillbegin:).md)
  Tells the delegate that the text has been lifted out of the text view and the user is beginning to drag the text.
- [func textDraggableView(any UIView & UITextDraggable, dragSessionDidEnd: any UIDragSession, with: UIDropOperation)](uitextdragdelegate/textdraggableview(_:dragsessiondidend:with:).md)
  Tells the delegate that the drag session has ended.
### Providing additional animations
- [func textDraggableView(any UIView & UITextDraggable, willAnimateLiftWith: any UIDragAnimating, session: any UIDragSession)](uitextdragdelegate/textdraggableview(_:willanimateliftwith:session:).md)
  Tells the delegate when the lift animation is about to begin, and gives you a chance to animate additional changes alongside the system animation.
### Providing custom drag items
- [func textDraggableView(any UIView & UITextDraggable, itemsForDrag: any UITextDragRequest) -> [UIDragItem]](uitextdragdelegate/textdraggableview(_:itemsfordrag:).md)
  Asks the delegate for custom drag items from a text view.
### Providing a custom preview for a drag activity
- [func textDraggableView(any UIView & UITextDraggable, dragPreviewForLiftingItem: UIDragItem, session: any UIDragSession) -> UITargetedDragPreview?](uitextdragdelegate/textdraggableview(_:dragpreviewforliftingitem:session:).md)
  Asks the delegate for the preview to show during the lift animation that happens when a user begins to drag an item from a text view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UITextDropDelegate](uitextdropdelegate.md)
  The interface for configuring a text view’s drop behavior.
- [protocol UITextDraggable](uitextdraggable.md)
  The interface that determines if a text view is a drag source.
- [struct UITextDragOptions](uitextdragoptions.md)
  A set of options that determine the behavior of a draggable text view.
- [protocol UITextDroppable](uitextdroppable.md)
  The interface that determines if a text view is a drop destination.
- [enum UITextDropEditability](uitextdropeditability.md)
  The text-drop editability styles for noneditable text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragdelegate)*