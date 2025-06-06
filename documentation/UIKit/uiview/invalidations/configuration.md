# UIView.Invalidations.Configuration

**Framework**: UIKit  
**Kind**: struct

A change that invalidates a view’s configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
struct Configuration
```

#### Overview

Use [`configuration`](uiviewinvalidating/configuration.md) to create an instance of this type.

## Topics

### Creating the invalidation structure
- [init()](uiview/invalidations/configuration/init.md)
  Creates a configuration invalidation structure.

## Relationships

### Conforms To
- [UIViewInvalidating](uiviewinvalidating.md)

## See Also

- [UIView.Invalidations.Constraints](uiview/invalidations/constraints.md)
  A change that invalidates a view’s constraints.
- [UIView.Invalidations.Display](uiview/invalidations/display.md)
  A change that requires the system to redraw a view’s content.
- [UIView.Invalidations.IntrinsicContentSize](uiview/invalidations/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [UIView.Invalidations.Layout](uiview/invalidations/layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [UIView.Invalidations.Tuple](uiview/invalidations/tuple.md)
  A change that invalidates a combination of factors covered by the other invalidation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/invalidations/configuration)*