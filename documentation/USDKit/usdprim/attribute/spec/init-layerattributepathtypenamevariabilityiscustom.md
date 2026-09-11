# init(layer:attributePath:typeName:variability:isCustom:)

**Framework**: USDKit  
**Kind**: init

Creates an attribute spec at the given path in the layer, authoring intermediate ancestor prim specs as `over`s where needed.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init?(layer: USDLayer, attributePath: USDLayer.Path, typeName: USDPrim.Attribute.ValueType, variability: USDPrim.Property.Variability = .varying, isCustom: Bool = false)
```

## Parameters

- `layer`: The layer that owns the new attribute.
- `attributePath`: The full path of the attribute to author.
- `typeName`: The attribute’s value type.
- `variability`: The attribute’s variability.
- `isCustom`: Whether the attribute is authored as `custom`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/spec/init(layer:attributepath:typename:variability:iscustom:))*