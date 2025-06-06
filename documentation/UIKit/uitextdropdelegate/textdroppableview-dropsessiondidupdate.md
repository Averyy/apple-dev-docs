# textDroppableView(_:dropSessionDidUpdate:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the drop session has been updated.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, dropSessionDidUpdate session: any UIDropSession)
```

#### Discussion

The system usually—but not always—calls this method before calling the [`textDroppableView(_:proposalForDrop:)`](uitextdropdelegate/textdroppableview(_:proposalfordrop:).md) method. However, it’s called frequently, so do only what is necessary in your implementation.

## Parameters

- `textDroppableView`: The text view that received the drop activity.
- `session`: The current drop session.

## See Also

- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidEnter: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidenter:).md)
  Tells the delegate that the user has moved the drag items into the coordinate system of the text view.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidExit: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidexit:).md)
  Tells the delegate that the user has moved the drag items out of the text view’s coordinate system.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidEnd: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidend:).md)
  Tells the delegate that the drop session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:dropsessiondidupdate:))*