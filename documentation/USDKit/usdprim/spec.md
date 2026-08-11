# USDPrim.Spec

**Framework**: USDKit  
**Kind**: struct

A handle to a prim definition stored in a layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Spec
```

#### Overview

`USDPrim.Spec` is a struct but acts as a handle into data owned by a [`USDLayer`](usdlayer.md), much like [`USDPrim`](usdprim.md) is a handle into a [`USDStage`](usdstage.md). Mutations write through to the layer rather than to the spec value itself, so property setters and methods on this type are non-mutating.

## Topics

### Initializers
- [init()](usdprim/spec/init.md)
  Creates an empty (invalid) prim spec handle.
- [init(USDPrim.PseudoRootSpec)](usdprim/spec/init(_:)-7yaap.md)
  Widens a `USDPrim.PseudoRootSpec` into a generic `USDPrim.Spec`, exposing the full prim-spec API (children, properties, metadata).
- [init?(USDLayer.Spec)](usdprim/spec/init(_:)-9poa6.md)
  Narrows an untyped [`USDLayer.Spec`](usdlayer/spec.md) to a `USDPrim.Spec`.
- [init?(layer: USDLayer, primPath: USDLayer.Path)](usdprim/spec/init(layer:primpath:).md)
  Creates a prim spec at the given path in the layer, authoring intermediate ancestor prim specs as `over`s where needed.
- [init?(parentLayer: USDLayer, name: USDToken, specifier: USDPrim.Specifier, typeName: String)](usdprim/spec/init(parentlayer:name:specifier:typename:).md)
  Creates a new top-level prim spec under the given layer.
- [init?(parentPrimSpec: USDPrim.Spec, name: USDToken, specifier: USDPrim.Specifier, typeName: String)](usdprim/spec/init(parentprimspec:name:specifier:typename:).md)
  Creates a new child prim spec under the given parent prim spec.
### Instance Properties
- [var assetInfo: Dictionary<String, USDValue>](usdprim/spec/assetinfo.md)
  The asset info dictionary authored on this prim.
- [var attributes: [USDPrim.Attribute.Spec]](usdprim/spec/attributes.md)
  All attribute specs on this prim.
- [var children: [USDPrim.Spec]](usdprim/spec/children.md)
  The child prim specs in authoring order.
- [var childrenOrder: [USDToken]?](usdprim/spec/childrenorder.md)
  The authored override for child ordering, or `nil` if no order is authored. When non-nil, this list controls the order in which child prim specs appear during composition.
- [var comment: String?](usdprim/spec/comment.md)
  The authored user comment, or `nil` if not authored.
- [var customData: Dictionary<String, USDValue>](usdprim/spec/customdata.md)
  The custom data dictionary authored on this prim.
- [var documentation: String?](usdprim/spec/documentation.md)
  The authored documentation, or `nil` if not authored.
- [var inherits: [USDLayer.Path]?](usdprim/spec/inherits.md)
  The authored inherit paths, or `nil` if none authored.
- [var isActive: Bool?](usdprim/spec/isactive.md)
  Whether this prim is active in composition, or `nil` if not authored.
- [var isInstanceable: Bool?](usdprim/spec/isinstanceable.md)
  Whether this prim is marked as an instance, or `nil` if not authored.
- [var kind: USDToken?](usdprim/spec/kind.md)
  The prim’s kind, or `nil` if not authored.
- [var name: USDToken](usdprim/spec/name.md)
  The prim’s local name.
- [var parent: USDPrim.Spec?](usdprim/spec/parent.md)
  The parent prim spec, or `nil` if this is a top-level prim spec.
- [var payloads: [USDPrim.Payload]?](usdprim/spec/payloads.md)
  The authored payloads on this prim, or `nil` if none authored.
- [var permission: USDLayer.Permission](usdprim/spec/permission.md)
  The prim’s permission level (public, restricted, private).
- [var prefix: String?](usdprim/spec/prefix.md)
  The authored prefix, or `nil` if not authored.
- [var prefixSubstitutions: Dictionary<String, USDValue>](usdprim/spec/prefixsubstitutions.md)
  The prefix substitutions dictionary.
- [var properties: [USDPrim.Property.Spec]](usdprim/spec/properties.md)
  All property specs (attributes and relationships) on this prim.
- [var propertyOrder: [USDToken]?](usdprim/spec/propertyorder.md)
  The authored override for property ordering, or `nil` if no order is authored.
- [var pseudoRoot: USDPrim.Spec?](usdprim/spec/pseudoroot.md)
  The pseudo-root prim spec at `/` in this spec’s layer.
- [var references: [USDPrim.Reference]?](usdprim/spec/references.md)
  The authored references on this prim, or `nil` if none authored.
- [var relationships: [USDPrim.Relationship.Spec]](usdprim/spec/relationships.md)
  All relationship specs on this prim.
- [var relocates: USDLayer.RelocatesMap?](usdprim/spec/relocates.md)
  The relocates map authored on this prim, or `nil` if none authored.
- [var specializes: [USDLayer.Path]?](usdprim/spec/specializes.md)
  The authored specializes paths, or `nil` if none authored.
- [var specifier: USDPrim.Specifier](usdprim/spec/specifier.md)
  How this prim definition composes — `def`, `over`, or `class`.
- [var suffix: String?](usdprim/spec/suffix.md)
  The authored suffix, or `nil` if not authored.
- [var suffixSubstitutions: Dictionary<String, USDValue>](usdprim/spec/suffixsubstitutions.md)
  The suffix substitutions dictionary.
- [var symmetricPeer: String?](usdprim/spec/symmetricpeer.md)
  The symmetric peer path, or `nil` if not authored.
- [var symmetryArguments: Dictionary<String, USDValue>](usdprim/spec/symmetryarguments.md)
  The symmetry arguments dictionary authored on this prim.
- [var symmetryFunction: USDToken?](usdprim/spec/symmetryfunction.md)
  The symmetry function token, or `nil` if not authored.
- [var typeName: USDToken](usdprim/spec/typename.md)
  The prim’s type name.
- [var variantSelections: [USDToken : USDToken]](usdprim/spec/variantselections.md)
  All authored variant selections, keyed by variant set name.
- [var variantSetNames: [USDToken]](usdprim/spec/variantsetnames.md)
  The names of variant sets defined on this prim.
- [var variantSets: [USDToken : USDPrim.VariantSetSpec]](usdprim/spec/variantsets.md)
  The variant sets authored on this prim, keyed by name.
### Instance Methods
- [func appendChild(USDPrim.Spec)](usdprim/spec/appendchild(_:).md)
  Appends `child` to the end of the children list.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute.Spec?](usdprim/spec/attribute(at:).md)
  Returns the attribute spec at the given path within this prim.
- [func blockVariantSelection(for: USDToken)](usdprim/spec/blockvariantselection(for:).md)
  Authors an explicit “no selection” for the given variant set.
- [func clearAssetInfo(String)](usdprim/spec/clearassetinfo(_:).md)
  Removes `key` from the asset info dictionary.
- [func clearCustomData(String)](usdprim/spec/clearcustomdata(_:).md)
  Removes `key` from the custom data dictionary.
- [func clearInherits()](usdprim/spec/clearinherits.md)
  Clears all authored inherit paths on this prim.
- [func clearPayloads()](usdprim/spec/clearpayloads.md)
  Clears all authored payloads on this prim.
- [func clearReferences()](usdprim/spec/clearreferences.md)
  Clears all authored references on this prim.
- [func clearRelocates()](usdprim/spec/clearrelocates.md)
  Clears all authored relocates on this prim.
- [func clearSpecializes()](usdprim/spec/clearspecializes.md)
  Clears all authored specializes paths on this prim.
- [func clearSymmetryArgument(String)](usdprim/spec/clearsymmetryargument(_:).md)
  Removes `name` from the symmetry arguments dictionary.
- [func clearVariantSelection(for: USDToken)](usdprim/spec/clearvariantselection(for:).md)
  Clears the variant selection for the given variant set.
- [func insertChild(USDPrim.Spec, at: Int)](usdprim/spec/insertchild(_:at:).md)
  Inserts `child` into the children list at `index`.
- [func prim(at: USDLayer.Path) -> USDPrim.Spec?](usdprim/spec/prim(at:).md)
  Returns the prim spec at the given path within this prim.
- [func property(at: USDLayer.Path) -> USDPrim.Property.Spec?](usdprim/spec/property(at:).md)
  Returns the property spec at the given path within this prim.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship.Spec?](usdprim/spec/relationship(at:).md)
  Returns the relationship spec at the given path within this prim.
- [func removeChild(USDPrim.Spec)](usdprim/spec/removechild(_:).md)
  Removes `child` from the children list. No-op if `child` is not a child of this spec.
- [func removeProperty(USDPrim.Property.Spec)](usdprim/spec/removeproperty(_:).md)
  Removes the given property spec from this prim.
- [func removeVariantSet(USDToken)](usdprim/spec/removevariantset(_:).md)
  Removes the variant set with the given name.
- [func rename(to: USDToken) throws](usdprim/spec/rename(to:).md)
  Sets the prim’s name.
- [func setAssetInfo(String, to: USDValue)](usdprim/spec/setassetinfo(_:to:).md)
  Sets `key` in the asset info dictionary to `value`.
- [func setCustomData(String, to: USDValue)](usdprim/spec/setcustomdata(_:to:).md)
  Sets `key` in the custom data dictionary to `value`.
- [func setSymmetryArgument(String, to: USDValue)](usdprim/spec/setsymmetryargument(_:to:).md)
  Sets `name` in the symmetry arguments dictionary to `value`.
- [func setVariantSelection(for: USDToken, to: USDToken)](usdprim/spec/setvariantselection(for:to:).md)
  Sets the variant selection for the given variant set.
- [func spec(at: USDLayer.Path) -> USDLayer.Spec?](usdprim/spec/spec(at:).md)
  Returns the spec at the given path within this prim.
- [func variantNames(in: USDToken) -> [USDToken]](usdprim/spec/variantnames(in:).md)
  Returns the variant names available in the given variant set.
- [func variantSelection(for: USDToken) -> USDToken?](usdprim/spec/variantselection(for:).md)
  Returns the authored variant selection for the given variant set.
### Type Methods
- [static func isValidName(USDToken) -> Bool](usdprim/spec/isvalidname(_:).md)
  Returns a Boolean value that indicates whether `name` is a valid prim name.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [USDLayer.Spec.FieldCollection](usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](usdlayer/spec/metadatacollection.md)

## See Also

- [USDPrim.PseudoRootSpec](usdprim/pseudorootspec.md)
  A handle to a layer’s pseudo-root — the implicit parent of all top-level prims in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/spec)*