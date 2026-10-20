# absolute(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

A dimension that indicates sizing for a view in a split arrangement uses the float value you provide, expressed in points.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
static func absolute(_ dimension: CGFloat) -> UISplitArrangement.Dimension
```

## Parameters

- `dimension`: The absolute point value of the dimension.

## See Also

### Getting a dimension
- [static var automatic: UISplitArrangement.Dimension](./automatic.md)
  A dimension that indicates sizing for a view in a split arrangement follows automatic rules.
- [static var intrinsic: UISplitArrangement.Dimension](./intrinsic.md)
  A dimension that indicates sizing for a view in a split arrangement uses intrinsic content size.
- [static func fractional(CGFloat) -> UISplitArrangement.Dimension](./fractional%28_%29.md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide as a fraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct/dimension/absolute(_:))*