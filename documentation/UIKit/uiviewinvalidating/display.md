# display

**Framework**: UIKit  
**Kind**: property

A change that requires the system to redraw a view’s content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
static var display: UIView.Invalidations.Display { get }
```

#### Discussion

Use this invalidation type to call [`setNeedsDisplay()`](uiview/setneedsdisplay().md) when a change in property value should cause the system to redraw the containing view’s content.

## See Also

- [static var configuration: UIView.Invalidations.Configuration](uiviewinvalidating/configuration.md)
  A change that invalidates a view’s configuration.
- [static var constraints: UIView.Invalidations.Constraints](uiviewinvalidating/constraints.md)
  A change that invalidates a view’s constraints.
- [static var intrinsicContentSize: UIView.Invalidations.IntrinsicContentSize](uiviewinvalidating/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [static var layout: UIView.Invalidations.Layout](uiviewinvalidating/layout.md)
  A change that invalidates the layout of the containing view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewinvalidating/display)*