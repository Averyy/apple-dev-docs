# fractional(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

A dimension that indicates sizing for a view in a split arrangement uses the float value you provide as a fraction.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
static func fractional(_ dimension: CGFloat) -> UISplitArrangement.Dimension
```

## Parameters

- `dimension`: A float value that expresses the fraction of the container to use, with a value between 0.0 and 1.0.

## See Also

### Getting a dimension
- [static var automatic: UISplitArrangement.Dimension](./automatic.md)
  A dimension that indicates sizing for a view in a split arrangement follows automatic rules.
- [static var intrinsic: UISplitArrangement.Dimension](./intrinsic.md)
  A dimension that indicates sizing for a view in a split arrangement uses intrinsic content size.
- [static func absolute(CGFloat) -> UISplitArrangement.Dimension](./absolute%28_%29.md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide, expressed in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct/dimension/fractional(_:))*