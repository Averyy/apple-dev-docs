# USDPrim.PseudoRootSpec

**Framework**: USDKit  
**Kind**: struct

A handle to a layer’s pseudo-root — the implicit parent of all top-level prims in a layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct PseudoRootSpec
```

#### Overview

The pseudo-root is a special spec that’s automatically created by every layer. It’s not authored as a prim in the file, but it conceptually owns the top-level prims. It conforms to `USDLayer.Spec.MetadataCollection` and `USDLayer.Spec.FieldCollection`.

## Topics

### Initializers
- [init()](usdprim/pseudorootspec/init.md)
  Creates an empty (invalid) pseudo-root spec handle.
- [init?(USDLayer.Spec)](usdprim/pseudorootspec/init(_:).md)
  Narrows an untyped [`USDLayer.Spec`](usdlayer/spec.md) to a pseudo-root spec.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [USDLayer.Spec.FieldCollection](usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](usdlayer/spec/metadatacollection.md)

## See Also

- [USDPrim.Spec](usdprim/spec.md)
  A handle to a prim definition stored in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/pseudorootspec)*