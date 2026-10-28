# UIViewReservedRegion

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A region within a view’s coordinate space that another entity reserves.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
@interface UIViewReservedRegion : NSObject
```

## Overview

A reserved region indicates an area within a view’s coordinate space that an entity reserves, such as the device hardware. Arrange your view content to account for this region. Each region describes a frame, margins, active state, and an identifier.

There are two categories of reserved regions:

- **[`occlusionRegionKind`](./uiviewreservedregionkind/occlusionregionkind.md)**: An area where an element, such as the Dynamic Island, a camera, or window controls, covers your content. Place content outside this area.
- **[`divisionRegionKind`](./uiviewreservedregionkind/divisionregionkind.md)**: An area where content splits into separate regions, such as at the fold of a hinge. Arrange your content on both sides of this area.

Read reserved regions using the [`reservedRegionsOfKind:options:`](./uiview/reservedregionsofkind_options_.md) method, which returns the reserved regions that overlap your view. By default, the method returns only active regions that affect your view. To also get inactive regions, pass [`UIViewReservedRegionQueryOptionsIncludeInactive`](./uiviewreservedregionqueryoptions/uiviewreservedregionqueryoptionsincludeinactive.md).

## Topics

### Getting region details
- [frame](./uiviewreservedregion/frame.md)
  The rect of the region in the view’s coordinate space, including the margins.
- [active](./uiviewreservedregion/active.md)
  Whether the region is currently active.
- [kind](./uiviewreservedregion/kind.md)
  The kind of the region.
- [UIViewReservedRegionKind](./uiviewreservedregionkind.md)
  A kind of reserved region.
- [identifier](./uiviewreservedregion/identifier.md)
  The identifier of the region.
- [UIViewReservedRegionIdentifier](./uiviewreservedregionidentifier.md)
  An identifier of a reserved region.
- [margins](./uiviewreservedregion/margins.md)
  The margins included in the frame around the reserved rect for interactive content.
### Querying reserved regions
- [UIViewReservedRegionQueryOptions](./uiviewreservedregionqueryoptions.md)
  Options for querying reserved regions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Inspecting reserved regions
- [- reservedRegionsOfKind:](./uiview/reservedregionsofkind_.md)
  Returns the reserved regions of a given kind.
- [- reservedRegionsOfKind:options:](./uiview/reservedregionsofkind_options_.md)
  Returns the reserved regions of a given kind and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewreservedregion)*