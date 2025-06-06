# MPSCNNLocalContrastNormalization

**Framework**: Metal Performance Shaders  
**Kind**: cl

A local-contrast normalization kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLocalContrastNormalization : MPSCNNKernel
```

#### Overview

The local contrast normalization kernel is quite similar to the spatial normalization kernel, described in the [`MPSCNNSpatialNormalization`](mpscnnspatialnormalization.md) class, in that it applies the kernel over local regions which extend spatially, but are in separate feature channels (i.e., they have the shape `1 x kernel width x kernel height`). However, instead of dividing by the local "energy" of the feature, the denominator uses the local variance of the feature - effectively the mean value of the feature is subtracted from the signal. For each feature channel, the function computes the variance `VAR(i,j)` and mean `M(i,j)` of `X(i,j)` inside each rectangle around the spatial point `(i,j)`. Then the result is computed for each element of `X` as follows:

![Y(i,j) = pm + ps * ( X(i,j) - p0 * M(i,j)) / (delta + alpha * VAR(i,j))^beta](https://docs-assets.developer.apple.com/published/866dd98e74/eaea8d5c-8e93-4ddf-ad7d-1fdb014fe6dc.png)

Where `kw` and `kh` are the values of the `kernelWidth` and the `kernelHeight` properties, respectively, and the values of the [`pm`](mpscnnlocalcontrastnormalization/1648907-pm.md), [`ps`](mpscnnlocalcontrastnormalization/1648942-ps.md), and [`p0`](mpscnnlocalcontrastnormalization/1648953-p0.md) properties can be used to offset and scale the result in various ways. For example setting `pm=0`, `ps=1`, `p0=1`, `delta=0`, `alpha=1.0` and `beta=0.5` scales input data so that the result has unit variance and zero mean, provided that input variance is positive.

It is your responsibility to ensure that the combination of the values of the [`delta`](mpscnnlocalcontrastnormalization/1648812-delta.md) and [`alpha`](mpscnnlocalcontrastnormalization/1648923-alpha.md) properties does not result in a situation where the denominator becomes zero - in such situations the resulting pixel-value is undefined. A good way to guard against tiny variances is to regulate the expression with a small delta value, for example `delta=1/1024`.

> 💡 **Tip**: The encoding methods in the [`MPSUnaryImageKernel`](mpsunaryimagekernel.md) class can be used to encode an [`MPSCNNLocalContrastNormalization`](mpscnnlocalcontrastnormalization.md) object to a [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer) object.

The encoding methods in the [`MPSUnaryImageKernel`](mpsunaryimagekernel.md) class can be used to encode an [`MPSCNNLocalContrastNormalization`](mpscnnlocalcontrastnormalization.md) object to a [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer) object.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnlocalcontrastnormalization/2867185-init.md)
  Initializes a local contrast normalization kernel.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)](mpscnnlocalcontrastnormalization/1648924-init.md)
  Initializes a local contrast normalization kernel.
### Instance Properties
- [var alpha: Float](mpscnnlocalcontrastnormalization/1648923-alpha.md)
  The "alpha" variable of the kernel function.
- [var beta: Float](mpscnnlocalcontrastnormalization/1648905-beta.md)
  The "beta" variable of the kernel function.
- [var delta: Float](mpscnnlocalcontrastnormalization/1648812-delta.md)
  The "delta" variable of the kernel function.
- [var p0: Float](mpscnnlocalcontrastnormalization/1648953-p0.md)
  The "p0" variable of the kernel function.
- [var pm: Float](mpscnnlocalcontrastnormalization/1648907-pm.md)
  The "pm" variable of the kernel function.
- [var ps: Float](mpscnnlocalcontrastnormalization/1648942-ps.md)
  The "ps" variable of the kernel function.

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNCrossChannelNormalization](mpscnncrosschannelnormalization.md)
  A normalization kernel applied across feature channels.
- [class MPSCNNCrossChannelNormalizationGradient](mpscnncrosschannelnormalizationgradient.md)
  A gradient normalization kernel applied across feature channels.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization)*