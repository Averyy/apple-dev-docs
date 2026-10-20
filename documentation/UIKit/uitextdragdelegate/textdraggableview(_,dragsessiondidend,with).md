# textDraggableView(_:dragSessionDidEnd:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the drag session has ended.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func textDraggableView(_ textDraggableView: any UIView & UITextDraggable, dragSessionDidEnd session: any UIDragSession, with operation: UIDropOperation)
```

```objc
- (void) textDraggableView:(UIView<UITextDraggable> *) textDraggableView dragSessionDidEnd:(id<UIDragSession>) session withOperation:(UIDropOperation) operation;
```

## Parameters

- `textDraggableView`: The text view where the drag activity was started.
- `session`: The drag session of the current drag activity.
- `operation`: The operation that occurred during the drop activity.

## See Also

### Handling drag session notifications
- [func textDraggableView(any UIView & UITextDraggable, dragSessionWillBegin: any UIDragSession)](./textdraggableview%28_,dragsessionwillbegin%29.md)
  Tells the delegate that the text has been lifted out of the text view and the user is beginning to drag the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragsessiondidend:with:))*