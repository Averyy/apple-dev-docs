# USDLayer.Spec

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A handle to a single spec stored in a layer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Spec
```

#### Overview

`Spec` is the untyped base used when retrieving a spec from a layer without knowing its concrete type. All concrete spec types (`USDPrim.Spec`, `USDPrim.Property.Spec`, etc.) conform to the nested [`USDLayer.Spec.MetadataCollection`](./spec/metadatacollection.md) and [`USDLayer.Spec.FieldCollection`](./spec/fieldcollection.md) protocols for shared metadata and field operations.

## Topics

### Protocols
- [USDLayer.Spec.FieldCollection](./spec/fieldcollection.md)
  Low-level read/write access to spec fields. Fields are the raw data backing both metadata and structural information on a spec.
- [USDLayer.Spec.MetadataCollection](./spec/metadatacollection.md)
  Read/write access to metadata stored on a spec.
### Initializers
- [init()](./spec/init%28%29.md)
  Creates an empty (invalid) spec handle.
- [init(USDPrim.Property.Spec)](./spec/init%28_%29-2y5gq.md)
  Widens a `USDPrim.Property.Spec` into an untyped [`USDLayer.Spec`](./spec.md).
- [init(USDPrim.Relationship.Spec)](./spec/init%28_%29-3kl4b.md)
  Widens a `USDPrim.Relationship.Spec` into an untyped [`USDLayer.Spec`](./spec.md).
- [init(USDPrim.VariantSetSpec)](./spec/init%28_%29-5d7my.md)
  Widens a `USDPrim.VariantSetSpec` into an untyped [`USDLayer.Spec`](./spec.md).
- [init(USDPrim.Attribute.Spec)](./spec/init%28_%29-5g16z.md)
  Widens a `USDPrim.Attribute.Spec` into an untyped [`USDLayer.Spec`](./spec.md).
- [init(USDPrim.PseudoRootSpec)](./spec/init%28_%29-67qus.md)
  Widens a `USDPrim.PseudoRootSpec` into an untyped [`USDLayer.Spec`](./spec.md).
- [init(USDPrim.Spec)](./spec/init%28_%29-7ecdx.md)
  Widens a `USDPrim.Spec` into an untyped [`USDLayer.Spec`](./spec.md).
- [init(USDPrim.VariantSpec)](./spec/init%28_%29-7vtld.md)
  Widens a `USDPrim.VariantSpec` into an untyped [`USDLayer.Spec`](./spec.md).

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [USDLayer.Spec.FieldCollection](./spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](./spec/metadatacollection.md)

## See Also

### Accessing scene description by path
- [func prim(at: USDLayer.Path) -> USDPrim.Spec?](./prim%28at%29.md)
  Returns the prim spec authored at the given path, or `nil` if no prim spec exists there.
- [func property(at: USDLayer.Path) -> USDPrim.Property.Spec?](./property%28at%29.md)
  Returns the property spec at the given path.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute.Spec?](./attribute%28at%29.md)
  Returns the attribute spec at the given path.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship.Spec?](./relationship%28at%29.md)
  Returns the relationship spec at the given path.
- [func spec(at: USDLayer.Path) -> USDLayer.Spec?](./spec%28at%29.md)
  Returns the spec at the given path, or `nil` if no spec is authored there.
- [func specType(at: USDLayer.Path) -> USDLayer.SpecType?](./spectype%28at%29.md)
  Returns the kind of spec authored at the given path, or `nil` if nothing is authored there.
- [func traverse(at: USDLayer.Path, (USDLayer.Path) -> Void)](./traverse%28at,_%29.md)
  Walks the spec tree rooted at the given path, calling `body` for each spec’s path.
- [USDLayer.Path](./path.md)
  A path within a USD scene hierarchy.
- [USDLayer.PathExpression](./pathexpression.md)
  A boolean expression over path patterns for selecting sets of prims.
- [USDLayer.SpecType](./spectype.md)
  The kind of spec stored at a path in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/spec)*