# UISplitArrangement

**Framework**: UIKit  
**Kind**: struct

An arrangement that splits views.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
struct UISplitArrangement
```

## Topics

### Creating a split arrangement
- [init()](uisplitarrangement-swift.struct/init.md)
  Creates a split arrangement.
### Configuring the arrangement
- [func axes(UIAxis) -> UISplitArrangement](uisplitarrangement-swift.struct/axes(_:).md)
  Sets the axes of the arrangement.
- [UISplitArrangement.Dimension](uisplitarrangement-swift.struct/dimension.md)
  A dimension for a view within a split arrangement.
- [UISplitArrangement.DimensionRange](uisplitarrangement-swift.struct/dimensionrange.md)
  A range of dimensions defining the minimum, preferred, and maximum size for a view within a split arrangement.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [UIArrangementViewController.Arrangement](uiarrangementviewcontroller/arrangement.md)

## See Also

- [UIArrangementViewController.Arrangement](uiarrangementviewcontroller/arrangement.md)
  A type that describes how an arrangement view controller lays out its view controllers.
- [struct UIOverlayArrangement](uioverlayarrangement-swift.struct.md)
  An arrangement that overlays views.
- [func updateArrangement<A>(A, animated: Bool)](uiarrangementviewcontroller/updatearrangement(_:animated:).md)
  Updates the arrangement of the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct)*