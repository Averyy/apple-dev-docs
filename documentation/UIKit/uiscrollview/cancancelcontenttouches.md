# canCancelContentTouches

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether touches in the content view always lead to tracking.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var canCancelContentTouches: Bool { get set }
```

```objc
@property (nonatomic) BOOL canCancelContentTouches;
```

## Discussion

If the value of this property is [`true`](../../Swift/true.md) and a view in the content has begun tracking a finger touching it, and if the user drags the finger enough to initiate a scroll, the view receives a [`touchesCancelled(_:with:)`](../uiresponder/touchescancelled%28_,with%29.md) message and the scroll view handles the touch as a scroll. If the value of this property is [`false`](../../Swift/false.md), the scroll view doesn’t scroll regardless of finger movement once the content view starts tracking.

## See Also

### Managing touches
- [func touchesShouldBegin(Set<UITouch>, with: UIEvent?, in: UIView) -> Bool](./touchesshouldbegin%28_,with,in%29.md)
  Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [func touchesShouldCancel(in: UIView) -> Bool](./touchesshouldcancel%28in%29.md)
  Returns whether to cancel touches related to the content subview and start dragging.
- [var delaysContentTouches: Bool](./delayscontenttouches.md)
  A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.
- [var directionalPressGestureRecognizer: UIGestureRecognizer](./directionalpressgesturerecognizer.md)
  The underlying gesture recognizer for directional button presses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/cancancelcontenttouches)*