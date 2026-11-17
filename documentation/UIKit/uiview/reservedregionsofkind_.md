# reservedRegionsOfKind:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the active reserved regions of a kind that overlap the view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
- (NSArray<UIViewReservedRegion *> *) reservedRegionsOfKind:(UIViewReservedRegionKind *) kind;
```

## Return Value

The active reserved regions that overlap the view, with frames in the view’s coordinate space.

## Discussion

This method is equivalent to calling [`reservedRegionsOfKind:options:`](./reservedregionsofkind_options_.md) with the [`UIViewReservedRegionQueryOptionsNone`](../uiviewreservedregionqueryoptions/uiviewreservedregionqueryoptionsnone.md) option, so it doesn’t return inactive regions. To also get inactive regions, call [`reservedRegionsOfKind:options:`](./reservedregionsofkind_options_.md) instead.

Use this method to arrange your view’s content around areas that the device hardware reserves, such as a camera or the fold of a hinge. UIKit tracks the regions you read in [`updateConstraints()`](./updateconstraints%28%29.md) and runs it again when the regions change.

For more information, see [`UIViewReservedRegion`](../uiviewreservedregion.md).

## Parameters

- `kind`: The kind of reserved region to return, such as [`occlusionRegionKind`](../uiviewreservedregionkind/occlusionregionkind.md) or [`divisionRegionKind`](../uiviewreservedregionkind/divisionregionkind.md).

## See Also

### Inspecting reserved regions
- [UIViewReservedRegion](../uiviewreservedregion.md)
  A region within a view’s coordinate space that another entity reserves.
- [- reservedRegionsOfKind:options:](./reservedregionsofkind_options_.md)
  Returns the reserved regions of a kind that overlap the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregionsofkind:)*