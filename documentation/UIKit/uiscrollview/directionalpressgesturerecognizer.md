# directionalPressGestureRecognizer

**Framework**: UIKit  
**Kind**: property

The underlying gesture recognizer for directional button presses.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var directionalPressGestureRecognizer: UIGestureRecognizer { get }
```

#### Discussion

The [`directionalPressGestureRecognizer`](uiscrollview/directionalpressgesturerecognizer.md) is disabled by default. If you want to perform scrolling in direct response to up, down, left, and right arrow button presses, instead of scrolling indirectly in response to focus updates, enable this gesture recognizer.

## See Also

- [func touchesShouldBegin(Set<UITouch>, with: UIEvent?, in: UIView) -> Bool](uiscrollview/touchesshouldbegin(_:with:in:).md)
  Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [func touchesShouldCancel(in: UIView) -> Bool](uiscrollview/touchesshouldcancel(in:).md)
  Returns whether to cancel touches related to the content subview and start dragging.
- [var canCancelContentTouches: Bool](uiscrollview/cancancelcontenttouches.md)
  A Boolean value that controls whether touches in the content view always lead to tracking.
- [var delaysContentTouches: Bool](uiscrollview/delayscontenttouches.md)
  A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/directionalpressgesturerecognizer)*