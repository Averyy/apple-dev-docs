# delaysContentTouches

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var delaysContentTouches: Bool { get set }
```

```objc
@property (nonatomic) BOOL delaysContentTouches;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), the scroll view delays handling the touch-down gesture until it can determine if scrolling is the intent. If the value is [`false`](../../Swift/false.md) , the scroll view immediately calls [`touchesShouldBegin(_:with:in:)`](./touchesshouldbegin%28_,with,in%29.md). The default value is [`true`](../../Swift/true.md).

See the class description for a fuller discussion.

## See Also

### Managing touches
- [func touchesShouldBegin(Set<UITouch>, with: UIEvent?, in: UIView) -> Bool](./touchesshouldbegin%28_,with,in%29.md)
  Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [func touchesShouldCancel(in: UIView) -> Bool](./touchesshouldcancel%28in%29.md)
  Returns whether to cancel touches related to the content subview and start dragging.
- [var canCancelContentTouches: Bool](./cancancelcontenttouches.md)
  A Boolean value that controls whether touches in the content view always lead to tracking.
- [var directionalPressGestureRecognizer: UIGestureRecognizer](./directionalpressgesturerecognizer.md)
  The underlying gesture recognizer for directional button presses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/delayscontenttouches)*