# subviews

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s immediate subviews.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var subviews: [UIView] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<__kindof UIView *> * subviews;
```

## Discussion

You can use this property to retrieve the subviews associated with your custom view hierarchies. The order of the subviews in the array reflects their visible order on the screen, with the view at index 0 being the back-most view.

For complex views declared in UIKit and other system frameworks, any subviews of the view are generally considered private and subject to change at any time. Therefore, you should not attempt to retrieve or modify subviews for these types of system-supplied views. If you do, your code may break during a future system update.

## See Also

### Managing the view hierarchy
- [var superview: UIView?](./superview.md)
  The receiver’s superview, or `nil` if it has none.
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
- [func exchangeSubview(at: Int, withSubviewAt: Int)](./exchangesubview%28at,withsubviewat%29.md)
  Exchanges the subviews at the specified indices.
- [func isDescendant(of: UIView) -> Bool](./isdescendant%28of%29.md)
  Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/subviews)*