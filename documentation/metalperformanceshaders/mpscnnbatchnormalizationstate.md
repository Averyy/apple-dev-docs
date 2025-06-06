# MPSCNNBatchNormalizationState

**Framework**: Metal Performance Shaders  
**Kind**: cl

An object that stores data required to execute batch normalization.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBatchNormalizationState : MPSNNGradientState
```

## Topics

### Instance Properties
- [var batchNormalization: MPSCNNBatchNormalization](mpscnnbatchnormalizationstate/2953969-batchnormalization.md)
### Instance Methods
- [func beta() -> (any MTLBuffer)?](mpscnnbatchnormalizationstate/2951888-beta.md)
- [func gamma() -> (any MTLBuffer)?](mpscnnbatchnormalizationstate/2951892-gamma.md)
- [func gradientForBeta() -> (any MTLBuffer)?](mpscnnbatchnormalizationstate/2951890-gradientforbeta.md)
- [func gradientForGamma() -> (any MTLBuffer)?](mpscnnbatchnormalizationstate/2951893-gradientforgamma.md)
- [func mean() -> (any MTLBuffer)?](mpscnnbatchnormalizationstate/2942612-mean.md)
- [func reset()](mpscnnbatchnormalizationstate/2942587-reset.md)
- [func variance() -> (any MTLBuffer)?](mpscnnbatchnormalizationstate/2942603-variance.md)

## Relationships

### Inherits From
- [MPSNNGradientState](mpsnngradientstate.md)

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
- [class MPSCNNBatchNormalization](mpscnnbatchnormalization.md)
  A batch normalization kernel.
- [class MPSCNNBatchNormalizationGradient](mpscnnbatchnormalizationgradient.md)
  A gradient batch normalization kernel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbatchnormalizationstate)*