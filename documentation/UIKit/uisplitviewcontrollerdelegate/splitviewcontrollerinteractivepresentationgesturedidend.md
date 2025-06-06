# splitViewControllerInteractivePresentationGestureDidEnd(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the interactive presentation gesture ends.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewControllerInteractivePresentationGestureDidEnd(_ svc: UISplitViewController)
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

The split view controller calls this method when the interactive presentation gesture ends. Use this method for performance optimizations related to drawing the column content or other work related to handling the interactive gesture.

## Parameters

- `svc`: The split view controller responding to the interactive presentation gesture.

## See Also

- [func splitViewControllerInteractivePresentationGestureWillBegin(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturewillbegin(_:).md)
  Tells the delegate that the interactive presentation gesture is about to begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturedidend(_:))*