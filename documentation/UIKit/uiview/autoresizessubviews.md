# autoresizesSubviews

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var autoresizesSubviews: Bool { get set }
```

```objc
@property (nonatomic) BOOL autoresizesSubviews;
```

## Discussion

When set to [`true`](../../Swift/true.md), the receiver adjusts the size of its subviews when its bounds change. The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring the resizing behavior
- [var contentMode: UIView.ContentMode](./contentmode-swift.property.md)
  A flag used to determine how a view lays out its content when its bounds change.
- [UIView.ContentMode](./contentmode-swift.enum.md)
  Options to specify how a view adjusts its content when its size changes.
- [func sizeThatFits(CGSize) -> CGSize](./sizethatfits%28_%29.md)
  Asks the view to calculate and return the size that best fits the specified size.
- [func sizeToFit()](./sizetofit%28%29.md)
  Resizes and moves the receiver view so it just encloses its subviews.
- [var autoresizingMask: UIView.AutoresizingMask](./autoresizingmask-swift.property.md)
  An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/autoresizessubviews)*