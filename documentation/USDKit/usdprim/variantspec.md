# USDPrim.VariantSpec

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A handle to a single variant option within a variant set.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct VariantSpec
```

## Topics

### Initializers
- [init()](./variantspec/init%28%29.md)
  Creates an empty (invalid) variant spec handle.
- [init?(USDLayer.Spec)](./variantspec/init%28_%29.md)
  Narrows an untyped [`USDLayer.Spec`](../usdlayer/spec.md) to a variant spec.
- [init?(owner: USDPrim.VariantSetSpec, name: USDToken)](./variantspec/init%28owner,name%29.md)
  Creates a new variant spec under the given variant set spec.
### Instance Properties
- [var name: USDToken](./variantspec/name.md)
  The variant’s local name.
- [var owner: USDPrim.VariantSetSpec?](./variantspec/owner.md)
  The owning variant set spec.
- [var primSpec: USDPrim.Spec?](./variantspec/primspec.md)
  The prim spec this variant authors when selected.
- [var variantSets: [USDToken : USDPrim.VariantSetSpec]](./variantspec/variantsets.md)
  Variant sets defined inside this variant (nested variation).
### Instance Methods
- [func variantNames(USDToken) -> [USDToken]](./variantspec/variantnames%28_%29.md)
  Returns the variant names available in a nested variant set on this variant.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [USDLayer.Spec.FieldCollection](../usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](../usdlayer/spec/metadatacollection.md)

## See Also

### Authoring variants
- [USDPrim.VariantSetSpec](./variantsetspec.md)
  A handle to a variant set — a named group of variant options.
- [typealias VariantsMap](./variantsmap.md)
  Maps variant set names to lists of available variant names.
- [typealias VariantSelectionMap](./variantselectionmap.md)
  Maps variant set names to selected variant names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantspec)*