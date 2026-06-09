# USDPrim.Property.Spec

**Framework**: USDKit  
**Kind**: struct

A handle to a property definition (attribute or relationship) stored in a layer.

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

`USDPrim.Property.Spec` is the untyped base for `USDPrim.Attribute.Spec` and `USDPrim.Relationship.Spec`. It acts as a handle into data owned by a [`USDLayer`](usdlayer.md) and mutations write through to the layer.

## Topics

### Protocols
- [USDPrim.Property.Spec.SymmetryCollection](usdprim/property/spec/symmetrycollection.md)
  Symmetry and naming substitutions used in rigging.
- [USDPrim.Property.Spec.ValueCollection](usdprim/property/spec/valuecollection.md)
  Value-related API for property specs that hold typed default values.
### Initializers
- [init()](usdprim/property/spec/init.md)
  Creates an empty (invalid) property spec handle.
- [init?(USDLayer.Spec)](usdprim/property/spec/init(_:).md)
  Narrows an untyped [`USDLayer.Spec`](usdlayer/spec.md) to a property spec.
### Instance Properties
- [var comment: String?](usdprim/property/spec/comment.md)
  The authored user comment, or `nil` if not authored.
- [var customData: Dictionary<String, USDValue>](usdprim/property/spec/customdata.md)
  The custom data dictionary authored on this property.
- [var documentation: String?](usdprim/property/spec/documentation.md)
  The authored documentation, or `nil` if not authored.
- [var isCustom: Bool](usdprim/property/spec/iscustom.md)
  Whether this property was authored as `custom`.
- [var name: USDToken](usdprim/property/spec/name.md)
  The property’s local name.
- [var owner: USDLayer.Spec?](usdprim/property/spec/owner.md)
  The spec that contains this property — typically a prim spec or variant spec.
- [var permission: USDLayer.Permission](usdprim/property/spec/permission.md)
  The property’s permission level (public, restricted, private).
### Instance Methods
- [func clearAssetInfo(String)](usdprim/property/spec/clearassetinfo(_:).md)
  Removes `key` from the asset info dictionary.
- [func clearCustomData(String)](usdprim/property/spec/clearcustomdata(_:).md)
  Removes `key` from the custom data dictionary.
- [func rename(to: USDToken) throws](usdprim/property/spec/rename(to:).md)
  Sets the property’s name.
- [func setAssetInfo(String, to: USDValue)](usdprim/property/spec/setassetinfo(_:to:).md)
  Sets `key` in the asset info dictionary to `value`. Read the full dictionary via `field("assetInfo")` from FieldCollection.
- [func setCustomData(String, to: USDValue)](usdprim/property/spec/setcustomdata(_:to:).md)
  Sets `key` in the custom data dictionary to `value`.
### Type Methods
- [static func isValidName(USDToken) -> Bool](usdprim/property/spec/isvalidname(_:).md)
  Returns a Boolean value that indicates whether `name` is a valid property name.

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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property/spec)*