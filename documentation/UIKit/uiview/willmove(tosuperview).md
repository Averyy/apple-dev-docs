# willMove(toSuperview:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the view that its superview is about to change to the specified superview.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func willMove(toSuperview newSuperview: UIView?)
```

```objc
- (void) willMoveToSuperview:(UIView *) newSuperview;
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the superview changes.

## Parameters

- `newSuperview`: A view object that will be the new superview of the receiver. This object may be `nil`.

## See Also

### Observing view-related changes
- [func didAddSubview(UIView)](./didaddsubview%28_%29.md)
  Tells the view that a subview was added.
- [func willRemoveSubview(UIView)](./willremovesubview%28_%29.md)
  Tells the view that a subview is about to be removed.
- [func didMoveToSuperview()](./didmovetosuperview%28%29.md)
  Tells the view that its superview changed.
- [func willMove(toWindow: UIWindow?)](./willmove%28towindow%29.md)
  Tells the view that its window object is about to change.
- [func didMoveToWindow()](./didmovetowindow%28%29.md)
  Tells the view that its window object changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/willmove(tosuperview:))*