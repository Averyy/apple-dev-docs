# shapeWithProvider:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a dynamic shape that resolves using the provided resolver closure and resolution context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) shapeWithProvider:(id<UIShapeProvider>) provider;
```

## See Also

### Creating a dynamic hover shape
- [UIShapeProvider](../uishapeprovider-31jrf.md)
  An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [- resolvedShapeInContext:](./resolvedshapeincontext_.md)
  Resolves the shape in the provided context.
- [UIShapeResolutionContext](../uishaperesolutioncontext.md)
  The context for resolving a dynamic shape.
- [UIResolvedShape](../uiresolvedshape.md)
  A shape that has completely resolved based on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-c.class/shapewithprovider:)*