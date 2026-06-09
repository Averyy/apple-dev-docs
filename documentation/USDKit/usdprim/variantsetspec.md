# USDPrim.VariantSetSpec

**Framework**: USDKit  
**Kind**: struct

A handle to a variant set — a named group of variant options.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct VariantSetSpec
```

## Topics

### Initializers
- [init()](usdprim/variantsetspec/init.md)
  Creates an empty (invalid) variant set spec handle.
- [init?(USDLayer.Spec)](usdprim/variantsetspec/init(_:).md)
  Narrows an untyped [`USDLayer.Spec`](usdlayer/spec.md) to a variant set spec.
- [init?(owner: USDPrim.VariantSpec, name: USDToken)](usdprim/variantsetspec/init(owner:name:)-1njrp.md)
  Creates a new variant set spec nested inside a variant spec.
- [init?(owner: USDPrim.Spec, name: USDToken)](usdprim/variantsetspec/init(owner:name:)-6pbza.md)
  Creates a new variant set spec under the given prim spec.
### Instance Properties
- [var name: USDToken](usdprim/variantsetspec/name.md)
  The variant set’s local name.
- [var owner: USDLayer.Spec?](usdprim/variantsetspec/owner.md)
  The owning spec — a prim spec or variant spec.
- [var variants: [USDPrim.VariantSpec]](usdprim/variantsetspec/variants.md)
  All variant specs in this set.
### Instance Methods
- [func removeVariant(USDPrim.VariantSpec)](usdprim/variantsetspec/removevariant(_:).md)
  Removes the given variant spec from this set.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [USDLayer.Spec.FieldCollection](usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](usdlayer/spec/metadatacollection.md)

## See Also

- [USDPrim.VariantSpec](usdprim/variantspec.md)
  A handle to a single variant option within a variant set.
- [typealias VariantsMap](usdprim/variantsmap.md)
  Maps variant set names to lists of available variant names.
- [typealias VariantSelectionMap](usdprim/variantselectionmap.md)
  Maps variant set names to selected variant names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantsetspec)*