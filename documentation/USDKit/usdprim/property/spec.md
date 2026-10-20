# USDPrim.Property.Spec

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A handle to a property definition (attribute or relationship) stored in a layer.

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

`USDPrim.Property.Spec` is the untyped base for `USDPrim.Attribute.Spec` and `USDPrim.Relationship.Spec`. It acts as a handle into data owned by a [`USDLayer`](../../usdlayer.md) and mutations write through to the layer.

## Topics

### Protocols
- [USDPrim.Property.Spec.SymmetryCollection](./spec/symmetrycollection.md)
  Symmetry and naming substitutions used in rigging.
- [USDPrim.Property.Spec.ValueCollection](./spec/valuecollection.md)
  Value-related API for property specs that hold typed default values.
### Initializers
- [init()](./spec/init%28%29.md)
  Creates an empty (invalid) property spec handle.
- [init?(USDLayer.Spec)](./spec/init%28_%29.md)
  Narrows an untyped [`USDLayer.Spec`](../../usdlayer/spec.md) to a property spec.
### Instance Properties
- [var comment: String?](./spec/comment.md)
  The authored user comment, or `nil` if not authored.
- [var customData: Dictionary<String, USDValue>](./spec/customdata.md)
  The custom data dictionary authored on this property.
- [var documentation: String?](./spec/documentation.md)
  The authored documentation, or `nil` if not authored.
- [var isCustom: Bool](./spec/iscustom.md)
  Whether this property was authored as `custom`.
- [var name: USDToken](./spec/name.md)
  The property’s local name.
- [var owner: USDLayer.Spec?](./spec/owner.md)
  The spec that contains this property — typically a prim spec or variant spec.
- [var permission: USDLayer.Permission](./spec/permission.md)
  The property’s permission level (public, restricted, private).
### Instance Methods
- [func clearAssetInfo(String)](./spec/clearassetinfo%28_%29.md)
  Removes `key` from the asset info dictionary.
- [func clearCustomData(String)](./spec/clearcustomdata%28_%29.md)
  Removes `key` from the custom data dictionary.
- [func rename(to: USDToken) throws](./spec/rename%28to%29.md)
  Sets the property’s name.
- [func setAssetInfo(String, to: USDValue)](./spec/setassetinfo%28_,to%29.md)
  Sets `key` in the asset info dictionary to `value`. Read the full dictionary via `field("assetInfo")` from FieldCollection.
- [func setCustomData(String, to: USDValue)](./spec/setcustomdata%28_,to%29.md)
  Sets `key` in the custom data dictionary to `value`.
### Type Methods
- [static func isValidName(USDToken) -> Bool](./spec/isvalidname%28_%29.md)
  Returns a Boolean value that indicates whether `name` is a valid property name.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [USDLayer.Spec.FieldCollection](../../usdlayer/spec/fieldcollection.md)
- [USDLayer.Spec.MetadataCollection](../../usdlayer/spec/metadatacollection.md)
- [USDPrim.Property.Spec.SymmetryCollection](./spec/symmetrycollection.md)
- [USDPrim.Property.Spec.ValueCollection](./spec/valuecollection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property/spec)*