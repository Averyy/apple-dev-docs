# USDPrim.Attribute.Spec

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A handle to an attribute definition stored in a layer.

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

#### Overview

`USDPrim.Attribute.Spec` is a struct but acts as a handle into data owned by a [`USDLayer`](../../usdlayer.md). Mutations write through to the layer.

## Topics

### Initializers
- [init()](./spec/init%28%29.md)
  Creates an empty (invalid) attribute spec handle.
- [init?(USDLayer.Spec)](./spec/init%28_%29.md)
  Narrows an untyped [`USDLayer.Spec`](../../usdlayer/spec.md) to an attribute spec.
- [init?(layer: USDLayer, attributePath: USDLayer.Path, typeName: USDPrim.Attribute.ValueType, variability: USDPrim.Property.Variability, isCustom: Bool)](./spec/init%28layer,attributepath,typename,variability,iscustom%29.md)
  Creates an attribute spec at the given path in the layer, authoring intermediate ancestor prim specs as `over`s where needed.
- [init?(owner: USDPrim.Spec, name: USDToken, typeName: USDPrim.Attribute.ValueType, variability: USDPrim.Property.Variability, isCustom: Bool)](./spec/init%28owner,name,typename,variability,iscustom%29.md)
  Creates a new attribute spec under the given prim spec.
### Instance Properties
- [var colorSpace: USDToken?](./spec/colorspace.md)
  The authored color space, or `nil` if not authored. Assigning `nil` clears the color space.
- [var comment: String?](./spec/comment.md)
  The authored user comment, or `nil` if not authored.
- [var connectionPaths: [USDLayer.Path]?](./spec/connectionpaths.md)
  The authored connection paths, or `nil` if none authored.
- [var customData: Dictionary<String, USDValue>](./spec/customdata.md)
  The custom data dictionary authored on this attribute.
- [var documentation: String?](./spec/documentation.md)
  The authored documentation, or `nil` if not authored.
- [var isCustom: Bool](./spec/iscustom.md)
  Whether this attribute was authored as `custom`.
- [var name: USDToken](./spec/name.md)
  The attribute’s local name.
- [var owner: USDLayer.Spec?](./spec/owner.md)
  The spec that contains this attribute.
- [var permission: USDLayer.Permission](./spec/permission.md)
  The attribute’s permission level (public, restricted, private).
### Instance Methods
- [func clearAssetInfo(String)](./spec/clearassetinfo%28_%29.md)
  Removes `key` from the asset info dictionary.
- [func clearConnectionPaths()](./spec/clearconnectionpaths%28%29.md)
  Clears all authored connection paths on this attribute.
- [func clearCustomData(String)](./spec/clearcustomdata%28_%29.md)
  Removes `key` from the custom data dictionary.
- [func rename(to: USDToken) throws](./spec/rename%28to%29.md)
  Sets the attribute’s name.
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
- [USDPrim.Property.Spec.ValueCollection](../property/spec/valuecollection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/spec)*