# contentMode

**Framework**: UIKit  
**Kind**: property

A flag used to determine how a view lays out its content when its bounds change.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var contentMode: UIView.ContentMode { get set }
```

#### Discussion

The content mode specifies how the cached bitmap of the view’s layer is adjusted when the view’s bounds change. This property is often used to implement resizable controls. Instead of redrawing the contents of the view every time, you can use this property to specify that you want to scale the contents (either with or without distortion) or pin them to a particular spot on the view.

> **Note**:  You can always force the contents of a view to be redrawn by calling the [`setNeedsDisplay()`](uiview/setneedsdisplay().md) or [`setNeedsDisplay(_:)`](uiview/setneedsdisplay(_:).md) method.

For a list of values you can assign to this property, see [`UIView.ContentMode`](uiview/contentmode-swift.enum.md). The default value of this property is [`UIView.ContentMode.scaleToFill`](uiview/contentmode-swift.enum/scaletofill.md).

## See Also

- [UIView.ContentMode](uiview/contentmode-swift.enum.md)
  Options to specify how a view adjusts its content when its size changes.
- [func sizeThatFits(CGSize) -> CGSize](uiview/sizethatfits(_:).md)
  Asks the view to calculate and return the size that best fits the specified size.
- [func sizeToFit()](uiview/sizetofit.md)
  Resizes and moves the receiver view so it just encloses its subviews.
- [var autoresizesSubviews: Bool](uiview/autoresizessubviews.md)
  A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [var autoresizingMask: UIView.AutoresizingMask](uiview/autoresizingmask-swift.property.md)
  An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/contentmode-swift.property)*