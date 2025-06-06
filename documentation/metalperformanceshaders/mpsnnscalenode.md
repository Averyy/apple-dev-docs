# MPSNNScaleNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

Abstract node representing an image resampling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNScaleNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, outputSize: MTLSize)](mpsnnscalenode/2915285-init.md)
- [init(source: MPSNNImageNode, transformProvider: (any MPSImageTransformProvider)?, outputSize: MTLSize)](mpsnnscalenode/2915278-init.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)

## See Also

- [class MPSNNBilinearScaleNode](mpsnnbilinearscalenode.md)
  A representation of a bilinear resampling filter.
- [class MPSNNLanczosScaleNode](mpsnnlanczosscalenode.md)
  A representation of a Lanczos resampling filter.
- [protocol MPSImageTransformProvider](mpsimagetransformprovider.md)
  A general interface for objects that provide image resampling. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnscalenode)*