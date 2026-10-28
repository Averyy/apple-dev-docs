# axes(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the axes that the arrangement supports to the axes you provide.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
func axes(_ axes: UIAxis) -> UISplitArrangement
```

## Discussion

For axes that you don’t include, the arrangement only displays the primary view.

## Parameters

- `axes`: The axes of the arrangement.

## See Also

### Configuring the arrangement
- [UISplitArrangement.Dimension](./dimension.md)
  A dimension for a view within a split arrangement.
- [UISplitArrangement.DimensionRange](./dimensionrange.md)
  A range of dimensions defining the minimum, preferred, and maximum size for a view within a split arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct/axes(_:))*