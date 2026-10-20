# USDLayer.AssetPath

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A reference to an external asset such as a texture, audio file, or USD layer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct AssetPath
```

#### Overview

Stores both the authored path (the string as written in USD) and the resolved path (the location after asset resolution, which may be empty if resolution did not run or failed). The resolved path is not guaranteed to be a filesystem path — custom asset resolvers may return URLs, database identifiers, or opaque tokens.

## Topics

### Initializers
- [init()](./assetpath/init%28%29.md)
  Creates an empty asset path.
- [init(String)](./assetpath/init%28_%29.md)
  Creates an asset path from a string identifier.
- [init(String, resolvedPath: String)](./assetpath/init%28_,resolvedpath%29.md)
  Creates an asset path with both authored and resolved values.
### Instance Properties
- [var authoredPath: String](./assetpath/authoredpath.md)
  The authored path string — the value as written in the USD file.
- [var resolvedPath: String?](./assetpath/resolvedpath.md)
  The resolved location after asset resolution, or `nil` if resolution did not run or failed.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](../usdprim/attribute/value.md)
- [USDValueProtocol](../usdvalueprotocol.md)

## See Also

### Composing the scene
- [var defaultPrim: USDToken?](./defaultprim.md)
  The name of the layer’s default prim — the prim referenced when this layer is included as a reference or payload without specifying a target. `nil` if not authored.
- [var subLayerPaths: [USDLayer.AssetPath]](./sublayerpaths.md)
  The asset paths of the layer’s sublayers, ordered from strongest to weakest opinion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/assetpath)*