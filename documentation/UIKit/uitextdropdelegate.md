# UITextDropDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for configuring a text view’s drop behavior.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextDropDelegate : NSObjectProtocol
```

## Topics

### Accepting a drop activity
- [func textDroppableView(any UIView & UITextDroppable, proposalForDrop: any UITextDropRequest) -> UITextDropProposal](uitextdropdelegate/textdroppableview(_:proposalfordrop:).md)
  Asks the delegate if the text view can accept a drop operation.
- [func textDroppableView(any UIView & UITextDroppable, willBecomeEditableForDrop: any UITextDropRequest) -> UITextDropEditability](uitextdropdelegate/textdroppableview(_:willbecomeeditablefordrop:).md)
  Asks the delegate if a noneditable text view can accept a drop operation.
### Handling drop session notifications
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidEnter: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidenter:).md)
  Tells the delegate that the user has moved the drag items into the coordinate system of the text view.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidExit: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidexit:).md)
  Tells the delegate that the user has moved the drag items out of the text view’s coordinate system.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidUpdate: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidupdate:).md)
  Tells the delegate that the drop session has been updated.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidEnd: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidend:).md)
  Tells the delegate that the drop session has ended.
### Handling drop activity notifications
- [func textDroppableView(any UIView & UITextDroppable, willPerformDrop: any UITextDropRequest)](uitextdropdelegate/textdroppableview(_:willperformdrop:).md)
  Tells the delegate that the drop operation is about to happen.
### Providing a custom preview for a drop activity
- [func textDroppableView(any UIView & UITextDroppable, previewForDroppingAllItemsWithDefault: UITargetedDragPreview) -> UITargetedDragPreview?](uitextdropdelegate/textdroppableview(_:previewfordroppingallitemswithdefault:).md)
  Asks the delegate for the preview to show during the drop animation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UITextDragDelegate](uitextdragdelegate.md)
  The interface for customizing the behavior of a drag activity for a text view.
- [protocol UITextDraggable](uitextdraggable.md)
  The interface that determines if a text view is a drag source.
- [struct UITextDragOptions](uitextdragoptions.md)
  A set of options that determine the behavior of a draggable text view.
- [protocol UITextDroppable](uitextdroppable.md)
  The interface that determines if a text view is a drop destination.
- [enum UITextDropEditability](uitextdropeditability.md)
  The text-drop editability styles for noneditable text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropdelegate)*