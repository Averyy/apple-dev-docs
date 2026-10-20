# bringSubviewToFront(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Moves the specified subview so that it appears on top of its siblings.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func bringSubviewToFront(_ view: UIView)
```

```objc
- (void) bringSubviewToFront:(UIView *) view;
```

#### Discussion

This method moves the specified view to the end of the array of views in the [`subviews`](./subviews.md) property.

## Parameters

- `view`: The subview to move to the front.

## See Also

### Managing the view hierarchy
- [var superview: UIView?](./superview.md)
  The receiver’s superview, or `nil` if it has none.
- [var subviews: [UIView]](./subviews.md)
  The receiver’s immediate subviews.
- [var window: UIWindow?](./window.md)
  The receiver’s window object, or `nil` if it has none.
- [func addSubview(UIView)](./addsubview%28_%29.md)
  Adds a view to the end of the receiver’s list of subviews.
- [func sendSubviewToBack(UIView)](./sendsubviewtoback%28_%29.md)
  Moves the specified subview so that it appears behind its siblings.
- [func removeFromSuperview()](./removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [func insertSubview(UIView, at: Int)](./insertsubview%28_,at%29.md)
  Inserts a subview at the specified index.
- [func insertSubview(UIView, aboveSubview: UIView)](./insertsubview%28_,abovesubview%29.md)
  Inserts a view above another view in the view hierarchy.
- [func insertSubview(UIView, belowSubview: UIView)](./insertsubview%28_,belowsubview%29.md)
  Inserts a view below another view in the view hierarchy.
- [func exchangeSubview(at: Int, withSubviewAt: Int)](./exchangesubview%28at,withsubviewat%29.md)
  Exchanges the subviews at the specified indices.
- [func isDescendant(of: UIView) -> Bool](./isdescendant%28of%29.md)
  Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/bringsubviewtofront(_:))*