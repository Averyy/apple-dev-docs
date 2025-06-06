# MPSCNNGroupNormalization

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNGroupNormalization : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnngroupnormalization/3152536-init.md)
- [init(device: any MTLDevice, dataSource: any MPSCNNGroupNormalizationDataSource)](mpscnngroupnormalization/3152537-init.md)
### Instance Properties
- [var dataSource: any MPSCNNGroupNormalizationDataSource](mpscnngroupnormalization/3152534-datasource.md)
- [var epsilon: Float](mpscnngroupnormalization/3152535-epsilon.md)
### Instance Methods
- [func reloadGammaAndBeta(with: any MTLCommandBuffer, gammaAndBetaState: MPSCNNNormalizationGammaAndBetaState)](mpscnngroupnormalization/3152539-reloadgammaandbeta.md)
- [func reloadGammaAndBetaFromDataSource()](mpscnngroupnormalization/3152538-reloadgammaandbetafromdatasource.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNGroupNormalizationGradientState?](mpscnngroupnormalization/3152540-resultstate.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNGroupNormalizationGradientState?](mpscnngroupnormalization/3152541-temporaryresultstate.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalization)*