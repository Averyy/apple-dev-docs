# UISplitArrangement.Dimension

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A dimension for a view within a split arrangement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
struct Dimension
```

## Topics

### Getting a dimension
- [static var automatic: UISplitArrangement.Dimension](./dimension/automatic.md)
  A dimension that indicates sizing for a view in a split arrangement follows automatic rules.
- [static var intrinsic: UISplitArrangement.Dimension](./dimension/intrinsic.md)
  A dimension that indicates sizing for a view in a split arrangement uses intrinsic content size.
- [static func absolute(CGFloat) -> UISplitArrangement.Dimension](./dimension/absolute%28_%29.md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide, expressed in points.
- [static func fractional(CGFloat) -> UISplitArrangement.Dimension](./dimension/fractional%28_%29.md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide as a fraction.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the arrangement
- [func axes(UIAxis) -> UISplitArrangement](./axes%28_%29.md)
  Sets the axes that the arrangement supports to the axes you provide.
- [UISplitArrangement.DimensionRange](./dimensionrange.md)
  A range of dimensions defining the minimum, preferred, and maximum size for a view within a split arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct/dimension)*