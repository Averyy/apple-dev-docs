# USDPrim.Relationship.Spec

**Framework**: USDKit  
**Kind**: struct

A handle to a relationship definition stored in a layer.

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

Relationships store connections to other prims (target paths) rather than typed values. Used for scene linkages like material bindings, collection membership, and proxy references.

## Topics

### Initializers
- [init()](usdprim/relationship/spec/init.md)
  Creates an empty (invalid) relationship spec handle.
- [init?(USDLayer.Spec)](usdprim/relationship/spec/init(_:).md)
  Narrows an untyped [`USDLayer.Spec`](usdlayer/spec.md) to a relationship spec.
- [init?(layer: USDLayer, relationshipPath: USDLayer.Path, variability: USDPrim.Property.Variability, isCustom: Bool)](usdprim/relationship/spec/init(layer:relationshippath:variability:iscustom:).md)
  Creates a relationship spec at the given path in the layer, authoring intermediate ancestor prim specs as `over`s where needed.
- [init?(owner: USDPrim.Spec, name: USDToken, variability: USDPrim.Property.Variability, isCustom: Bool)](usdprim/relationship/spec/init(owner:name:variability:iscustom:).md)
  Creates a new relationship spec under the given prim spec.
### Instance Properties
- [var comment: String?](usdprim/relationship/spec/comment.md)
  The authored user comment, or `nil` if not authored.
- [var customData: Dictionary<String, USDValue>](usdprim/relationship/spec/customdata.md)
  The custom data dictionary authored on this relationship.
- [var documentation: String?](usdprim/relationship/spec/documentation.md)
  The authored documentation, or `nil` if not authored.
- [var isCustom: Bool](usdprim/relationship/spec/iscustom.md)
  Whether this relationship was authored as `custom`.
- [var name: USDToken](usdprim/relationship/spec/name.md)
  The relationship’s local name.
- [var noLoadHint: Bool](usdprim/relationship/spec/noloadhint.md)
  Hint to the runtime to skip loading payloads on targeted prims. Default: `false`.
- [var owner: USDLayer.Spec?](usdprim/relationship/spec/owner.md)
  The spec that contains this relationship.
- [var permission: USDLayer.Permission](usdprim/relationship/spec/permission.md)
  The relationship’s permission level (public, restricted, private).
- [var targetPaths: [USDLayer.Path]?](usdprim/relationship/spec/targetpaths.md)
  The authored target paths, or `nil` if none authored.
### Instance Methods
- [func clearAssetInfo(String)](usdprim/relationship/spec/clearassetinfo(_:).md)
  Removes `key` from the asset info dictionary.
- [func clearCustomData(String)](usdprim/relationship/spec/clearcustomdata(_:).md)
  Removes `key` from the custom data dictionary.
- [func clearTargetPaths()](usdprim/relationship/spec/cleartargetpaths.md)
  Clears all authored target paths on this relationship.
- [func removeTarget(USDLayer.Path, preservingOrder: Bool)](usdprim/relationship/spec/removetarget(_:preservingorder:).md)
  Removes an authored target path.
- [func rename(to: USDToken) throws](usdprim/relationship/spec/rename(to:).md)
  Sets the relationship’s name.
- [func replaceTarget(USDLayer.Path, with: USDLayer.Path)](usdprim/relationship/spec/replacetarget(_:with:).md)
  Replaces an authored target path with a new path.
- [func setAssetInfo(String, to: USDValue)](usdprim/relationship/spec/setassetinfo(_:to:).md)
  Sets `key` in the asset info dictionary to `value`. Read the full dictionary via `field("assetInfo")` from FieldCollection.
- [func setCustomData(String, to: USDValue)](usdprim/relationship/spec/setcustomdata(_:to:).md)
  Sets `key` in the custom data dictionary to `value`.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [USDLayer.Spec.FieldCollection](usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](usdlayer/spec/metadatacollection.md)
- [USDPrim.Property.Spec.SymmetryCollection](usdprim/property/spec/symmetrycollection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship/spec)*