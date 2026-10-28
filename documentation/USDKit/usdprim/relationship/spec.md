# USDPrim.Relationship.Spec

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A handle to a relationship definition stored in a layer.

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

Relationships store connections to other prims (target paths) rather than typed values. Used for scene linkages like material bindings, collection membership, and proxy references.

## Topics

### Initializers
- [init()](./spec/init%28%29.md)
  Creates an empty (invalid) relationship spec handle.
- [init?(USDLayer.Spec)](./spec/init%28_%29.md)
  Narrows an untyped [`USDLayer.Spec`](../../usdlayer/spec.md) to a relationship spec.
- [init?(layer: USDLayer, relationshipPath: USDLayer.Path, variability: USDPrim.Property.Variability, isCustom: Bool)](./spec/init%28layer,relationshippath,variability,iscustom%29.md)
  Creates a relationship spec at the given path in the layer, authoring intermediate ancestor prim specs as `over`s where needed.
- [init?(owner: USDPrim.Spec, name: USDToken, variability: USDPrim.Property.Variability, isCustom: Bool)](./spec/init%28owner,name,variability,iscustom%29.md)
  Creates a new relationship spec under the given prim spec.
### Instance Properties
- [var comment: String?](./spec/comment.md)
  The authored user comment, or `nil` if not authored.
- [var customData: Dictionary<String, USDValue>](./spec/customdata.md)
  The custom data dictionary authored on this relationship.
- [var documentation: String?](./spec/documentation.md)
  The authored documentation, or `nil` if not authored.
- [var isCustom: Bool](./spec/iscustom.md)
  Whether this relationship was authored as `custom`.
- [var name: USDToken](./spec/name.md)
  The relationship’s local name.
- [var noLoadHint: Bool](./spec/noloadhint.md)
  Hint to the runtime to skip loading payloads on targeted prims. Default: `false`.
- [var owner: USDLayer.Spec?](./spec/owner.md)
  The spec that contains this relationship.
- [var permission: USDLayer.Permission](./spec/permission.md)
  The relationship’s permission level (public, restricted, private).
- [var targetPaths: [USDLayer.Path]?](./spec/targetpaths.md)
  The authored target paths, or `nil` if none authored.
### Instance Methods
- [func clearAssetInfo(String)](./spec/clearassetinfo%28_%29.md)
  Removes `key` from the asset info dictionary.
- [func clearCustomData(String)](./spec/clearcustomdata%28_%29.md)
  Removes `key` from the custom data dictionary.
- [func clearTargetPaths()](./spec/cleartargetpaths%28%29.md)
  Clears all authored target paths on this relationship.
- [func removeTarget(USDLayer.Path, preservingOrder: Bool)](./spec/removetarget%28_,preservingorder%29.md)
  Removes an authored target path.
- [func rename(to: USDToken) throws](./spec/rename%28to%29.md)
  Sets the relationship’s name.
- [func replaceTarget(USDLayer.Path, with: USDLayer.Path)](./spec/replacetarget%28_,with%29.md)
  Replaces an authored target path with a new path.
- [func setAssetInfo(String, to: USDValue)](./spec/setassetinfo%28_,to%29.md)
  Sets `key` in the asset info dictionary to `value`. Read the full dictionary via `field("assetInfo")` from FieldCollection.
- [func setCustomData(String, to: USDValue)](./spec/setcustomdata%28_,to%29.md)
  Sets `key` in the custom data dictionary to `value`.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [USDLayer.Spec.FieldCollection](../../usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](../../usdlayer/spec/metadatacollection.md)
- [USDPrim.Property.Spec.SymmetryCollection](../property/spec/symmetrycollection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship/spec)*