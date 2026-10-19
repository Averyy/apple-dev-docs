# automatic

**Framework**: UIKit  
**Kind**: property

A dimension that indicates sizing for a view in a split arrangement follows automatic rules.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
static var automatic: UISplitArrangement.Dimension { get }
```

#### Discussion

This defaults to [`intrinsic`](uisplitarrangement-swift.struct/dimension/intrinsic.md).

## See Also

- [static var intrinsic: UISplitArrangement.Dimension](uisplitarrangement-swift.struct/dimension/intrinsic.md)
  A dimension that indicates sizing for a view in a split arrangement uses intrinsic content size.
- [static func absolute(CGFloat) -> UISplitArrangement.Dimension](uisplitarrangement-swift.struct/dimension/absolute(_:).md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide, expressed in points.
- [static func fractional(CGFloat) -> UISplitArrangement.Dimension](uisplitarrangement-swift.struct/dimension/fractional(_:).md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide as a fraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct/dimension/automatic)*