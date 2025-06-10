# UIShape.Resolved

**Framework**: UIKit  
**Kind**: struct

A shape that has completely resolved based on a context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
struct Resolved
```

## Topics

### Creating a resolved shape by applying insets
- [func inset(by: UIEdgeInsets) -> UIShape.Resolved](uishape-swift.struct/resolved/inset(by:)-9sjcg.md)
  Creates a new modified shape by applying the provided insets to this shape.
- [func inset(by: CGFloat) -> UIShape.Resolved](uishape-swift.struct/resolved/inset(by:)-1r5gp.md)
  Creates a new modified shape by applying the provided inset to this shape.
### Accessing the resolved shape’s attributes
- [let shape: UIShape](uishape-swift.struct/resolved/shape.md)
  The abstract shape that produces this resolved shape.
- [var boundingRect: CGRect](uishape-swift.struct/resolved/boundingrect.md)
  The bounding rectangle that frames the shape.
- [var path: UIBezierPath](uishape-swift.struct/resolved/path.md)
  The Bézier path representing this shape.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [init(some UIShapeProvider)](uishape-swift.struct/init(_:).md)
  Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [protocol UIShapeProvider](uishapeprovider-60loj.md)
  An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [UIShape.ResolutionContext](uishape-swift.struct/resolutioncontext.md)
  The context for resolving a dynamic shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-swift.struct/resolved)*