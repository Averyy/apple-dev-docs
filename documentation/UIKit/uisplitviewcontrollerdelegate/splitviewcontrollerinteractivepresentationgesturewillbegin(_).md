# splitViewControllerInteractivePresentationGestureWillBegin(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the interactive presentation gesture is about to begin.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func splitViewControllerInteractivePresentationGestureWillBegin(_ svc: UISplitViewController)
```

```objc
- (void) splitViewControllerInteractivePresentationGestureWillBegin:(UISplitViewController *) svc;
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method when the interactive presentation gesture is about to begin. Use this method for performance optimizations related to drawing the column content or other work related to handling the interactive gesture.

## Parameters

- `svc`: The split view controller responding to the interactive presentation gesture.

## See Also

### Handling the presentation gesture
- [func splitViewControllerInteractivePresentationGestureDidEnd(UISplitViewController)](./splitviewcontrollerinteractivepresentationgesturedidend%28_%29.md)
  Tells the delegate when the interactive presentation gesture ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturewillbegin(_:))*