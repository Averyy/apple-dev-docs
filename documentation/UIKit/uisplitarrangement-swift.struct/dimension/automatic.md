# automatic

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A dimension that indicates sizing for a view in a split arrangement follows automatic rules.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
static var automatic: UISplitArrangement.Dimension { get }
```

#### Discussion

This defaults to [`intrinsic`](./intrinsic.md).

## See Also

### Getting a dimension
- [static var intrinsic: UISplitArrangement.Dimension](./intrinsic.md)
  A dimension that indicates sizing for a view in a split arrangement uses intrinsic content size.
- [static func absolute(CGFloat) -> UISplitArrangement.Dimension](./absolute%28_%29.md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide, expressed in points.
- [static func fractional(CGFloat) -> UISplitArrangement.Dimension](./fractional%28_%29.md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide as a fraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct/dimension/automatic)*