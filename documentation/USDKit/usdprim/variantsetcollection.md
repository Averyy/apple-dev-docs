# USDPrim.VariantSetCollection

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Manages variant sets on a prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct VariantSetCollection
```

#### Overview

Variants provide a way to package multiple variations of scene data within a single asset. A prim can have multiple variant sets, each containing named variants that can be selected at runtime.

## Topics

### Instance Properties
- [var names: [String]](./variantsetcollection/names.md)
  The names of all variant sets on this prim.
- [var selections: [String : String]](./variantsetcollection/selections.md)
  The composed variant selections on this prim, keyed by variant set name.
### Instance Methods
- [func add(String) throws -> USDPrim.VariantSet](./variantsetcollection/add%28_%29.md)
  Adds a new variant set to the prim.
### Subscripts
- [subscript(String) -> USDPrim.VariantSet?](./variantsetcollection/subscript%28_%29.md)
  Returns the variant set with the specified name, or `nil` if no variant set with that name exists on the prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantsetcollection)*