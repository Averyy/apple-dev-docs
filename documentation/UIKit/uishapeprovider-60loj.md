# UIShapeProvider

**Framework**: UIKit  
**Kind**: protocol

An interface for a type that provides a custom shape by resolving it dynamically based on a context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
protocol UIShapeProvider : Equatable
```

## Topics

### Resolving a custom shape
- [func resolve(in: Self.Context) -> Self.Resolved](uishapeprovider-60loj/resolve(in:).md)
  Resolves the shape in the provided context.
### Supporting types
- [UIShapeProvider.Context](uishapeprovider-60loj/context.md)
  The context for resolving a dynamic shape.
- [UIShapeProvider.Resolved](uishapeprovider-60loj/resolved.md)
  A shape that has completely resolved based on a context.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
### Conforming Types
- [UIShape](uishape-swift.struct.md)

## See Also

- [init(some UIShapeProvider)](uishape-swift.struct/init(_:).md)
  Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShape.ResolutionContext](uishape-swift.struct/resolutioncontext.md)
  The context for resolving a dynamic shape.
- [UIShape.Resolved](uishape-swift.struct/resolved.md)
  A shape that has completely resolved based on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishapeprovider-60loj)*