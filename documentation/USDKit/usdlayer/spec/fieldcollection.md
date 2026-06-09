# USDLayer.Spec.FieldCollection

**Framework**: USDKit  
**Kind**: protocol

Low-level read/write access to spec fields. Fields are the raw data backing both metadata and structural information on a spec.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol FieldCollection
```

## Topics

### Instance Properties
- [var fields: [USDToken]](usdlayer/spec/fieldcollection/fields.md)
  All authored field names on this spec.
### Instance Methods
- [func clearField(USDToken) -> Bool](usdlayer/spec/fieldcollection/clearfield(_:).md)
  Clears the authored value for `name`.
- [func field(USDToken) -> USDValue?](usdlayer/spec/fieldcollection/field(_:).md)
  Returns the value of `name`, or `nil` if the field is unauthored.
- [func field<T>(USDToken, as: T.Type) -> T?](usdlayer/spec/fieldcollection/field(_:as:).md)
  Typed field accessor.
- [func isInert(ignoringChildren: Bool) -> Bool](usdlayer/spec/fieldcollection/isinert(ignoringchildren:).md)
  Returns a Boolean value that indicates whether the spec contains no authored data.
- [func setField(USDToken, to: USDValue) -> Bool](usdlayer/spec/fieldcollection/setfield(_:to:)-26nys.md)
  Sets the field `name` to `value`.
- [func setField<T>(USDToken, to: T) -> Bool](usdlayer/spec/fieldcollection/setfield(_:to:)-4lcqw.md)
  Typed field setter.

## Relationships

### Conforming Types
- [USDLayer.Spec](usdlayer/spec.md)
- [USDPrim.Attribute.Spec](usdprim/attribute/spec.md)
- [USDPrim.Property.Spec](usdprim/property/spec.md)
- [USDPrim.PseudoRootSpec](usdprim/pseudorootspec.md)
- [USDPrim.Relationship.Spec](usdprim/relationship/spec.md)
- [USDPrim.Spec](usdprim/spec.md)
- [USDPrim.VariantSetSpec](usdprim/variantsetspec.md)
- [USDPrim.VariantSpec](usdprim/variantspec.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/spec/fieldcollection)*