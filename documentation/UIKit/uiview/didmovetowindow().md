# didMoveToWindow()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the view that its window object changed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func didMoveToWindow()
```

```objc
- (void) didMoveToWindow;
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the window changes.

The [`window`](./window.md) property may be `nil` by the time that this method is called, indicating that the receiver does not currently reside in any window. This occurs when the receiver has just been removed from its superview or when the receiver has just been added to a superview that is not attached to a window. Overrides of this method may choose to ignore such cases if they are not of interest.

## See Also

### Observing view-related changes
- [func didAddSubview(UIView)](./didaddsubview%28_%29.md)
  Tells the view that a subview was added.
- [func willRemoveSubview(UIView)](./willremovesubview%28_%29.md)
  Tells the view that a subview is about to be removed.
- [func willMove(toSuperview: UIView?)](./willmove%28tosuperview%29.md)
  Tells the view that its superview is about to change to the specified superview.
- [func didMoveToSuperview()](./didmovetosuperview%28%29.md)
  Tells the view that its superview changed.
- [func willMove(toWindow: UIWindow?)](./willmove%28towindow%29.md)
  Tells the view that its window object is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/didmovetowindow())*