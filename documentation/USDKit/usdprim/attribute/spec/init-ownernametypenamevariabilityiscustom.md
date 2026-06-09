# init(owner:name:typeName:variability:isCustom:)

**Framework**: USDKit  
**Kind**: init

Creates a new attribute spec under the given prim spec.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init?(owner: USDPrim.Spec, name: USDToken, typeName: USDPrim.Attribute.ValueType, variability: USDPrim.Property.Variability = .varying, isCustom: Bool = false)
```

## Parameters

- `owner`: The prim spec that owns the new attribute.
- `name`: The attribute’s name.
- `typeName`: The attribute’s value type.
- `variability`: The attribute’s variability.
- `isCustom`: Whether the attribute is authored as `custom`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/spec/init(owner:name:typename:variability:iscustom:))*