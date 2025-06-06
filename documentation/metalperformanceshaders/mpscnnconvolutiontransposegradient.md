# MPSCNNConvolutionTransposeGradient

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
class MPSCNNConvolutionTransposeGradient : MPSCNNGradientKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolutiontransposegradient/3131783-init.md)
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolutiontransposegradient/3131784-init.md)
### Instance Properties
- [var dataSource: any MPSCNNConvolutionDataSource](mpscnnconvolutiontransposegradient/3131780-datasource.md)
- [var gradientOption: MPSCNNConvolutionGradientOption](mpscnnconvolutiontransposegradient/3131781-gradientoption.md)
- [var groups: Int](mpscnnconvolutiontransposegradient/3131782-groups.md)
- [var sourceGradientFeatureChannels: Int](mpscnnconvolutiontransposegradient/3131787-sourcegradientfeaturechannels.md)
- [var sourceImageFeatureChannels: Int](mpscnnconvolutiontransposegradient/3131788-sourceimagefeaturechannels.md)
### Instance Methods
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](mpscnnconvolutiontransposegradient/3131786-reloadweightsandbiases.md)
- [func reloadWeightsAndBiasesFromDataSource()](mpscnnconvolutiontransposegradient/3131785-reloadweightsandbiasesfromdataso.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontransposegradient)*