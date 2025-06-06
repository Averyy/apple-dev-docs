# inverse()

**Framework**: UIKit  
**Kind**: method

Returns a new region that’s the mathematical inverse of the current region.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func inverse() -> Self
```

#### Return Value

A new region whose contents include all points that are not in the current region.

#### Discussion

The inverse of the infinite region is an empty region.

## See Also

- [func byDifference(from: UIRegion) -> Self](uiregion/bydifference(from:).md)
  Returns a new region created by subtracting the specified region from the current region.
- [func byIntersection(with: UIRegion) -> Self](uiregion/byintersection(with:).md)
  Returns a new region containing only the area occupied by both the specified region and current region.
- [func byUnion(with: UIRegion) -> Self](uiregion/byunion(with:).md)
  Returns a new region containing the combined areas of the specified region and the current region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion/inverse())*