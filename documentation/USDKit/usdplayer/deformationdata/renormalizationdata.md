# USDPlayer.DeformationData.RenormalizationData

**Framework**: USDKit  
**Kind**: struct

Triangle adjacency data for post-deformation normal renormalization.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/renormalizationdata)*