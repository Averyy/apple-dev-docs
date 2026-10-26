# UIViewReservedRegionKind

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A kind of reserved region.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
@interface UIViewReservedRegionKind : NSObject
```

## Topics

### Specifying a reserved region
- [+ divisionRegionKind](./uiviewreservedregionkind/divisionregionkind.md)
  A region where an element should divide into two separate regions.
- [+ occlusionRegionKind](./uiviewreservedregionkind/occlusionregionkind.md)
  A region that is occluded by an element.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Getting region details
- [frame](./uiviewreservedregion/frame.md)
  The rect of the region in the view’s coordinate space, including the margins.
- [active](./uiviewreservedregion/active.md)
  Whether the region is currently active.
- [kind](./uiviewreservedregion/kind.md)
  The kind of the region.
- [identifier](./uiviewreservedregion/identifier.md)
  The identifier of the region.
- [UIViewReservedRegionIdentifier](./uiviewreservedregionidentifier.md)
  An identifier of a reserved region.
- [margins](./uiviewreservedregion/margins.md)
  The margins included in the frame around the reserved rect for interactive content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewreservedregionkind)*