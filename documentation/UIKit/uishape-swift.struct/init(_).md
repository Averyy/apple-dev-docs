# init(_:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a dynamic shape that resolves using the provided resolver closure and resolution context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
init(_ provider: some UIShapeProvider)
```

## See Also

### Creating a dynamic hover shape
- [protocol UIShapeProvider](../uishapeprovider-60loj.md)
  An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [UIShape.ResolutionContext](./resolutioncontext.md)
  The context for resolving a dynamic shape.
- [UIShape.Resolved](./resolved.md)
  A shape that has completely resolved based on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-swift.struct/init(_:))*