# init(owner:name:variability:isCustom:)

**Framework**: USDKit  
**Kind**: init

Creates a new relationship spec under the given prim spec.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init?(owner: USDPrim.Spec, name: USDToken, variability: USDPrim.Property.Variability = .varying, isCustom: Bool = true)
```

## Parameters

- `owner`: The prim spec that owns the new relationship.
- `name`: The relationship’s name.
- `variability`: The relationship’s variability.
- `isCustom`: Whether the relationship is authored as `custom`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship/spec/init(owner:name:variability:iscustom:))*