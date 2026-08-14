# USDPrim.VariantSet

**Framework**: USDKit  
**Kind**: struct

Represents a single variant set on a prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct VariantSet
```

#### Overview

`USDPrim.VariantSet` provides methods to add variants, query available variants, and control which variant is currently selected. Each variant set contains named variants that represent different configurations of the prim’s data.

## Topics

### Instance Properties
- [var authoredSelection: String?](usdprim/variantset/authoredselection.md)
  The authored variant selection, or `nil` if none is authored.
- [var isValid: Bool](usdprim/variantset/isvalid.md)
  A Boolean value indicating whether this variant set is valid.
- [var name: String](usdprim/variantset/name.md)
  The name of this variant set.
- [var prim: USDPrim](usdprim/variantset/prim.md)
  The prim that owns this variant set.
- [var selection: String?](usdprim/variantset/selection.md)
  The currently selected variant name, or `nil` if no selection composes.
- [var variantNames: [String]](usdprim/variantset/variantnames.md)
  The names of all variants in this variant set.
### Instance Methods
- [func add(String) throws](usdprim/variantset/add(_:).md)
  Adds a new variant to this variant set.
- [func blockSelection() throws](usdprim/variantset/blockselection.md)
  Blocks the variant selection by authoring an explicit empty value on the current edit target.
- [func clearSelection() throws](usdprim/variantset/clearselection.md)
  Clears the variant selection.
- [func setSelection(String) throws](usdprim/variantset/setselection(_:).md)
  Sets the variant selection.
- [func withEditTarget<R>(layer: USDLayer?, (USDStage.EditTarget) throws -> R) rethrows -> R](usdprim/variantset/withedittarget(layer:_:).md)
  Performs the closure with the stage’s edit target set to author into the currently selected variant.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantset)*