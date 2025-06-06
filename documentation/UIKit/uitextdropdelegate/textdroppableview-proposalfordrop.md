# textDroppableView(_:proposalForDrop:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the text view can accept a drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, proposalForDrop drop: any UITextDropRequest) -> UITextDropProposal
```

#### Return Value

A text drop proposal that specifies the behavior of the drop operation.

#### Discussion

This method is called multiple times while the user performs the drag and drop activity. For instance, it’s called when the user drags items into the text view. It’s also called when the text position changes while the user drags items over the text view. If the drag session changes, which happens when the user adds more items to the drag item set, the method is called again.

Because this method is called frequently, it’s important for your implementation to do only what is necessary to return the appropriate drop proposal as quickly as possible.

## Parameters

- `textDroppableView`: The text view that received the drop activity.
- `drop`: The drop request.

## See Also

- [func textDroppableView(any UIView & UITextDroppable, willBecomeEditableForDrop: any UITextDropRequest) -> UITextDropEditability](uitextdropdelegate/textdroppableview(_:willbecomeeditablefordrop:).md)
  Asks the delegate if a noneditable text view can accept a drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:proposalfordrop:))*