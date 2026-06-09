# init(assetPath:primPath:layerOffset:)

**Framework**: USDKit  
**Kind**: init

Creates a payload.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(assetPath: String? = nil, primPath: USDLayer.Path? = nil, layerOffset: USDLayer.TimeOffset = USDLayer.TimeOffset())
```

## Parameters

- `assetPath`: The asset path to target. Pass `nil` if not yet set.
- `primPath`: The prim path within the referenced asset. Pass `nil` to use the asset’s default prim.
- `layerOffset`: The time transformation applied during composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/payload/init(assetpath:primpath:layeroffset:))*