# canCancelContentTouches

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls whether touches in the content view always lead to tracking.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canCancelContentTouches: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) and a view in the content has begun tracking a finger touching it, and if the user drags the finger enough to initiate a scroll, the view receives a [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) message and the scroll view handles the touch as a scroll. If the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the scroll view doesn’t scroll regardless of finger movement once the content view starts tracking.

## See Also

- [func touchesShouldBegin(Set<UITouch>, with: UIEvent?, in: UIView) -> Bool](uiscrollview/touchesshouldbegin(_:with:in:).md)
  Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [func touchesShouldCancel(in: UIView) -> Bool](uiscrollview/touchesshouldcancel(in:).md)
  Returns whether to cancel touches related to the content subview and start dragging.
- [var delaysContentTouches: Bool](uiscrollview/delayscontenttouches.md)
  A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.
- [var directionalPressGestureRecognizer: UIGestureRecognizer](uiscrollview/directionalpressgesturerecognizer.md)
  The underlying gesture recognizer for directional button presses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/cancancelcontenttouches)*