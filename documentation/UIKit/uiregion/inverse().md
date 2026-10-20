# inverse()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a new region that’s the mathematical inverse of the current region.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func inverse() -> Self
```

```objc
- (instancetype) inverseRegion;
```

#### Return Value

A new region whose contents include all points that are not in the current region.

#### Discussion

The inverse of the infinite region is an empty region.

## See Also

### Creating complex regions
- [func byDifference(from: UIRegion) -> Self](./bydifference%28from%29.md)
  Returns a new region created by subtracting the specified region from the current region.
- [func byIntersection(with: UIRegion) -> Self](./byintersection%28with%29.md)
  Returns a new region containing only the area occupied by both the specified region and current region.
- [func byUnion(with: UIRegion) -> Self](./byunion%28with%29.md)
  Returns a new region containing the combined areas of the specified region and the current region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion/inverse())*