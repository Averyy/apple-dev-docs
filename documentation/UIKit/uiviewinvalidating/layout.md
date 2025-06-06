# layout

**Framework**: UIKit  
**Kind**: property

A change that invalidates the layout of the containing view’s subviews.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
static var layout: UIView.Invalidations.Layout { get }
```

#### Discussion

Use this invalidation type to call [`setNeedsLayout()`](uiview/setneedslayout().md) when a change in property value should cause an update to the layout of the containing view’s subviews.

## See Also

- [static var configuration: UIView.Invalidations.Configuration](uiviewinvalidating/configuration.md)
  A change that invalidates a view’s configuration.
- [static var constraints: UIView.Invalidations.Constraints](uiviewinvalidating/constraints.md)
  A change that invalidates a view’s constraints.
- [static var display: UIView.Invalidations.Display](uiviewinvalidating/display.md)
  A change that requires the system to redraw a view’s content.
- [static var intrinsicContentSize: UIView.Invalidations.IntrinsicContentSize](uiviewinvalidating/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewinvalidating/layout)*