# UIView.Invalidations.Tuple

**Framework**: UIKit  
**Kind**: struct

A change that invalidates a combination of factors covered by the other invalidation types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
struct Tuple<Invalidation1, Invalidation2> where Invalidation1 : UIViewInvalidating, Invalidation2 : UIViewInvalidating
```

#### Overview

The system uses this type when a change invalidates multiple aspects of a view. Use a tuple of the static values defined in [`UIViewInvalidating`](uiviewinvalidating.md) when more than one invalidation type applies to a change.

## Topics

### Creating the invalidation structure
- [init(Invalidation1, Invalidation2)](uiview/invalidations/tuple/init(_:_:).md)
  Creates an invalidation structure with multiple invalidations.

## Relationships

### Conforms To
- [UIViewInvalidating](uiviewinvalidating.md)

## See Also

- [UIView.Invalidations.Configuration](uiview/invalidations/configuration.md)
  A change that invalidates a view’s configuration.
- [UIView.Invalidations.Constraints](uiview/invalidations/constraints.md)
  A change that invalidates a view’s constraints.
- [UIView.Invalidations.Display](uiview/invalidations/display.md)
  A change that requires the system to redraw a view’s content.
- [UIView.Invalidations.IntrinsicContentSize](uiview/invalidations/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [UIView.Invalidations.Layout](uiview/invalidations/layout.md)
  A change that invalidates the layout of the containing view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/invalidations/tuple)*