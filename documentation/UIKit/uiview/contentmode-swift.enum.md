# UIView.ContentMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Options to specify how a view adjusts its content when its size changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum ContentMode
```

```c
enum UIViewContentMode : NSInteger;
```

## Topics

### Constants
- [UIView.ContentMode.scaleToFill](./contentmode-swift.enum/scaletofill.md)
  The option to scale the content to fit the size of itself by changing the aspect ratio of the content if necessary.
- [UIView.ContentMode.scaleAspectFit](./contentmode-swift.enum/scaleaspectfit.md)
  The option to scale the content to fit the size of the view by maintaining the aspect ratio. Any remaining area of the view’s bounds is transparent.
- [UIView.ContentMode.scaleAspectFill](./contentmode-swift.enum/scaleaspectfill.md)
  The option to scale the content to fill the size of the view. Some portion of the content may be clipped to fill the view’s bounds.
- [UIView.ContentMode.redraw](./contentmode-swift.enum/redraw.md)
  The option to redisplay the view when the bounds change by invoking the [`setNeedsDisplay()`](./setneedsdisplay%28%29.md) method.
- [UIView.ContentMode.center](./contentmode-swift.enum/center.md)
  The option to center the content in the view’s bounds, keeping the proportions the same.
- [UIView.ContentMode.top](./contentmode-swift.enum/top.md)
  The option to center the content aligned at the top in the view’s bounds.
- [UIView.ContentMode.bottom](./contentmode-swift.enum/bottom.md)
  The option to center the content aligned at the bottom in the view’s bounds.
- [UIView.ContentMode.left](./contentmode-swift.enum/left.md)
  The option to align the content on the left of the view.
- [UIView.ContentMode.right](./contentmode-swift.enum/right.md)
  The option to align the content on the right of the view.
- [UIView.ContentMode.topLeft](./contentmode-swift.enum/topleft.md)
  The option to align the content in the top-left corner of the view.
- [UIView.ContentMode.topRight](./contentmode-swift.enum/topright.md)
  The option to align the content in the top-right corner of the view.
- [UIView.ContentMode.bottomLeft](./contentmode-swift.enum/bottomleft.md)
  The option to align the content in the bottom-left corner of the view.
- [UIView.ContentMode.bottomRight](./contentmode-swift.enum/bottomright.md)
  The option to align the content in the bottom-right corner of the view.
### Initializers
- [init?(rawValue: Int)](./contentmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the resizing behavior
- [var contentMode: UIView.ContentMode](./contentmode-swift.property.md)
  A flag used to determine how a view lays out its content when its bounds change.
- [func sizeThatFits(CGSize) -> CGSize](./sizethatfits%28_%29.md)
  Asks the view to calculate and return the size that best fits the specified size.
- [func sizeToFit()](./sizetofit%28%29.md)
  Resizes and moves the receiver view so it just encloses its subviews.
- [var autoresizesSubviews: Bool](./autoresizessubviews.md)
  A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [var autoresizingMask: UIView.AutoresizingMask](./autoresizingmask-swift.property.md)
  An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/contentmode-swift.enum)*