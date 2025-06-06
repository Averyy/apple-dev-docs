# MPSCNNSpatialNormalization

**Framework**: Metalperformanceshaders  
**Kind**: cl

A spatial normalization kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNSpatialNormalization : MPSCNNKernel
```

#### Overview

The spatial normalization for a feature channel applies the kernel over local regions which extend spatially, but are in separate feature channels (i.e., they have the shape `1 x kernel width x kernel height`).

For each feature channel, the function computes the sum of squares of `X` inside each rectangle, `N2(i,j)`. It then divides each element of `X` as follows:

![Y(i,j) = X(i,j) / (delta + alpha/(kw*kh) * N2(i,j))^beta](https://docs-assets.developer.apple.com/published/866dd98e74/887eebc5-2a18-404d-b9e9-83e1c2dda78f.png)

Where `kw` and `kh` are the values of the `kernelWidth` and `kernelHeight` properties, respectively. It is your responsibility to ensure that the combination of the values of the [`delta`](mpscnnspatialnormalization/1648933-delta.md) and [`alpha`](mpscnnspatialnormalization/1648825-alpha.md)`kernelWidth``kernelHeight` properties does not result in a situation where the denominator becomes zero (in such situations the resulting pixel-value is undefined).

> **Note**: The encoding methods in the [`MPSUnaryImageKernel`](mpsunaryimagekernel.md) class can be used to encode an [`MPSCNNSpatialNormalization`](mpscnnspatialnormalization.md) object to a [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer) object.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnspatialnormalization/2867021-init.md)
  Initializes a spatial normalization kernel.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)](mpscnnspatialnormalization/1648831-init.md)
  Initializes a spatial normalization kernel.
### Instance Properties
- [var alpha: Float](mpscnnspatialnormalization/1648825-alpha.md)
  The "alpha" variable of the kernel function.
- [var beta: Float](mpscnnspatialnormalization/1648936-beta.md)
  The "beta" variable of the kernel function.
- [var delta: Float](mpscnnspatialnormalization/1648933-delta.md)
  The "delta" variable of the kernel function.

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
- [class MPSCNNSpatialNormalizationGradient](mpscnnspatialnormalizationgradient.md)
  A gradient spatial normalization kernel.
- [class MPSCNNBatchNormalization](mpscnnbatchnormalization.md)
  A batch normalization kernel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnspatialnormalization)*