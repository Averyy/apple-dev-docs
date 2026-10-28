# didMoveToSuperview()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the view that its superview changed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func didMoveToSuperview()
```

```objc
- (void) didMoveToSuperview;
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the superview changes.

## See Also

### Observing view-related changes
- [func didAddSubview(UIView)](./didaddsubview%28_%29.md)
  Tells the view that a subview was added.
- [func willRemoveSubview(UIView)](./willremovesubview%28_%29.md)
  Tells the view that a subview is about to be removed.
- [func willMove(toSuperview: UIView?)](./willmove%28tosuperview%29.md)
  Tells the view that its superview is about to change to the specified superview.
- [func willMove(toWindow: UIWindow?)](./willmove%28towindow%29.md)
  Tells the view that its window object is about to change.
- [func didMoveToWindow()](./didmovetowindow%28%29.md)
  Tells the view that its window object changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/didmovetosuperview())*