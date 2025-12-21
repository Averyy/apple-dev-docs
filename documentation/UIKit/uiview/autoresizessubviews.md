# autoresizesSubviews

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var autoresizesSubviews: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/Swift/true), the receiver adjusts the size of its subviews when its bounds change. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var contentMode: UIView.ContentMode](uiview/contentmode-swift.property.md)
  A flag used to determine how a view lays out its content when its bounds change.
- [UIView.ContentMode](uiview/contentmode-swift.enum.md)
  Options to specify how a view adjusts its content when its size changes.
- [func sizeThatFits(CGSize) -> CGSize](uiview/sizethatfits(_:).md)
  Asks the view to calculate and return the size that best fits the specified size.
- [func sizeToFit()](uiview/sizetofit.md)
  Resizes and moves the receiver view so it just encloses its subviews.
- [var autoresizingMask: UIView.AutoresizingMask](uiview/autoresizingmask-swift.property.md)
  An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/autoresizessubviews)*