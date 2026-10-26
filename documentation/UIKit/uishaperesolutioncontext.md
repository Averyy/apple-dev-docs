# UIShapeResolutionContext

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

The context for resolving a dynamic shape.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```objc
@interface UIShapeResolutionContext : NSObject
```

## Topics

### Determining the content shape
- [contentShape](./uishaperesolutioncontext/contentshape.md)
  The resolved shape of the content to which this shape can apply.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Creating a dynamic hover shape
- [+ shapeWithProvider:](./uishape-c.class/shapewithprovider_.md)
  Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShapeProvider](./uishapeprovider-31jrf.md)
  An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [- resolvedShapeInContext:](./uishape-c.class/resolvedshapeincontext_.md)
  Resolves the shape in the provided context.
- [UIResolvedShape](./uiresolvedshape.md)
  A shape that has completely resolved based on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishaperesolutioncontext)*