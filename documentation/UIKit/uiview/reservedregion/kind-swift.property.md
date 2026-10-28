# kind

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The kind of the region.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
let kind: UIView.ReservedRegion.Kind
```

## Discussion

The kind tells you how to respond to the region. Place your content outside an [`occlusion`](./kind-swift.struct/occlusion.md) region, and arrange it on both sides of a [`division`](./kind-swift.struct/division.md) region.

## See Also

### Getting region details
- [let frame: CGRect](./frame.md)
  The rectangle that describes the region within your view.
- [let isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the region is active.
- [UIView.ReservedRegion.Kind](./kind-swift.struct.md)
  A kind of reserved region.
- [let margins: UIEdgeInsets](./margins.md)
  The extra space around the reserved area that keeps interactive content clear of it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregion/kind-swift.property)*