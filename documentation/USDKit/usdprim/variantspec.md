# USDPrim.VariantSpec

**Framework**: USDKit  
**Kind**: struct

A handle to a single variant option within a variant set.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct VariantSpec
```

## Topics

### Initializers
- [init()](usdprim/variantspec/init.md)
  Creates an empty (invalid) variant spec handle.
- [init?(USDLayer.Spec)](usdprim/variantspec/init(_:).md)
  Narrows an untyped [`USDLayer.Spec`](usdlayer/spec.md) to a variant spec.
- [init?(owner: USDPrim.VariantSetSpec, name: USDToken)](usdprim/variantspec/init(owner:name:).md)
  Creates a new variant spec under the given variant set spec.
### Instance Properties
- [var name: USDToken](usdprim/variantspec/name.md)
  The variant’s local name.
- [var owner: USDPrim.VariantSetSpec?](usdprim/variantspec/owner.md)
  The owning variant set spec.
- [var primSpec: USDPrim.Spec?](usdprim/variantspec/primspec.md)
  The prim spec this variant authors when selected.
- [var variantSets: [USDToken : USDPrim.VariantSetSpec]](usdprim/variantspec/variantsets.md)
  Variant sets defined inside this variant (nested variation).
### Instance Methods
- [func variantNames(USDToken) -> [USDToken]](usdprim/variantspec/variantnames(_:).md)
  Returns the variant names available in a nested variant set on this variant.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [USDLayer.Spec.FieldCollection](usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](usdlayer/spec/metadatacollection.md)

## See Also

- [USDPrim.VariantSetSpec](usdprim/variantsetspec.md)
  A handle to a variant set — a named group of variant options.
- [typealias VariantsMap](usdprim/variantsmap.md)
  Maps variant set names to lists of available variant names.
- [typealias VariantSelectionMap](usdprim/variantselectionmap.md)
  Maps variant set names to selected variant names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantspec)*