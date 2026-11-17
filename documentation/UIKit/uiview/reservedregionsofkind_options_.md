# reservedRegionsOfKind:options:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the reserved regions of a kind that overlap the view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
- (NSArray<UIViewReservedRegion *> *) reservedRegionsOfKind:(UIViewReservedRegionKind *) kind options:(UIViewReservedRegionQueryOptions) options;
```

## Return Value

The reserved regions that overlap the view, with frames in the view’s coordinate space.

## Discussion

Use this method to arrange your view’s content around areas that the device hardware reserves, such as a camera or the fold of a hinge. UIKit tracks the regions you read in [`updateConstraints()`](./updateconstraints%28%29.md) and runs it again when the regions change.

For more information, see [`UIViewReservedRegion`](../uiviewreservedregion.md).

## Parameters

- `kind`: The kind of reserved region to return, such as [`occlusionRegionKind`](../uiviewreservedregionkind/occlusionregionkind.md) or [`divisionRegionKind`](../uiviewreservedregionkind/divisionregionkind.md).
- `options`: Options that change which regions the method returns. By default, the method returns only active regions. Pass [`UIViewReservedRegionQueryOptionsIncludeInactive`](../uiviewreservedregionqueryoptions/uiviewreservedregionqueryoptionsincludeinactive.md) to also return regions that aren’t currently active.

## See Also

### Inspecting reserved regions
- [UIViewReservedRegion](../uiviewreservedregion.md)
  A region within a view’s coordinate space that another entity reserves.
- [- reservedRegionsOfKind:](./reservedregionsofkind_.md)
  Returns the active reserved regions of a kind that overlap the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregionsofkind:options:)*