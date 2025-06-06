# textDraggableView(_:dragSessionWillBegin:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the text has been lifted out of the text view and the user is beginning to drag the text.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textDraggableView(_ textDraggableView: any UIView & UITextDraggable, dragSessionWillBegin session: any UIDragSession)
```

## Parameters

- `textDraggableView`: The text view where the drag activity was started.
- `session`: The drag session of the current drag activity.

## See Also

- [func textDraggableView(any UIView & UITextDraggable, dragSessionDidEnd: any UIDragSession, with: UIDropOperation)](uitextdragdelegate/textdraggableview(_:dragsessiondidend:with:).md)
  Tells the delegate that the drag session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragsessionwillbegin:))*