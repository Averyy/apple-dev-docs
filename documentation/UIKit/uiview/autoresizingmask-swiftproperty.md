# autoresizingMask

**Framework**: UIKit  
**Kind**: property

An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var autoresizingMask: UIView.AutoresizingMask { get set }
```

#### Discussion

When a view’s bounds change, that view automatically resizes its subviews according to each subview’s autoresizing mask. You specify the value of this mask by combining the constants described in [`UIView.AutoresizingMask`](uiview/autoresizingmask-swift.struct.md) using the C bitwise OR operator. Combining these constants lets you specify which dimensions of the view should grow or shrink relative to the superview. The default value of this property is [`UIViewAutoresizingNone`](uiviewautoresizing/uiviewautoresizingnone.md), which indicates that the view should not be resized at all.

When more than one option along the same axis is set, the default behavior is to distribute the size difference proportionally among the flexible portions. The larger the flexible portion, relative to the other flexible portions, the more it is likely to grow. For example, suppose this property includes the [`flexibleWidth`](uiview/autoresizingmask-swift.struct/flexiblewidth.md) and [`flexibleRightMargin`](uiview/autoresizingmask-swift.struct/flexiblerightmargin.md) constants but does not include the [`flexibleLeftMargin`](uiview/autoresizingmask-swift.struct/flexibleleftmargin.md) constant, thus indicating that the width of the view’s left margin is fixed but that the view’s width and right margin may change. Thus, the view appears anchored to the left side of its superview while both the view width and the gap to the right of the view increase.

If the autoresizing behaviors do not offer the precise layout that you need for your views, you can use a custom container view and override its [`layoutSubviews()`](uiview/layoutsubviews().md) method to position your subviews more precisely.

## See Also

- [var contentMode: UIView.ContentMode](uiview/contentmode-swift.property.md)
  A flag used to determine how a view lays out its content when its bounds change.
- [UIView.ContentMode](uiview/contentmode-swift.enum.md)
  Options to specify how a view adjusts its content when its size changes.
- [func sizeThatFits(CGSize) -> CGSize](uiview/sizethatfits(_:).md)
  Asks the view to calculate and return the size that best fits the specified size.
- [func sizeToFit()](uiview/sizetofit.md)
  Resizes and moves the receiver view so it just encloses its subviews.
- [var autoresizesSubviews: Bool](uiview/autoresizessubviews.md)
  A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/autoresizingmask-swift.property)*