# reservedRegions(kind:options:)

**Framework**: UIKit  
**Kind**: method

Returns the reserved regions of a given kind and options.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func reservedRegions(kind: UIView.ReservedRegion.Kind, options: UIView.ReservedRegion.QueryOptions = []) -> [UIView.ReservedRegion]
```

## Parameters

- `kind`: The kind of the region.
- `options`: The options for querying the reserved regions.

## See Also

- [UIView.ReservedRegion](uiview/reservedregion.md)
  A region within a view’s coordinate space that another entity occupies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregions(kind:options:))*