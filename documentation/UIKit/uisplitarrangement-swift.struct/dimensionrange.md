# UISplitArrangement.DimensionRange

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A range of dimensions defining the minimum, preferred, and maximum size for a view within a split arrangement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
struct DimensionRange
```

## Topics

### Creating a dimension range
- [init()](./dimensionrange/init%28%29.md)
  Creates a dimension range.
### Getting the dimensions
- [var minimum: UISplitArrangement.Dimension](./dimensionrange/minimum.md)
  The minimum dimension for the view.
- [var preferred: UISplitArrangement.Dimension](./dimensionrange/preferred.md)
  The preferred dimension for the view.
- [var maximum: UISplitArrangement.Dimension](./dimensionrange/maximum.md)
  The maximum dimension for the view.

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
- [UISplitArrangement.Dimension](./dimension.md)
  A dimension for a view within a split arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct/dimensionrange)*