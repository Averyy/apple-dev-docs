# USDPrim.VariantSetSpec

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A handle to a variant set — a named group of variant options.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct VariantSetSpec
```

## Topics

### Initializers
- [init()](./variantsetspec/init%28%29.md)
  Creates an empty (invalid) variant set spec handle.
- [init?(USDLayer.Spec)](./variantsetspec/init%28_%29.md)
  Narrows an untyped [`USDLayer.Spec`](../usdlayer/spec.md) to a variant set spec.
- [init?(owner: USDPrim.VariantSpec, name: USDToken)](./variantsetspec/init%28owner,name%29-1njrp.md)
  Creates a new variant set spec nested inside a variant spec.
- [init?(owner: USDPrim.Spec, name: USDToken)](./variantsetspec/init%28owner,name%29-6pbza.md)
  Creates a new variant set spec under the given prim spec.
### Instance Properties
- [var name: USDToken](./variantsetspec/name.md)
  The variant set’s local name.
- [var owner: USDLayer.Spec?](./variantsetspec/owner.md)
  The owning spec — a prim spec or variant spec.
- [var variants: [USDPrim.VariantSpec]](./variantsetspec/variants.md)
  All variant specs in this set.
### Instance Methods
- [func removeVariant(USDPrim.VariantSpec)](./variantsetspec/removevariant%28_%29.md)
  Removes the given variant spec from this set.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [USDLayer.Spec.FieldCollection](../usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](../usdlayer/spec/metadatacollection.md)

## See Also

### Authoring variants
- [USDPrim.VariantSpec](./variantspec.md)
  A handle to a single variant option within a variant set.
- [typealias VariantsMap](./variantsmap.md)
  Maps variant set names to lists of available variant names.
- [typealias VariantSelectionMap](./variantselectionmap.md)
  Maps variant set names to selected variant names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantsetspec)*