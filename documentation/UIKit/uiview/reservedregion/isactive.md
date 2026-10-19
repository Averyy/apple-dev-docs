# isActive

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the region is active.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
let isActive: Bool
```

#### Discussion

A region can become active or inactive as conditions change. An active region currently affects your view. An inactive region doesn’t. For example, the fold of iPhone Duo is active when the device is partially open, and inactive when it’s fully open.

By default, [`reservedRegions(kind:options:)`](uiview/reservedregions(kind:options:).md) returns only active regions. To also get inactive regions, pass [`includeInactive`](uiview/reservedregion/queryoptions/includeinactive.md).

## See Also

- [let frame: CGRect](uiview/reservedregion/frame.md)
  The rectangle that describes the region within your view.
- [let kind: UIView.ReservedRegion.Kind](uiview/reservedregion/kind-swift.property.md)
  The kind of the region.
- [UIView.ReservedRegion.Kind](uiview/reservedregion/kind-swift.struct.md)
  A kind of reserved region.
- [let margins: UIEdgeInsets](uiview/reservedregion/margins.md)
  The extra space around the reserved area that keeps interactive content clear of it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregion/isactive)*