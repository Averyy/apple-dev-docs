# automaticDimension

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

A dimension that indicates sizing for a view in a split arrangement follows automatic rules.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
+ (instancetype) automaticDimension;
```

## Discussion

This defaults to [`intrinsicDimension`](./intrinsicdimension.md).

## See Also

### Getting a dimension
- [+ intrinsicDimension](./intrinsicdimension.md)
  A dimension that indicates sizing for a view in a split arrangement uses intrinsic content size.
- [+ absoluteDimension:](./absolutedimension_.md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide, expressed in points.
- [+ fractionalDimension:](./fractionaldimension_.md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide as a fraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangementdimension/automaticdimension)*