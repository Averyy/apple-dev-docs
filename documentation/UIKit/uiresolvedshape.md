# UIResolvedShape

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A shape that has completely resolved based on a context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```objc
@interface UIResolvedShape : NSObject
```

## Topics

### Creating a resolved shape by applying insets
- [- shapeByApplyingInsets:](./uiresolvedshape/shapebyapplyinginsets_.md)
  Creates a new modified shape by applying the provided insets to this shape.
- [- shapeByApplyingInset:](./uiresolvedshape/shapebyapplyinginset_.md)
  Creates a new modified shape by applying the provided inset to this shape.
### Accessing the resolved shape’s attributes
- [shape](./uiresolvedshape/shape.md)
  The abstract shape that produces this resolved shape.
- [boundingRect](./uiresolvedshape/boundingrect.md)
  The bounding rectangle that frames the shape.
- [path](./uiresolvedshape/path.md)
  The Bézier path representing this shape.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Creating a dynamic hover shape
- [+ shapeWithProvider:](./uishape-c.class/shapewithprovider_.md)
  Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShapeProvider](./uishapeprovider-31jrf.md)
  An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [- resolvedShapeInContext:](./uishape-c.class/resolvedshapeincontext_.md)
  Resolves the shape in the provided context.
- [UIShapeResolutionContext](./uishaperesolutioncontext.md)
  The context for resolving a dynamic shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresolvedshape)*