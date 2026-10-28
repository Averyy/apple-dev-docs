# textDroppableView(_:dropSessionDidEnd:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the drop session has ended.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, dropSessionDidEnd session: any UIDropSession)
```

```objc
- (void) textDroppableView:(UIView<UITextDroppable> *) textDroppableView dropSessionDidEnd:(id<UIDropSession>) session;
```

## Discussion

You implement this method if your delegate needs to do additional cleanup after the drop session has ended.

## Parameters

- `textDroppableView`: The text view that received the drop activity.
- `session`: The drop session that has ended.

## See Also

### Handling drop session notifications
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidEnter: any UIDropSession)](./textdroppableview%28_,dropsessiondidenter%29.md)
  Tells the delegate that the user has moved the drag items into the coordinate system of the text view.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidExit: any UIDropSession)](./textdroppableview%28_,dropsessiondidexit%29.md)
  Tells the delegate that the user has moved the drag items out of the text view’s coordinate system.
- [func textDroppableView(any UIView & UITextDroppable, dropSessionDidUpdate: any UIDropSession)](./textdroppableview%28_,dropsessiondidupdate%29.md)
  Tells the delegate that the drop session has been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:dropsessiondidend:))*