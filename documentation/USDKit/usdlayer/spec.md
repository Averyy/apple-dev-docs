# USDLayer.Spec

**Framework**: USDKit  
**Kind**: struct

A handle to a single spec stored in a layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Spec
```

#### Overview

`Spec` is the untyped base used when retrieving a spec from a layer without knowing its concrete type. All concrete spec types (`USDPrim.Spec`, `USDPrim.Property.Spec`, etc.) conform to the nested [`USDLayer.Spec.MetadataCollection`](usdlayer/spec/metadatacollection.md) and [`USDLayer.Spec.FieldCollection`](usdlayer/spec/fieldcollection.md) protocols for shared metadata and field operations.

## Topics

### Protocols
- [USDLayer.Spec.FieldCollection](usdlayer/spec/fieldcollection.md)
  Low-level read/write access to spec fields. Fields are the raw data backing both metadata and structural information on a spec.
- [USDLayer.Spec.MetadataCollection](usdlayer/spec/metadatacollection.md)
  Read/write access to metadata stored on a spec.
### Initializers
- [init()](usdlayer/spec/init.md)
  Creates an empty (invalid) spec handle.
- [init(USDPrim.Property.Spec)](usdlayer/spec/init(_:)-2y5gq.md)
  Widens a `USDPrim.Property.Spec` into an untyped [`USDLayer.Spec`](usdlayer/spec.md).
- [init(USDPrim.Relationship.Spec)](usdlayer/spec/init(_:)-3kl4b.md)
  Widens a `USDPrim.Relationship.Spec` into an untyped [`USDLayer.Spec`](usdlayer/spec.md).
- [init(USDPrim.VariantSetSpec)](usdlayer/spec/init(_:)-5d7my.md)
  Widens a `USDPrim.VariantSetSpec` into an untyped [`USDLayer.Spec`](usdlayer/spec.md).
- [init(USDPrim.Attribute.Spec)](usdlayer/spec/init(_:)-5g16z.md)
  Widens a `USDPrim.Attribute.Spec` into an untyped [`USDLayer.Spec`](usdlayer/spec.md).
- [init(USDPrim.PseudoRootSpec)](usdlayer/spec/init(_:)-67qus.md)
  Widens a `USDPrim.PseudoRootSpec` into an untyped [`USDLayer.Spec`](usdlayer/spec.md).
- [init(USDPrim.Spec)](usdlayer/spec/init(_:)-7ecdx.md)
  Widens a `USDPrim.Spec` into an untyped [`USDLayer.Spec`](usdlayer/spec.md).
- [init(USDPrim.VariantSpec)](usdlayer/spec/init(_:)-7vtld.md)
  Widens a `USDPrim.VariantSpec` into an untyped [`USDLayer.Spec`](usdlayer/spec.md).

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [USDLayer.Spec.FieldCollection](usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](usdlayer/spec/metadatacollection.md)

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
- [USDLayer.SpecType](usdlayer/spectype.md)
  The kind of spec stored at a path in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/spec)*