# USDPrim.VariantSetCollection

**Framework**: USDKit  
**Kind**: struct

Manages variant sets on a prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct VariantSetCollection
```

#### Overview

Variants provide a way to package multiple variations of scene data within a single asset. A prim can have multiple variant sets, each containing named variants that can be selected at runtime.

## Topics

### Instance Properties
- [var names: [String]](usdprim/variantsetcollection/names.md)
  The names of all variant sets on this prim.
- [var selections: [String : String]](usdprim/variantsetcollection/selections.md)
  The composed variant selections on this prim, keyed by variant set name.
### Instance Methods
- [func add(String) throws -> USDPrim.VariantSet](usdprim/variantsetcollection/add(_:).md)
  Adds a new variant set to the prim.
### Subscripts
- [subscript(String) -> USDPrim.VariantSet?](usdprim/variantsetcollection/subscript(_:).md)
  Returns the variant set with the specified name, or `nil` if no variant set with that name exists on the prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantsetcollection)*