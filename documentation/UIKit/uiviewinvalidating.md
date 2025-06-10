# UIViewInvalidating

**Framework**: UIKit  
**Kind**: protocol

Implements a type of invalidation that can occur on a view that requires an update.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
protocol UIViewInvalidating
```

## Topics

### Specifying invalidation types
- [static var configuration: UIView.Invalidations.Configuration](uiviewinvalidating/configuration.md)
  A change that invalidates a view’s configuration.
- [static var constraints: UIView.Invalidations.Constraints](uiviewinvalidating/constraints.md)
  A change that invalidates a view’s constraints.
- [static var display: UIView.Invalidations.Display](uiviewinvalidating/display.md)
  A change that requires the system to redraw a view’s content.
- [static var intrinsicContentSize: UIView.Invalidations.IntrinsicContentSize](uiviewinvalidating/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [static var layout: UIView.Invalidations.Layout](uiviewinvalidating/layout.md)
  A change that invalidates the layout of the containing view’s subviews.
### Invalidating the view
- [func invalidate(view: UIView)](uiviewinvalidating/invalidate(view:).md)
  Indicates to the system that an aspect of a view is invalid and triggers the necessary update.
- [UIView.Invalidations](uiview/invalidations.md)
  Changes that cause an aspect of a view to be invalid and require an update.
### Type Properties
- [static var properties: UIView.Invalidations.Properties](uiviewinvalidating/properties.md)

## Relationships

### Conforming Types
- [UIView.Invalidations.Configuration](uiview/invalidations/configuration.md)
- [UIView.Invalidations.Constraints](uiview/invalidations/constraints.md)
- [UIView.Invalidations.Display](uiview/invalidations/display.md)
- [UIView.Invalidations.IntrinsicContentSize](uiview/invalidations/intrinsiccontentsize.md)
- [UIView.Invalidations.Layout](uiview/invalidations/layout.md)
- [UIView.Invalidations.Properties](uiview/invalidations/properties.md)
- [UIView.Invalidations.Tuple](uiview/invalidations/tuple.md)

## See Also

- [UIView.Invalidating](uiview/invalidating.md)
  A property wrapper that notifies the system that a property value change has invalidated an aspect of the containing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewinvalidating)*