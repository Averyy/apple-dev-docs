# defaultPrim

**Framework**: USDKit  
**Kind**: property

The name of the layer’s default prim — the prim referenced when this layer is included as a reference or payload without specifying a target. `nil` if not authored.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var defaultPrim: USDToken? { get nonmutating set }
```

## See Also

- [var subLayerPaths: [USDLayer.AssetPath]](usdlayer/sublayerpaths.md)
  The asset paths of the layer’s sublayers, ordered from strongest to weakest opinion.
- [USDLayer.AssetPath](usdlayer/assetpath.md)
  A reference to an external asset such as a texture, audio file, or USD layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/defaultprim)*