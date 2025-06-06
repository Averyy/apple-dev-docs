# subviews

**Framework**: UIKit  
**Kind**: property

The receiver’s immediate subviews.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var subviews: [UIView] { get }
```

#### Discussion

You can use this property to retrieve the subviews associated with your custom view hierarchies. The order of the subviews in the array reflects their visible order on the screen, with the view at index 0 being the back-most view.

For complex views declared in UIKit and other system frameworks, any subviews of the view are generally considered private and subject to change at any time. Therefore, you should not attempt to retrieve or modify subviews for these types of system-supplied views. If you do, your code may break during a future system update.

## See Also

- [var superview: UIView?](uiview/superview.md)
  The receiver’s superview, or `nil` if it has none.
- [var window: UIWindow?](uiview/window.md)
  The receiver’s window object, or `nil` if it has none.
- [func addSubview(UIView)](uiview/addsubview(_:).md)
  Adds a view to the end of the receiver’s list of subviews.
- [func bringSubviewToFront(UIView)](uiview/bringsubviewtofront(_:).md)
  Moves the specified subview so that it appears on top of its siblings.
- [func sendSubviewToBack(UIView)](uiview/sendsubviewtoback(_:).md)
  Moves the specified subview so that it appears behind its siblings.
- [func removeFromSuperview()](uiview/removefromsuperview.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [func insertSubview(UIView, at: Int)](uiview/insertsubview(_:at:).md)
  Inserts a subview at the specified index.
- [func insertSubview(UIView, aboveSubview: UIView)](uiview/insertsubview(_:abovesubview:).md)
  Inserts a view above another view in the view hierarchy.
- [func insertSubview(UIView, belowSubview: UIView)](uiview/insertsubview(_:belowsubview:).md)
  Inserts a view below another view in the view hierarchy.
- [func exchangeSubview(at: Int, withSubviewAt: Int)](uiview/exchangesubview(at:withsubviewat:).md)
  Exchanges the subviews at the specified indices.
- [func isDescendant(of: UIView) -> Bool](uiview/isdescendant(of:).md)
  Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/subviews)*