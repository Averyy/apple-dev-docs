# USDPlayer.DeformationData.RenormalizationData

**Framework**: USDKit  
**Kind**: struct

Triangle adjacency data for post-deformation normal renormalization.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RenormalizationData
```

## Topics

### Structures
- [USDPlayer.DeformationData.RenormalizationData.Update](usdplayer/deformationdata/renormalizationdata/update.md)
  Delta update carrying only the adjacency fields that changed since the last frame.
### Instance Properties
- [let vertexAdjacencies: [UInt32]](usdplayer/deformationdata/renormalizationdata/vertexadjacencies.md)
  Flattened list of triangle face indices adjacent to each vertex.
- [let vertexAdjacencyEndIndices: [UInt32]](usdplayer/deformationdata/renormalizationdata/vertexadjacencyendindices.md)
  Cumulative end indices into `vertexAdjacencies`, one per vertex.
- [let vertexIndicesPerTriangle: [UInt32]](usdplayer/deformationdata/renormalizationdata/vertexindicespertriangle.md)
  Vertex indices for each triangle, stored as three consecutive indices per triangle.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/renormalizationdata)*