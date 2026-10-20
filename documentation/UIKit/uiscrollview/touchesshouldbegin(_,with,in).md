# touchesShouldBegin(_:with:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func touchesShouldBegin(_ touches: Set<UITouch>, with event: UIEvent?, in view: UIView) -> Bool
```

```objc
- (BOOL) touchesShouldBegin:(NSSet<UITouch *> *) touches withEvent:(UIEvent *) event inContentView:(UIView *) view;
```

#### Return Value

Return [`false`](../../Swift/false.md) if you don’t want the scroll view to send event messages to `view`. If you want `view` to receive those messages, return [`true`](../../Swift/true.md) (the default).

#### Discussion

The default behavior of [`UIScrollView`](../uiscrollview.md) is to invoke the [`UIResponder`](../uiresponder.md) event-handling methods of the target subview that the touches occur in.

## Parameters

- `touches`: A set of [`UITouch`](../uitouch.md) instances that represent the touches for the starting phase of the event represented by `event`.
- `event`: An object representing the event to which the touch objects in `touches` belong.
- `view`: The subview in the content where the touch-down gesture occurred.

## See Also

### Managing touches
- [func touchesShouldCancel(in: UIView) -> Bool](./touchesshouldcancel%28in%29.md)
  Returns whether to cancel touches related to the content subview and start dragging.
- [var canCancelContentTouches: Bool](./cancancelcontenttouches.md)
  A Boolean value that controls whether touches in the content view always lead to tracking.
- [var delaysContentTouches: Bool](./delayscontenttouches.md)
  A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.
- [var directionalPressGestureRecognizer: UIGestureRecognizer](./directionalpressgesturerecognizer.md)
  The underlying gesture recognizer for directional button presses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/touchesshouldbegin(_:with:in:))*