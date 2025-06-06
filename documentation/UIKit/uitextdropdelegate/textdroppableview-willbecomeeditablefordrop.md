# textDroppableView(_:willBecomeEditableForDrop:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if a noneditable text view can accept a drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, willBecomeEditableForDrop drop: any UITextDropRequest) -> UITextDropEditability
```

#### Return Value

A text drop editability style that indicates whether the text view can accept a drop operation.

#### Discussion

By default, a text view that is not editable can’t accept drop requests. However, you can change this behavior by returning the editability style [`UITextDropEditability.temporary`](uitextdropeditability/temporary.md) or [`UITextDropEditability.yes`](uitextdropeditability/yes.md) in your implementation of this method. Not implementing this method is the same as returning the [`UITextDropEditability.no`](uitextdropeditability/no.md) style.

## Parameters

- `textDroppableView`: The text view that received the drop activity.
- `drop`: The drop request.

## See Also

- [func textDroppableView(any UIView & UITextDroppable, proposalForDrop: any UITextDropRequest) -> UITextDropProposal](uitextdropdelegate/textdroppableview(_:proposalfordrop:).md)
  Asks the delegate if the text view can accept a drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:willbecomeeditablefordrop:))*