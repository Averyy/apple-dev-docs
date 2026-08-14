# USDPlayer.DeformationData.RenormalizationData.Update

**Framework**: USDKit  
**Kind**: struct

Delta update carrying only the adjacency fields that changed since the last frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Update
```

## Topics

### Instance Properties
- [let vertexAdjacencies: [UInt32]?](usdplayer/deformationdata/renormalizationdata/update/vertexadjacencies.md)
  Changed vertex adjacency data.
- [let vertexAdjacencyEndIndices: [UInt32]?](usdplayer/deformationdata/renormalizationdata/update/vertexadjacencyendindices.md)
  Changed vertex adjacency end indices.
- [let vertexIndicesPerTriangle: [UInt32]?](usdplayer/deformationdata/renormalizationdata/update/vertexindicespertriangle.md)
  Changed vertex indices per triangle.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/renormalizationdata/update)*