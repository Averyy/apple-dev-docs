# USDPrim.Property.Spec.ValueCollection

**Framework**: USDKit  
**Kind**: protocol

Value-related API for property specs that hold typed default values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol ValueCollection
```

#### Overview

Only `USDPrim.Property.Spec` and `USDPrim.Attribute.Spec` conform to this protocol; `USDPrim.Relationship.Spec` does not, because relationships don’t store typed values.

## Topics

### Instance Properties
- [var defaultValue: USDValue?](usdprim/property/spec/valuecollection/defaultvalue.md)
  The authored default value, or `nil` if not authored. Assigning `nil` clears the default.
- [var typeName: USDPrim.Attribute.ValueType](usdprim/property/spec/valuecollection/typename.md)
  The property’s value type.
- [var variability: USDPrim.Property.Variability](usdprim/property/spec/valuecollection/variability.md)
  The property’s variability (varying, uniform, or config).

## Relationships

### Conforming Types
- [USDPrim.Attribute.Spec](usdprim/attribute/spec.md)
- [USDPrim.Property.Spec](usdprim/property/spec.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property/spec/valuecollection)*