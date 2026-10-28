# exchangeSubview(at:withSubviewAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Exchanges the subviews at the specified indices.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func exchangeSubview(at index1: Int, withSubviewAt index2: Int)
```

```objc
- (void) exchangeSubviewAtIndex:(NSInteger) index1 withSubviewAtIndex:(NSInteger) index2;
```

## Discussion

Each index represents the position of the corresponding view in the array in the [`subviews`](./subviews.md) property. Subview indices start at `0` and cannot be greater than the number of subviews. This method does not change the superview of either view but simply swaps their positions in the [`subviews`](./subviews.md) array.

## Parameters

- `index1`: The index of the first subview in the receiver.
- `index2`: The index of the second subview in the receiver.

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
- [func bringSubviewToFront(UIView)](./bringsubviewtofront%28_%29.md)
  Moves the specified subview so that it appears on top of its siblings.
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
- [func isDescendant(of: UIView) -> Bool](./isdescendant%28of%29.md)
  Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/exchangesubview(at:withsubviewat:))*