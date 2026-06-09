# USDPrim.Attribute.Spec

**Framework**: USDKit  
**Kind**: struct

A handle to an attribute definition stored in a layer.

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

`USDPrim.Attribute.Spec` is a struct but acts as a handle into data owned by a [`USDLayer`](usdlayer.md). Mutations write through to the layer.

## Topics

### Initializers
- [init()](usdprim/attribute/spec/init.md)
  Creates an empty (invalid) attribute spec handle.
- [init?(USDLayer.Spec)](usdprim/attribute/spec/init(_:).md)
  Narrows an untyped [`USDLayer.Spec`](usdlayer/spec.md) to an attribute spec.
- [init?(layer: USDLayer, attributePath: USDLayer.Path, typeName: USDPrim.Attribute.ValueType, variability: USDPrim.Property.Variability, isCustom: Bool)](usdprim/attribute/spec/init(layer:attributepath:typename:variability:iscustom:).md)
  Creates an attribute spec at the given path in the layer, authoring intermediate ancestor prim specs as `over`s where needed.
- [init?(owner: USDPrim.Spec, name: USDToken, typeName: USDPrim.Attribute.ValueType, variability: USDPrim.Property.Variability, isCustom: Bool)](usdprim/attribute/spec/init(owner:name:typename:variability:iscustom:).md)
  Creates a new attribute spec under the given prim spec.
### Instance Properties
- [var colorSpace: USDToken?](usdprim/attribute/spec/colorspace.md)
  The authored color space, or `nil` if not authored. Assigning `nil` clears the color space.
- [var comment: String?](usdprim/attribute/spec/comment.md)
  The authored user comment, or `nil` if not authored.
- [var connectionPaths: [USDLayer.Path]?](usdprim/attribute/spec/connectionpaths.md)
  The authored connection paths, or `nil` if none authored.
- [var customData: Dictionary<String, USDValue>](usdprim/attribute/spec/customdata.md)
  The custom data dictionary authored on this attribute.
- [var documentation: String?](usdprim/attribute/spec/documentation.md)
  The authored documentation, or `nil` if not authored.
- [var isCustom: Bool](usdprim/attribute/spec/iscustom.md)
  Whether this attribute was authored as `custom`.
- [var name: USDToken](usdprim/attribute/spec/name.md)
  The attribute’s local name.
- [var owner: USDLayer.Spec?](usdprim/attribute/spec/owner.md)
  The spec that contains this attribute.
- [var permission: USDLayer.Permission](usdprim/attribute/spec/permission.md)
  The attribute’s permission level (public, restricted, private).
### Instance Methods
- [func clearAssetInfo(String)](usdprim/attribute/spec/clearassetinfo(_:).md)
  Removes `key` from the asset info dictionary.
- [func clearConnectionPaths()](usdprim/attribute/spec/clearconnectionpaths.md)
  Clears all authored connection paths on this attribute.
- [func clearCustomData(String)](usdprim/attribute/spec/clearcustomdata(_:).md)
  Removes `key` from the custom data dictionary.
- [func rename(to: USDToken) throws](usdprim/attribute/spec/rename(to:).md)
  Sets the attribute’s name.
- [func setAssetInfo(String, to: USDValue)](usdprim/attribute/spec/setassetinfo(_:to:).md)
  Sets `key` in the asset info dictionary to `value`. Read the full dictionary via `field("assetInfo")` from FieldCollection.
- [func setCustomData(String, to: USDValue)](usdprim/attribute/spec/setcustomdata(_:to:).md)
  Sets `key` in the custom data dictionary to `value`.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [USDLayer.Spec.FieldCollection](usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](usdlayer/spec/metadatacollection.md)
- [USDPrim.Property.Spec.SymmetryCollection](usdprim/property/spec/symmetrycollection.md)
- [USDPrim.Property.Spec.ValueCollection](usdprim/property/spec/valuecollection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/spec)*