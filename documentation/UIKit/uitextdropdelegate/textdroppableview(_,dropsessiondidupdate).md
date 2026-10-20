# textDroppableView(_:dropSessionDidUpdate:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the drop session has been updated.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, dropSessionDidUpdate session: any UIDropSession)
```

```objc
- (void) textDroppableView:(UIView<UITextDroppable> *) textDroppableView dropSessionDidUpdate:(id<UIDropSession>) session;
```

#### Discussion

The system usually—but not always—calls this method before calling the [`textDroppableView(_:proposalForDrop:)`](./textdroppableview%28_,proposalfordrop%29.md) method. However, it’s called frequently, so do only what is necessary in your implementation.

## Parameters

- `textDroppableView`: The text view that received the drop activity.
- `session`: The current drop session.

## See Also

### Handling drop session notifications
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidEnter: any UIDropSession)](./textdroppableview%28_,dropsessiondidenter%29.md)
  Tells the delegate that the user has moved the drag items into the coordinate system of the text view.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidExit: any UIDropSession)](./textdroppableview%28_,dropsessiondidexit%29.md)
  Tells the delegate that the user has moved the drag items out of the text view’s coordinate system.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidEnd: any UIDropSession)](./textdroppableview%28_,dropsessiondidend%29.md)
  Tells the delegate that the drop session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:dropsessiondidupdate:))*