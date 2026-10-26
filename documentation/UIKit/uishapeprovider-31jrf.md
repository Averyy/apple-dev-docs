# UIShapeProvider

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

An interface for a type that provides a custom shape by resolving it dynamically based on a context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```objc
@protocol UIShapeProvider <NSObject>
```

## Topics

### Resolving a custom shape
- [- resolvedShapeInContext:](./uishapeprovider-31jrf/resolvedshapeincontext_.md)
  Resolves the shape in the provided context.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UIShape](./uishape-c.class.md)

## See Also

### Creating a dynamic hover shape
- [+ shapeWithProvider:](./uishape-c.class/shapewithprovider_.md)
  Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [- resolvedShapeInContext:](./uishape-c.class/resolvedshapeincontext_.md)
  Resolves the shape in the provided context.
- [UIShapeResolutionContext](./uishaperesolutioncontext.md)
  The context for resolving a dynamic shape.
- [UIResolvedShape](./uiresolvedshape.md)
  A shape that has completely resolved based on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishapeprovider-31jrf)*