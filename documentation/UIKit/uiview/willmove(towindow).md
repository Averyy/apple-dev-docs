# willMove(toWindow:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the view that its window object is about to change.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func willMove(toWindow newWindow: UIWindow?)
```

```objc
- (void) willMoveToWindow:(UIWindow *) newWindow;
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the window changes.

## Parameters

- `newWindow`: The window object that will be at the root of the receiver’s new view hierarchy. This parameter may be `nil`.

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
- [func didMoveToWindow()](./didmovetowindow%28%29.md)
  Tells the view that its window object changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/willmove(towindow:))*