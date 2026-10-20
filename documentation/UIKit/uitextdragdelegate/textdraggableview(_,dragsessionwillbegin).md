# textDraggableView(_:dragSessionWillBegin:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the text has been lifted out of the text view and the user is beginning to drag the text.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func textDraggableView(_ textDraggableView: any UIView & UITextDraggable, dragSessionWillBegin session: any UIDragSession)
```

```objc
- (void) textDraggableView:(UIView<UITextDraggable> *) textDraggableView dragSessionWillBegin:(id<UIDragSession>) session;
```

## Parameters

- `textDraggableView`: The text view where the drag activity was started.
- `session`: The drag session of the current drag activity.

## See Also

### Handling drag session notifications
- [func textDraggableView(any UIView & UITextDraggable, dragSessionDidEnd: any UIDragSession, with: UIDropOperation)](./textdraggableview%28_,dragsessiondidend,with%29.md)
  Tells the delegate that the drag session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragsessionwillbegin:))*