# UIView.ReservedRegion.Kind

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

## Overview

Pass a kind to [`reservedRegions(kind:options:)`](../reservedregions%28kind,options%29.md) to choose which regions you get: [`occlusion`](./kind-swift.struct/occlusion.md) for areas that cover your content, and [`division`](./kind-swift.struct/division.md) for areas that split it. Each [`UIView.ReservedRegion`](../reservedregion.md) also reports its kind in its [`kind`](./kind-swift.property.md) property.

## Topics

### Getting reserved region kinds
- [static let occlusion: UIView.ReservedRegion.Kind](./kind-swift.struct/occlusion.md)
  A region that covers part of your view.
- [static let division: UIView.ReservedRegion.Kind](./kind-swift.struct/division.md)
  A region that splits your view into separate parts.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../../../Swift/customreflectable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Getting region details
- [let frame: CGRect](./frame.md)
  The rectangle that describes the region within your view.
- [let isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the region is active.
- [let kind: UIView.ReservedRegion.Kind](./kind-swift.property.md)
  The kind of the region.
- [let margins: UIEdgeInsets](./margins.md)
  The extra space around the reserved area that keeps interactive content clear of it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregion/kind-swift.struct)*