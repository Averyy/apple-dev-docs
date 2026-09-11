# add(to:from:layerOffset:position:)

**Framework**: USDKit  
**Kind**: method

Adds an external reference arc.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func add(to primPath: USDLayer.Path?, from assetPath: String, layerOffset: USDLayer.TimeOffset = .init(), position: USDPrim.ListPosition = .backOfPrependList) throws
```

#### Discussion

> **Note**: An error if the reference cannot be added.

## Parameters

- `primPath`: The prim path within the target asset. Pass `nil` to target the asset’s default prim.
- `assetPath`: The asset path of the external layer to load.
- `layerOffset`: Time offset and scale to apply during composition.
- `position`: Where to insert the reference in the prim’s reference list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/referencecollection/add(to:from:layeroffset:position:))*