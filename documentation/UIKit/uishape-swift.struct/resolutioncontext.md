# UIShape.ResolutionContext

**Framework**: UIKit  
**Kind**: struct

The context for resolving a dynamic shape.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
struct ResolutionContext
```

## Topics

### Determining the content shape
- [var contentShape: UIShape.Resolved](uishape-swift.struct/resolutioncontext/contentshape.md)
  The resolved shape of the content to which this shape can apply.

## See Also

- [init(some UIShapeProvider)](uishape-swift.struct/init(_:).md)
  Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [protocol UIShapeProvider](uishapeprovider-60loj.md)
  An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [UIShape.Resolved](uishape-swift.struct/resolved.md)
  A shape that has completely resolved based on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-swift.struct/resolutioncontext)*