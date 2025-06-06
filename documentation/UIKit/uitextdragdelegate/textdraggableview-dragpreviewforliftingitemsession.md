# textDraggableView(_:dragPreviewForLiftingItem:session:)

**Framework**: Uikit  
**Kind**: method

Asks the delegate for the preview to show during the lift animation that happens when a user begins to drag an item from a text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textDraggableView(_ textDraggableView: any UIView & UITextDraggable, dragPreviewForLiftingItem item: UIDragItem, session: any UIDragSession) -> UITargetedDragPreview?
```

#### Return Value

A targeted drag preview to show during the lift animation, or `nil` to show the default preview.

#### Discussion

You implement this method when you want to show a nondefault preview during the lift animation. If you return `nil`, the system shows default preview.

> **Note**:  This method is not called when the [`suggestedItems`](uitextdragrequest/suggesteditems.md) array for the text drag request contains the drag item.

## Parameters

- `textDraggableView`: The text view where the drag activity was started.
- `item`: The drag item that is being lifted.
- `session`: The drag session of the current drag activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragpreviewforliftingitem:session:))*