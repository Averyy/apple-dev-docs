# fractionalDimension:

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

```objc
+ (instancetype) fractionalDimension:(CGFloat) fraction;
```

## Parameters

- `fraction`: A float value that expresses the fraction of the container to use, with a value between 0.0 and 1.0.

## See Also

### Getting a dimension
- [+ automaticDimension](./automaticdimension.md)
  A dimension that indicates sizing for a view in a split arrangement follows automatic rules.
- [+ intrinsicDimension](./intrinsicdimension.md)
  A dimension that indicates sizing for a view in a split arrangement uses intrinsic content size.
- [+ absoluteDimension:](./absolutedimension_.md)
  A dimension that indicates sizing for a view in a split arrangement uses the float value you provide, expressed in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangementdimension/fractionaldimension:)*