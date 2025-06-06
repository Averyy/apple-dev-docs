# UITextDragRequest

**Framework**: UIKit  
**Kind**: protocol

The interface for describing the attributes of a drag activity originating in a text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextDragRequest : NSObjectProtocol
```

## Topics

### Getting the drag items
- [var existingItems: [UIDragItem]](uitextdragrequest/existingitems.md)
  The array of drag items present in a drag session.
- [var suggestedItems: [UIDragItem]](uitextdragrequest/suggesteditems.md)
  An array of drag items that the system provides when the text drag delegate doesn’t provide custom drag items.
### Getting information about the text
- [var dragRange: UITextRange](uitextdragrequest/dragrange.md)
  A range of text associated with a drag item in an active drag session that originated in a text view.
- [var isSelected: Bool](uitextdragrequest/isselected.md)
  A Boolean value indicating whether text is selected for dragging.
### Getting the drag session
- [var dragSession: any UIDragSession](uitextdragrequest/dragsession.md)
  The active drag session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UITextDragPreviewRenderer](uitextdragpreviewrenderer.md)
  Renders previews of text dragged by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragrequest)*