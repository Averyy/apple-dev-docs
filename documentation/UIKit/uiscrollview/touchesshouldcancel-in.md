# touchesShouldCancel(in:)

**Framework**: UIKit  
**Kind**: method

Returns whether to cancel touches related to the content subview and start dragging.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func touchesShouldCancel(in view: UIView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to cancel further touch messages to `view`, [`false`](https://developer.apple.com/documentation/swift/false) to have `view` continue to receive those messages. The default returned value is [`true`](https://developer.apple.com/documentation/swift/true) if `view` is not a [`UIControl`](uicontrol.md) object; otherwise, it returns [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The scroll view calls this method just after it starts sending tracking messages to the content view. If it receives [`false`](https://developer.apple.com/documentation/swift/false) from this method, it stops dragging and forwards the touch events to the content subview. The scroll view doesn’t call this method if the value of the [`canCancelContentTouches`](uiscrollview/cancancelcontenttouches.md) property is [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `view`: The view object in the content that’s being touched.

## See Also

- [func touchesShouldBegin(Set<UITouch>, with: UIEvent?, in: UIView) -> Bool](uiscrollview/touchesshouldbegin(_:with:in:).md)
  Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [var canCancelContentTouches: Bool](uiscrollview/cancancelcontenttouches.md)
  A Boolean value that controls whether touches in the content view always lead to tracking.
- [var delaysContentTouches: Bool](uiscrollview/delayscontenttouches.md)
  A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.
- [var directionalPressGestureRecognizer: UIGestureRecognizer](uiscrollview/directionalpressgesturerecognizer.md)
  The underlying gesture recognizer for directional button presses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/touchesshouldcancel(in:))*