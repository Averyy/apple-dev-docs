# USDPrim.Spec

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A handle to a prim definition stored in a layer.

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

## Overview

`USDPrim.Spec` is a struct but acts as a handle into data owned by a [`USDLayer`](../usdlayer.md), much like [`USDPrim`](../usdprim.md) is a handle into a [`USDStage`](../usdstage.md). Mutations write through to the layer rather than to the spec value itself, so property setters and methods on this type are non-mutating.

## Topics

### Initializers
- [init()](./spec/init%28%29.md)
  Creates an empty (invalid) prim spec handle.
- [init(USDPrim.PseudoRootSpec)](./spec/init%28_%29-7yaap.md)
  Widens a `USDPrim.PseudoRootSpec` into a generic `USDPrim.Spec`, exposing the full prim-spec API (children, properties, metadata).
- [init?(USDLayer.Spec)](./spec/init%28_%29-9poa6.md)
  Narrows an untyped [`USDLayer.Spec`](../usdlayer/spec.md) to a `USDPrim.Spec`.
- [init?(layer: USDLayer, primPath: USDLayer.Path)](./spec/init%28layer,primpath%29.md)
  Creates a prim spec at the given path in the layer, authoring intermediate ancestor prim specs as `over`s where needed.
- [init?(parentLayer: USDLayer, name: USDToken, specifier: USDPrim.Specifier, typeName: String)](./spec/init%28parentlayer,name,specifier,typename%29.md)
  Creates a new top-level prim spec under the given layer.
- [init?(parentPrimSpec: USDPrim.Spec, name: USDToken, specifier: USDPrim.Specifier, typeName: String)](./spec/init%28parentprimspec,name,specifier,typename%29.md)
  Creates a new child prim spec under the given parent prim spec.
### Instance Properties
- [var assetInfo: Dictionary<String, USDValue>](./spec/assetinfo.md)
  The asset info dictionary authored on this prim.
- [var attributes: [USDPrim.Attribute.Spec]](./spec/attributes.md)
  All attribute specs on this prim.
- [var children: [USDPrim.Spec]](./spec/children.md)
  The child prim specs in authoring order.
- [var childrenOrder: [USDToken]?](./spec/childrenorder.md)
  The authored override for child ordering, or `nil` if no order is authored. When non-nil, this list controls the order in which child prim specs appear during composition.
- [var comment: String?](./spec/comment.md)
  The authored user comment, or `nil` if not authored.
- [var customData: Dictionary<String, USDValue>](./spec/customdata.md)
  The custom data dictionary authored on this prim.
- [var documentation: String?](./spec/documentation.md)
  The authored documentation, or `nil` if not authored.
- [var inherits: [USDLayer.Path]?](./spec/inherits.md)
  The authored inherit paths, or `nil` if none authored.
- [var isActive: Bool?](./spec/isactive.md)
  Whether this prim is active in composition, or `nil` if not authored.
- [var isInstanceable: Bool?](./spec/isinstanceable.md)
  Whether this prim is marked as an instance, or `nil` if not authored.
- [var kind: USDToken?](./spec/kind.md)
  The prim’s kind, or `nil` if not authored.
- [var name: USDToken](./spec/name.md)
  The prim’s local name.
- [var parent: USDPrim.Spec?](./spec/parent.md)
  The parent prim spec, or `nil` if this is a top-level prim spec.
- [var payloads: [USDPrim.Payload]?](./spec/payloads.md)
  The authored payloads on this prim, or `nil` if none authored.
- [var permission: USDLayer.Permission](./spec/permission.md)
  The prim’s permission level (public, restricted, private).
- [var prefix: String?](./spec/prefix.md)
  The authored prefix, or `nil` if not authored.
- [var prefixSubstitutions: Dictionary<String, USDValue>](./spec/prefixsubstitutions.md)
  The prefix substitutions dictionary.
- [var properties: [USDPrim.Property.Spec]](./spec/properties.md)
  All property specs (attributes and relationships) on this prim.
- [var propertyOrder: [USDToken]?](./spec/propertyorder.md)
  The authored override for property ordering, or `nil` if no order is authored.
- [var pseudoRoot: USDPrim.Spec?](./spec/pseudoroot.md)
  The pseudo-root prim spec at `/` in this spec’s layer.
- [var references: [USDPrim.Reference]?](./spec/references.md)
  The authored references on this prim, or `nil` if none authored.
- [var relationships: [USDPrim.Relationship.Spec]](./spec/relationships.md)
  All relationship specs on this prim.
- [var relocates: USDLayer.RelocatesMap?](./spec/relocates.md)
  The relocates map authored on this prim, or `nil` if none authored.
- [var specializes: [USDLayer.Path]?](./spec/specializes.md)
  The authored specializes paths, or `nil` if none authored.
- [var specifier: USDPrim.Specifier](./spec/specifier.md)
  How this prim definition composes — `def`, `over`, or `class`.
- [var suffix: String?](./spec/suffix.md)
  The authored suffix, or `nil` if not authored.
- [var suffixSubstitutions: Dictionary<String, USDValue>](./spec/suffixsubstitutions.md)
  The suffix substitutions dictionary.
- [var symmetricPeer: String?](./spec/symmetricpeer.md)
  The symmetric peer path, or `nil` if not authored.
- [var symmetryArguments: Dictionary<String, USDValue>](./spec/symmetryarguments.md)
  The symmetry arguments dictionary authored on this prim.
- [var symmetryFunction: USDToken?](./spec/symmetryfunction.md)
  The symmetry function token, or `nil` if not authored.
- [var typeName: USDToken](./spec/typename.md)
  The prim’s type name.
- [var variantSelections: [USDToken : USDToken]](./spec/variantselections.md)
  All authored variant selections, keyed by variant set name.
- [var variantSetNames: [USDToken]](./spec/variantsetnames.md)
  The names of variant sets defined on this prim.
- [var variantSets: [USDToken : USDPrim.VariantSetSpec]](./spec/variantsets.md)
  The variant sets authored on this prim, keyed by name.
### Instance Methods
- [func appendChild(USDPrim.Spec)](./spec/appendchild%28_%29.md)
  Appends `child` to the end of the children list.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute.Spec?](./spec/attribute%28at%29.md)
  Returns the attribute spec at the given path within this prim.
- [func blockVariantSelection(for: USDToken)](./spec/blockvariantselection%28for%29.md)
  Authors an explicit “no selection” for the given variant set.
- [func clearAssetInfo(String)](./spec/clearassetinfo%28_%29.md)
  Removes `key` from the asset info dictionary.
- [func clearCustomData(String)](./spec/clearcustomdata%28_%29.md)
  Removes `key` from the custom data dictionary.
- [func clearInherits()](./spec/clearinherits%28%29.md)
  Clears all authored inherit paths on this prim.
- [func clearPayloads()](./spec/clearpayloads%28%29.md)
  Clears all authored payloads on this prim.
- [func clearReferences()](./spec/clearreferences%28%29.md)
  Clears all authored references on this prim.
- [func clearRelocates()](./spec/clearrelocates%28%29.md)
  Clears all authored relocates on this prim.
- [func clearSpecializes()](./spec/clearspecializes%28%29.md)
  Clears all authored specializes paths on this prim.
- [func clearSymmetryArgument(String)](./spec/clearsymmetryargument%28_%29.md)
  Removes `name` from the symmetry arguments dictionary.
- [func clearVariantSelection(for: USDToken)](./spec/clearvariantselection%28for%29.md)
  Clears the variant selection for the given variant set.
- [func insertChild(USDPrim.Spec, at: Int)](./spec/insertchild%28_,at%29.md)
  Inserts `child` into the children list at `index`.
- [func prim(at: USDLayer.Path) -> USDPrim.Spec?](./spec/prim%28at%29.md)
  Returns the prim spec at the given path within this prim.
- [func property(at: USDLayer.Path) -> USDPrim.Property.Spec?](./spec/property%28at%29.md)
  Returns the property spec at the given path within this prim.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship.Spec?](./spec/relationship%28at%29.md)
  Returns the relationship spec at the given path within this prim.
- [func removeChild(USDPrim.Spec)](./spec/removechild%28_%29.md)
  Removes `child` from the children list. No-op if `child` is not a child of this spec.
- [func removeProperty(USDPrim.Property.Spec)](./spec/removeproperty%28_%29.md)
  Removes the given property spec from this prim.
- [func removeVariantSet(USDToken)](./spec/removevariantset%28_%29.md)
  Removes the variant set with the given name.
- [func rename(to: USDToken) throws](./spec/rename%28to%29.md)
  Sets the prim’s name.
- [func setAssetInfo(String, to: USDValue)](./spec/setassetinfo%28_,to%29.md)
  Sets `key` in the asset info dictionary to `value`.
- [func setCustomData(String, to: USDValue)](./spec/setcustomdata%28_,to%29.md)
  Sets `key` in the custom data dictionary to `value`.
- [func setSymmetryArgument(String, to: USDValue)](./spec/setsymmetryargument%28_,to%29.md)
  Sets `name` in the symmetry arguments dictionary to `value`.
- [func setVariantSelection(for: USDToken, to: USDToken)](./spec/setvariantselection%28for,to%29.md)
  Sets the variant selection for the given variant set.
- [func spec(at: USDLayer.Path) -> USDLayer.Spec?](./spec/spec%28at%29.md)
  Returns the spec at the given path within this prim.
- [func variantNames(in: USDToken) -> [USDToken]](./spec/variantnames%28in%29.md)
  Returns the variant names available in the given variant set.
- [func variantSelection(for: USDToken) -> USDToken?](./spec/variantselection%28for%29.md)
  Returns the authored variant selection for the given variant set.
### Type Methods
- [static func isValidName(USDToken) -> Bool](./spec/isvalidname%28_%29.md)
  Returns a Boolean value that indicates whether `name` is a valid prim name.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [USDLayer.Spec.FieldCollection](../usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](../usdlayer/spec/metadatacollection.md)

## See Also

### Working with scene-description specs
- [USDPrim.PseudoRootSpec](./pseudorootspec.md)
  A handle to a layer’s pseudo-root — the implicit parent of all top-level prims in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/spec)*