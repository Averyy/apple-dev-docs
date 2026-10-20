# UIView.Invalidations

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Changes that cause an aspect of a view to be invalid and require an update.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS
- Swift 5.1+

## Declaration

```swift
enum Invalidations
```

## Topics

### Invalidation types
- [UIView.Invalidations.Configuration](./invalidations/configuration.md)
  A change that invalidates a view’s configuration.
- [UIView.Invalidations.Constraints](./invalidations/constraints.md)
  A change that invalidates a view’s constraints.
- [UIView.Invalidations.Display](./invalidations/display.md)
  A change that requires the system to redraw a view’s content.
- [UIView.Invalidations.IntrinsicContentSize](./invalidations/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [UIView.Invalidations.Layout](./invalidations/layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [UIView.Invalidations.Tuple](./invalidations/tuple.md)
  A change that invalidates a combination of factors covered by the other invalidation types.
### Structures
- [UIView.Invalidations.Properties](./invalidations/properties.md)

## See Also

### Invalidating the view
- [func invalidate(view: UIView)](../uiviewinvalidating/invalidate%28view%29.md)
  Indicates to the system that an aspect of a view is invalid and triggers the necessary update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/invalidations)*