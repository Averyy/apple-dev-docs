# frame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The rectangle that describes the region within your view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
let frame: CGRect
```

## Discussion

The frame uses your view’s own coordinates. It already includes the region’s [`margins`](./margins.md), so you don’t need to add the margins yourself.

## See Also

### Getting region details
- [let isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the region is active.
- [let kind: UIView.ReservedRegion.Kind](./kind-swift.property.md)
  The kind of the region.
- [UIView.ReservedRegion.Kind](./kind-swift.struct.md)
  A kind of reserved region.
- [let margins: UIEdgeInsets](./margins.md)
  The extra space around the reserved area that keeps interactive content clear of it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregion/frame)*