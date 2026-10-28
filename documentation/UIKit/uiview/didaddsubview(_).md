# didAddSubview(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the view that a subview was added.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func didAddSubview(_ subview: UIView)
```

```objc
- (void) didAddSubview:(UIView *) subview;
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions when subviews are added. This method is called in response to adding a subview using any of the relevant view methods.

## Parameters

- `subview`: The view that was added as a subview.

## See Also

### Related Documentation
- [func insertSubview(UIView, belowSubview: UIView)](./insertsubview%28_,belowsubview%29.md)
  Inserts a view below another view in the view hierarchy.
- [func insertSubview(UIView, aboveSubview: UIView)](./insertsubview%28_,abovesubview%29.md)
  Inserts a view above another view in the view hierarchy.
- [func addSubview(UIView)](./addsubview%28_%29.md)
  Adds a view to the end of the receiver’s list of subviews.
- [func insertSubview(UIView, at: Int)](./insertsubview%28_,at%29.md)
  Inserts a subview at the specified index.
### Observing view-related changes
- [func willRemoveSubview(UIView)](./willremovesubview%28_%29.md)
  Tells the view that a subview is about to be removed.
- [func willMove(toSuperview: UIView?)](./willmove%28tosuperview%29.md)
  Tells the view that its superview is about to change to the specified superview.
- [func didMoveToSuperview()](./didmovetosuperview%28%29.md)
  Tells the view that its superview changed.
- [func willMove(toWindow: UIWindow?)](./willmove%28towindow%29.md)
  Tells the view that its window object is about to change.
- [func didMoveToWindow()](./didmovetowindow%28%29.md)
  Tells the view that its window object changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/didaddsubview(_:))*