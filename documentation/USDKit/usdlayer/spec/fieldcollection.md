# USDLayer.Spec.FieldCollection

**Framework**: USDKit  
**Kind**: protocol  
**Role**: Protocol

Low-level read/write access to spec fields. Fields are the raw data backing both metadata and structural information on a spec.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol FieldCollection
```

## Topics

### Instance Properties
- [var fields: [USDToken]](./fieldcollection/fields.md)
  All authored field names on this spec.
### Instance Methods
- [func clearField(USDToken) -> Bool](./fieldcollection/clearfield%28_%29.md)
  Clears the authored value for `name`.
- [func field(USDToken) -> USDValue?](./fieldcollection/field%28_%29.md)
  Returns the value of `name`, or `nil` if the field is unauthored.
- [func field<T>(USDToken, as: T.Type) -> T?](./fieldcollection/field%28_,as%29.md)
  Typed field accessor.
- [func isInert(ignoringChildren: Bool) -> Bool](./fieldcollection/isinert%28ignoringchildren%29.md)
  Returns a Boolean value that indicates whether the spec contains no authored data.
- [func setField(USDToken, to: USDValue) -> Bool](./fieldcollection/setfield%28_,to%29-26nys.md)
  Sets the field `name` to `value`.
- [func setField<T>(USDToken, to: T) -> Bool](./fieldcollection/setfield%28_,to%29-4lcqw.md)
  Typed field setter.

## Relationships

### Conforming Types
- [USDLayer.Spec](../spec.md)
- [USDPrim.Attribute.Spec](../../usdprim/attribute/spec.md)
- [USDPrim.Property.Spec](../../usdprim/property/spec.md)
- [USDPrim.PseudoRootSpec](../../usdprim/pseudorootspec.md)
- [USDPrim.Relationship.Spec](../../usdprim/relationship/spec.md)
- [USDPrim.Spec](../../usdprim/spec.md)
- [USDPrim.VariantSetSpec](../../usdprim/variantsetspec.md)
- [USDPrim.VariantSpec](../../usdprim/variantspec.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/spec/fieldcollection)*