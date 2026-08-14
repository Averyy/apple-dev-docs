# USDLayer.AssetPath

**Framework**: USDKit  
**Kind**: struct

A reference to an external asset such as a texture, audio file, or USD layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct AssetPath
```

#### Overview

Stores both the authored path (the string as written in USD) and the resolved path (the location after asset resolution, which may be empty if resolution did not run or failed). The resolved path is not guaranteed to be a filesystem path — custom asset resolvers may return URLs, database identifiers, or opaque tokens.

## Topics

### Initializers
- [init()](usdlayer/assetpath/init.md)
  Creates an empty asset path.
- [init(String)](usdlayer/assetpath/init(_:).md)
  Creates an asset path from a string identifier.
- [init(String, resolvedPath: String)](usdlayer/assetpath/init(_:resolvedpath:).md)
  Creates an asset path with both authored and resolved values.
### Instance Properties
- [var authoredPath: String](usdlayer/assetpath/authoredpath.md)
  The authored path string — the value as written in the USD file.
- [var resolvedPath: String?](usdlayer/assetpath/resolvedpath.md)
  The resolved location after asset resolution, or `nil` if resolution did not run or failed.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDValueProtocol](usdvalueprotocol.md)

## See Also

- [var defaultPrim: USDToken?](usdlayer/defaultprim.md)
  The name of the layer’s default prim — the prim referenced when this layer is included as a reference or payload without specifying a target. `nil` if not authored.
- [var subLayerPaths: [USDLayer.AssetPath]](usdlayer/sublayerpaths.md)
  The asset paths of the layer’s sublayers, ordered from strongest to weakest opinion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/assetpath)*