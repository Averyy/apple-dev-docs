# intrinsicContentSize

**Framework**: UIKit  
**Kind**: property

A change that invalidates a view’s intrinsic size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
static var intrinsicContentSize: UIView.Invalidations.IntrinsicContentSize { get }
```

#### Discussion

Use this type of invalidation type to call [`invalidateIntrinsicContentSize()`](uiview/invalidateintrinsiccontentsize().md) when a change in property value invalidates the containing view’s intrinsic content size. When you use this type, the constraint-based layout system accounts for the change the next time it updates the layout.

## See Also

- [static var configuration: UIView.Invalidations.Configuration](uiviewinvalidating/configuration.md)
  A change that invalidates a view’s configuration.
- [static var constraints: UIView.Invalidations.Constraints](uiviewinvalidating/constraints.md)
  A change that invalidates a view’s constraints.
- [static var display: UIView.Invalidations.Display](uiviewinvalidating/display.md)
  A change that requires the system to redraw a view’s content.
- [static var layout: UIView.Invalidations.Layout](uiviewinvalidating/layout.md)
  A change that invalidates the layout of the containing view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewinvalidating/intrinsiccontentsize)*