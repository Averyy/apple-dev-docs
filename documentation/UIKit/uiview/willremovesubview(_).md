# willRemoveSubview(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the view that a subview is about to be removed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func willRemoveSubview(_ subview: UIView)
```

```objc
- (void) willRemoveSubview:(UIView *) subview;
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever subviews are removed. This method is called when the subview’s superview changes or when the subview is removed from the view hierarchy completely.

## Parameters

- `subview`: The subview that will be removed.

## See Also

### Related Documentation
- [func removeFromSuperview()](./removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
### Observing view-related changes
- [func didAddSubview(UIView)](./didaddsubview%28_%29.md)
  Tells the view that a subview was added.
- [func willMove(toSuperview: UIView?)](./willmove%28tosuperview%29.md)
  Tells the view that its superview is about to change to the specified superview.
- [func didMoveToSuperview()](./didmovetosuperview%28%29.md)
  Tells the view that its superview changed.
- [func willMove(toWindow: UIWindow?)](./willmove%28towindow%29.md)
  Tells the view that its window object is about to change.
- [func didMoveToWindow()](./didmovetowindow%28%29.md)
  Tells the view that its window object changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/willremovesubview(_:))*