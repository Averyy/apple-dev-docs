# UIView.ReservedRegion

**Framework**: UIKit  
**Kind**: struct

A region within a view’s coordinate space that another entity occupies.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
struct ReservedRegion
```

#### Overview

A reserved region indicates that another entity occupies an area within a view’s coordinate space that the view doesn’t own. Arrange your view content to account for this region. Each region describes a frame, margins, active state, and an identifier.

There are two categories of reserved regions:

- **[`occlusion`](uiview/reservedregion/kind-swift.struct/occlusion.md)**: An area where an element, such as the Dynamic Island, a camera, or window controls, occludes content.
- **[`division`](uiview/reservedregion/kind-swift.struct/division.md)**: An area where content splits into separate regions, such as at the fold of a hinge.

Read reserved regions using the [`reservedRegions(kind:options:)`](uiview/reservedregions(kind:options:).md) method, which returns all of the reserved regions that currently intersect your view regardless of whether they are currently active.

## Topics

### Getting region details
- [let frame: CGRect](uiview/reservedregion/frame.md)
  The rectangle of the region in the view’s coordinate space, including the margins.
- [let isActive: Bool](uiview/reservedregion/isactive.md)
  A Boolean value that indicates whether the region is currently active.
- [let kind: UIView.ReservedRegion.Kind](uiview/reservedregion/kind-swift.property.md)
  The kind of the region.
- [UIView.ReservedRegion.Kind](uiview/reservedregion/kind-swift.struct.md)
  A kind of reserved region.
- [let margins: UIEdgeInsets](uiview/reservedregion/margins.md)
  The margins included in the frame around the reserved region for interactive content.
### Querying reserved regions
- [UIView.ReservedRegion.QueryOptions](uiview/reservedregion/queryoptions.md)
  Options for querying reserved regions.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)

## See Also

- [func reservedRegions(kind: UIView.ReservedRegion.Kind, options: UIView.ReservedRegion.QueryOptions) -> [UIView.ReservedRegion]](uiview/reservedregions(kind:options:).md)
  Returns the reserved regions of a given kind and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregion)*