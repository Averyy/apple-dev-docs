# textDroppableView(_:dropSessionDidEnter:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user has moved the drag items into the coordinate system of the text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, dropSessionDidEnter session: any UIDropSession)
```

## Parameters

- `textDroppableView`: The text view that received the drop activity.
- `session`: The current drop session.

## See Also

- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidExit: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidexit:).md)
  Tells the delegate that the user has moved the drag items out of the text view’s coordinate system.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidUpdate: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidupdate:).md)
  Tells the delegate that the drop session has been updated.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidEnd: any UIDropSession)](uitextdropdelegate/textdroppableview(_:dropsessiondidend:).md)
  Tells the delegate that the drop session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:dropsessiondidenter:))*