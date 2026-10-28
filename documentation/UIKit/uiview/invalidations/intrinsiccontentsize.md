# UIView.Invalidations.IntrinsicContentSize

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A change that invalidates a view’s intrinsic size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS
- Swift 5.1+

## Declaration

```swift
struct IntrinsicContentSize
```

## Overview

Use [`intrinsicContentSize`](../../uiviewinvalidating/intrinsiccontentsize.md) to create an instance of this type.

## Topics

### Creating the invalidation structure
- [var intrinsicContentSize: CGSize](../intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [init()](./intrinsiccontentsize/init%28%29.md)
  Creates an intrinsic content size invalidation structure.

## Relationships

### Conforms To
- [UIViewInvalidating](../../uiviewinvalidating.md)

## See Also

### Invalidation types
- [UIView.Invalidations.Configuration](./configuration.md)
  A change that invalidates a view’s configuration.
- [UIView.Invalidations.Constraints](./constraints.md)
  A change that invalidates a view’s constraints.
- [UIView.Invalidations.Display](./display.md)
  A change that requires the system to redraw a view’s content.
- [UIView.Invalidations.Layout](./layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [UIView.Invalidations.Tuple](./tuple.md)
  A change that invalidates a combination of factors covered by the other invalidation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/invalidations/intrinsiccontentsize)*