# delaysContentTouches

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var delaysContentTouches: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the scroll view delays handling the touch-down gesture until it can determine if scrolling is the intent. If the value is [`false`](https://developer.apple.com/documentation/swift/false) , the scroll view immediately calls [`touchesShouldBegin(_:with:in:)`](uiscrollview/touchesshouldbegin(_:with:in:).md). The default value is [`true`](https://developer.apple.com/documentation/swift/true).

See the class description for a fuller discussion.

## See Also

- [func touchesShouldBegin(Set<UITouch>, with: UIEvent?, in: UIView) -> Bool](uiscrollview/touchesshouldbegin(_:with:in:).md)
  Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [func touchesShouldCancel(in: UIView) -> Bool](uiscrollview/touchesshouldcancel(in:).md)
  Returns whether to cancel touches related to the content subview and start dragging.
- [var canCancelContentTouches: Bool](uiscrollview/cancancelcontenttouches.md)
  A Boolean value that controls whether touches in the content view always lead to tracking.
- [var directionalPressGestureRecognizer: UIGestureRecognizer](uiscrollview/directionalpressgesturerecognizer.md)
  The underlying gesture recognizer for directional button presses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/delayscontenttouches)*