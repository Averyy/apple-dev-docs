# USDPlayer.DeformationData.RenormalizationData

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

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
- [USDPlayer.DeformationData.RenormalizationData.Update](./renormalizationdata/update.md)
  Delta update carrying only the adjacency fields that changed since the last frame.
### Instance Properties
- [let vertexAdjacencies: [UInt32]](./renormalizationdata/vertexadjacencies.md)
  Flattened list of triangle face indices adjacent to each vertex.
- [let vertexAdjacencyEndIndices: [UInt32]](./renormalizationdata/vertexadjacencyendindices.md)
  Cumulative end indices into `vertexAdjacencies`, one per vertex.
- [let vertexIndicesPerTriangle: [UInt32]](./renormalizationdata/vertexindicespertriangle.md)
  Vertex indices for each triangle, stored as three consecutive indices per triangle.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/renormalizationdata)*