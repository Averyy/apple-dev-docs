# directionalPressGestureRecognizer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The underlying gesture recognizer for directional button presses.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+

> **Deprecated**: Configuring the panGestureRecognizer for indirect scrolling automatically supports directional presses now, so this property is no longer useful.

## Declaration

```swift
var directionalPressGestureRecognizer: UIGestureRecognizer { get }
```

```objc
@property (nonatomic, readonly) UIGestureRecognizer * directionalPressGestureRecognizer;
```

## Discussion

The [`directionalPressGestureRecognizer`](./directionalpressgesturerecognizer.md) is disabled by default. If you want to perform scrolling in direct response to up, down, left, and right arrow button presses, instead of scrolling indirectly in response to focus updates, enable this gesture recognizer.

## See Also

### Managing touches
- [func touchesShouldBegin(Set<UITouch>, with: UIEvent?, in: UIView) -> Bool](./touchesshouldbegin%28_,with,in%29.md)
  Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [func touchesShouldCancel(in: UIView) -> Bool](./touchesshouldcancel%28in%29.md)
  Returns whether to cancel touches related to the content subview and start dragging.
- [var canCancelContentTouches: Bool](./cancancelcontenttouches.md)
  A Boolean value that controls whether touches in the content view always lead to tracking.
- [var delaysContentTouches: Bool](./delayscontenttouches.md)
  A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/directionalpressgesturerecognizer)*