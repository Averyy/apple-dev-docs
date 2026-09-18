# UISplitArrangement.Dimension

**Framework**: UIKit  
**Kind**: struct

A dimension for a view within a split arrangement.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
struct Dimension
```

## Topics

### Getting a dimension
- [static var automatic: UISplitArrangement.Dimension](uisplitarrangement-swift.struct/dimension/automatic.md)
  The automatic dimension for a split arrangement.
- [static var intrinsic: UISplitArrangement.Dimension](uisplitarrangement-swift.struct/dimension/intrinsic.md)
  The intrinsic dimension for a split arrangement based on intrinsic content size.
- [static func absolute(CGFloat) -> UISplitArrangement.Dimension](uisplitarrangement-swift.struct/dimension/absolute(_:).md)
  An absolute dimension for a split arrangement.
- [static func fractional(CGFloat) -> UISplitArrangement.Dimension](uisplitarrangement-swift.struct/dimension/fractional(_:).md)
  A fractional dimension for a split arrangement.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func axes(UIAxis) -> UISplitArrangement](uisplitarrangement-swift.struct/axes(_:).md)
  Sets the axes of the arrangement.
- [UISplitArrangement.DimensionRange](uisplitarrangement-swift.struct/dimensionrange.md)
  A range of dimensions defining the minimum, preferred, and maximum size for a view within a split arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct/dimension)*