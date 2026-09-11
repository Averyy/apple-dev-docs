# init(assetPath:primPath:layerOffset:)

**Framework**: USDKit  
**Kind**: init

Creates a payload.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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