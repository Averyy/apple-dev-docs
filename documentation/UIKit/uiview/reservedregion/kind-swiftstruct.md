# UIView.ReservedRegion.Kind

**Framework**: UIKit  
**Kind**: struct

A kind of reserved region.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
struct Kind
```

#### Overview

Pass a kind to [`reservedRegions(kind:options:)`](uiview/reservedregions(kind:options:).md) to choose which regions you get: [`occlusion`](uiview/reservedregion/kind-swift.struct/occlusion.md) for areas that cover your content, and [`division`](uiview/reservedregion/kind-swift.struct/division.md) for areas that split it. Each [`UIView.ReservedRegion`](uiview/reservedregion.md) also reports its kind in its [`kind`](uiview/reservedregion/kind-swift.property.md) property.

## Topics

### Getting reserved region kinds
- [static let occlusion: UIView.ReservedRegion.Kind](uiview/reservedregion/kind-swift.struct/occlusion.md)
  A region that covers part of your view.
- [static let division: UIView.ReservedRegion.Kind](uiview/reservedregion/kind-swift.struct/division.md)
  A region that splits your view into separate parts.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomReflectable](../swift/customreflectable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [let frame: CGRect](uiview/reservedregion/frame.md)
  The rectangle that describes the region within your view.
- [let isActive: Bool](uiview/reservedregion/isactive.md)
  A Boolean value that indicates whether the region is active.
- [let kind: UIView.ReservedRegion.Kind](uiview/reservedregion/kind-swift.property.md)
  The kind of the region.
- [let margins: UIEdgeInsets](uiview/reservedregion/margins.md)
  The extra space around the reserved area that keeps interactive content clear of it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregion/kind-swift.struct)*