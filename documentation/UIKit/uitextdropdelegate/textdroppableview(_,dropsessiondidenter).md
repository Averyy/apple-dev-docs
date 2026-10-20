# textDroppableView(_:dropSessionDidEnter:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user has moved the drag items into the coordinate system of the text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, dropSessionDidEnter session: any UIDropSession)
```

```objc
- (void) textDroppableView:(UIView<UITextDroppable> *) textDroppableView dropSessionDidEnter:(id<UIDropSession>) session;
```

## Parameters

- `textDroppableView`: The text view that received the drop activity.
- `session`: The current drop session.

## See Also

### Handling drop session notifications
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidExit: any UIDropSession)](./textdroppableview%28_,dropsessiondidexit%29.md)
  Tells the delegate that the user has moved the drag items out of the text view’s coordinate system.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidUpdate: any UIDropSession)](./textdroppableview%28_,dropsessiondidupdate%29.md)
  Tells the delegate that the drop session has been updated.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidEnd: any UIDropSession)](./textdroppableview%28_,dropsessiondidend%29.md)
  Tells the delegate that the drop session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:dropsessiondidenter:))*