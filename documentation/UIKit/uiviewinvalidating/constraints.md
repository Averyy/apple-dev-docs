# constraints

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A change that invalidates a view’s constraints.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS
- Swift 5.1+

## Declaration

```swift
static var constraints: UIView.Invalidations.Constraints { get }
```

Available when `Self` is `UIView.Invalidations.Constraints`.

#### Discussion

Use this invalidation type to call [`setNeedsUpdateConstraints()`](../uiview/setneedsupdateconstraints%28%29.md) when a change in property value should cause the containing view to update constraints.

## See Also

### Specifying invalidation types
- [static var configuration: UIView.Invalidations.Configuration](./configuration.md)
  A change that invalidates a view’s configuration.
- [static var display: UIView.Invalidations.Display](./display.md)
  A change that requires the system to redraw a view’s content.
- [static var intrinsicContentSize: UIView.Invalidations.IntrinsicContentSize](./intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [static var layout: UIView.Invalidations.Layout](./layout.md)
  A change that invalidates the layout of the containing view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewinvalidating/constraints)*