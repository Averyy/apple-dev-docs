# USDLayer.SpecType

**Framework**: USDKit  
**Kind**: enum

The kind of spec stored at a path in a layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum SpecType
```

## Topics

### Enumeration Cases
- [USDLayer.SpecType.attribute](usdlayer/spectype/attribute.md)
  An attribute spec.
- [USDLayer.SpecType.connection](usdlayer/spectype/connection.md)
  An attribute connection spec.
- [USDLayer.SpecType.prim](usdlayer/spectype/prim.md)
  A prim spec.
- [USDLayer.SpecType.pseudoRoot](usdlayer/spectype/pseudoroot.md)
  The implicit pseudo-root spec at `/`.
- [USDLayer.SpecType.relationship](usdlayer/spectype/relationship.md)
  A relationship spec.
- [USDLayer.SpecType.relationshipTarget](usdlayer/spectype/relationshiptarget.md)
  A relationship target spec.
- [USDLayer.SpecType.variant](usdlayer/spectype/variant.md)
  A variant spec.
- [USDLayer.SpecType.variantSet](usdlayer/spectype/variantset.md)
  A variant set spec.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func prim(at: USDLayer.Path) -> USDPrim.Spec?](usdlayer/prim(at:).md)
  Returns the prim spec authored at the given path, or `nil` if no prim spec exists there.
- [func property(at: USDLayer.Path) -> USDPrim.Property.Spec?](usdlayer/property(at:).md)
  Returns the property spec at the given path.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute.Spec?](usdlayer/attribute(at:).md)
  Returns the attribute spec at the given path.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship.Spec?](usdlayer/relationship(at:).md)
  Returns the relationship spec at the given path.
- [func spec(at: USDLayer.Path) -> USDLayer.Spec?](usdlayer/spec(at:).md)
  Returns the spec at the given path, or `nil` if no spec is authored there.
- [func specType(at: USDLayer.Path) -> USDLayer.SpecType?](usdlayer/spectype(at:).md)
  Returns the kind of spec authored at the given path, or `nil` if nothing is authored there.
- [func traverse(at: USDLayer.Path, (USDLayer.Path) -> Void)](usdlayer/traverse(at:_:).md)
  Walks the spec tree rooted at the given path, calling `body` for each spec’s path.
- [USDLayer.Path](usdlayer/path.md)
  A path within a USD scene hierarchy.
- [USDLayer.PathExpression](usdlayer/pathexpression.md)
  A boolean expression over path patterns for selecting sets of prims.
- [USDLayer.Spec](usdlayer/spec.md)
  A handle to a single spec stored in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/spectype)*