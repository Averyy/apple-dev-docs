# init(assetPath:primPath:layerOffset:customData:)

**Framework**: USDKit  
**Kind**: init

Creates a reference.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(assetPath: String? = nil, primPath: USDLayer.Path? = nil, layerOffset: USDLayer.TimeOffset = USDLayer.TimeOffset(), customData: Dictionary<String, USDValue> = [:])
```

## Parameters

- `assetPath`: The asset path to target. Pass `nil` for an internal reference (pointing within the same layer stack).
- `primPath`: The prim path within the referenced asset. Pass `nil` to use the asset’s default prim.
- `layerOffset`: The time transformation applied during composition.
- `customData`: Custom data dictionary attached to the reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/reference/init(assetpath:primpath:layeroffset:customdata:))*