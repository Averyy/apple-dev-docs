# MPSCNNBatchNormalization

**Framework**: Metal Performance Shaders  
**Kind**: cl

A batch normalization kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBatchNormalization : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnbatchnormalization/2942602-init.md)
- [init(device: any MTLDevice, dataSource: any MPSCNNBatchNormalizationDataSource)](mpscnnbatchnormalization/2942600-init.md)
- [init(device: any MTLDevice, dataSource: any MPSCNNBatchNormalizationDataSource, fusedNeuronDescriptor: MPSNNNeuronDescriptor?)](mpscnnbatchnormalization/3013771-init.md)
### Instance Properties
- [var dataSource: any MPSCNNBatchNormalizationDataSource](mpscnnbatchnormalization/2953967-datasource.md)
- [var epsilon: Float](mpscnnbatchnormalization/2942599-epsilon.md)
- [var numberOfFeatureChannels: Int](mpscnnbatchnormalization/2942604-numberoffeaturechannels.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceImage: MPSImage, batchNormalizationState: MPSCNNBatchNormalizationState, destinationImage: MPSImage)](mpscnnbatchnormalization/2942591-encode.md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [MPSImage], batchNormalizationState: MPSCNNBatchNormalizationState, destinationImages: [MPSImage])](mpscnnbatchnormalization/2942610-encodebatch.md)
- [func reloadDataSource(any MPSCNNBatchNormalizationDataSource)](mpscnnbatchnormalization/2942609-reloaddatasource.md)
- [func reloadGammaAndBeta(with: any MTLCommandBuffer, gammaAndBetaState: MPSCNNNormalizationGammaAndBetaState)](mpscnnbatchnormalization/2953965-reloadgammaandbeta.md)
- [func reloadGammaAndBetaFromDataSource()](mpscnnbatchnormalization/2976464-reloadgammaandbetafromdatasource.md)
- [func reloadMeanAndVariance(with: any MTLCommandBuffer, meanAndVarianceState: MPSCNNNormalizationMeanAndVarianceState)](mpscnnbatchnormalization/3002359-reloadmeanandvariance.md)
- [func reloadMeanAndVarianceFromDataSource()](mpscnnbatchnormalization/3002358-reloadmeanandvariancefromdatasou.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNBatchNormalizationState?](mpscnnbatchnormalization/2954874-resultstate.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNBatchNormalizationState?](mpscnnbatchnormalization/2954875-temporaryresultstate.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNCrossChannelNormalization](mpscnncrosschannelnormalization.md)
  A normalization kernel applied across feature channels.
- [class MPSCNNCrossChannelNormalizationGradient](mpscnncrosschannelnormalizationgradient.md)
  A gradient normalization kernel applied across feature channels.
- [class MPSCNNLocalContrastNormalization](mpscnnlocalcontrastnormalization.md)
  A local-contrast normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradient](mpscnnlocalcontrastnormalizationgradient.md)
  A gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalization](mpscnnspatialnormalization.md)
  A spatial normalization kernel.
- [class MPSCNNSpatialNormalizationGradient](mpscnnspatialnormalizationgradient.md)
  A gradient spatial normalization kernel.
- [class MPSCNNBatchNormalizationGradient](mpscnnbatchnormalizationgradient.md)
  A gradient batch normalization kernel.
- [class MPSCNNBatchNormalizationState](mpscnnbatchnormalizationstate.md)
  An object that stores data required to execute batch normalization.
- [class MPSCNNNormalizationMeanAndVarianceState](mpscnnnormalizationmeanandvariancestate.md)
  An object that stores mean and variance terms used to execute batch normalization.
- [class MPSCNNBatchNormalizationStatistics](mpscnnbatchnormalizationstatistics.md)
  An object that stores statistics required to execute batch normalization.
- [class MPSCNNBatchNormalizationStatisticsGradient](mpscnnbatchnormalizationstatisticsgradient.md)
  An object that stores the gradient of the loss function with respect to the batch statistics and batch normalization weights.
- [class MPSCNNInstanceNormalization](mpscnninstancenormalization.md)
  An instance normalization kernel.
- [class MPSCNNInstanceNormalizationGradient](mpscnninstancenormalizationgradient.md)
  A gradient instance normalization kernel.
- [class MPSCNNInstanceNormalizationGradientState](mpscnninstancenormalizationgradientstate.md)
  An object that stores information required to execute a gradient pass for instance normalization.
- [class MPSCNNNormalizationGammaAndBetaState](mpscnnnormalizationgammaandbetastate.md)
  An object that stores gamma and beta terms used to apply a scale and bias in instance- or batch-normalization operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbatchnormalization)*