# USDPrim.VariantSet

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Represents a single variant set on a prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct VariantSet
```

#### Overview

`USDPrim.VariantSet` provides methods to add variants, query available variants, and control which variant is currently selected. Each variant set contains named variants that represent different configurations of the prim’s data.

## Topics

### Instance Properties
- [var authoredSelection: String?](./variantset/authoredselection.md)
  The authored variant selection, or `nil` if none is authored.
- [var isValid: Bool](./variantset/isvalid.md)
  A Boolean value indicating whether this variant set is valid.
- [var name: String](./variantset/name.md)
  The name of this variant set.
- [var prim: USDPrim](./variantset/prim.md)
  The prim that owns this variant set.
- [var selection: String?](./variantset/selection.md)
  The currently selected variant name, or `nil` if no selection composes.
- [var variantNames: [String]](./variantset/variantnames.md)
  The names of all variants in this variant set.
### Instance Methods
- [func add(String) throws](./variantset/add%28_%29.md)
  Adds a new variant to this variant set.
- [func blockSelection() throws](./variantset/blockselection%28%29.md)
  Blocks the variant selection by authoring an explicit empty value on the current edit target.
- [func clearSelection() throws](./variantset/clearselection%28%29.md)
  Clears the variant selection.
- [func setSelection(String) throws](./variantset/setselection%28_%29.md)
  Sets the variant selection.
- [func withEditTarget<R>(layer: USDLayer?, (USDStage.EditTarget) throws -> R) rethrows -> R](./variantset/withedittarget%28layer,_%29.md)
  Performs the closure with the stage’s edit target set to author into the currently selected variant.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantset)*