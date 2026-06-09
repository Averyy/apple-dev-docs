# init(layer:relationshipPath:variability:isCustom:)

**Framework**: USDKit  
**Kind**: init

Creates a relationship spec at the given path in the layer, authoring intermediate ancestor prim specs as `over`s where needed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init?(layer: USDLayer, relationshipPath: USDLayer.Path, variability: USDPrim.Property.Variability = .varying, isCustom: Bool = false)
```

## Parameters

- `layer`: The layer that owns the new relationship.
- `relationshipPath`: The full path of the relationship to author.
- `variability`: The relationship’s variability.
- `isCustom`: Whether the relationship is authored as `custom`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship/spec/init(layer:relationshippath:variability:iscustom:))*