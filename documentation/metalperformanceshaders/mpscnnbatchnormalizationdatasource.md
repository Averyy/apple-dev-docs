# MPSCNNBatchNormalizationDataSource

**Framework**: Metal Performance Shaders  
**Kind**: intf

A protocol that defines methods that a batch normalization state uses to initialize scale factors, bias terms, and batch statistics.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
protocol MPSCNNBatchNormalizationDataSource
```

## Topics

### Initializers
- [init?(coder: NSCoder)](mpscnnbatchnormalizationdatasource/2951886-init.md)
### Type Properties
- [static var supportsSecureCoding: Bool](mpscnnbatchnormalizationdatasource/2951887-supportssecurecoding.md)
### Instance Methods
- [func beta() -> UnsafeMutablePointer<Float>?](mpscnnbatchnormalizationdatasource/2942586-beta.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnnbatchnormalizationdatasource/3013773-copy.md)
- [func encode(with: NSCoder)](mpscnnbatchnormalizationdatasource/2951882-encode.md)
- [func epsilon() -> Float](mpscnnbatchnormalizationdatasource/2947917-epsilon.md)
- [func gamma() -> UnsafeMutablePointer<Float>?](mpscnnbatchnormalizationdatasource/2942605-gamma.md)
- [func label() -> String?](mpscnnbatchnormalizationdatasource/2953128-label.md)
- [func load() -> Bool](mpscnnbatchnormalizationdatasource/2942579-load.md)
- [func mean() -> UnsafeMutablePointer<Float>?](mpscnnbatchnormalizationdatasource/2942589-mean.md)
- [func numberOfFeatureChannels() -> Int](mpscnnbatchnormalizationdatasource/2942596-numberoffeaturechannels.md)
- [func purge()](mpscnnbatchnormalizationdatasource/2942607-purge.md)
- [func updateGammaAndBeta(with: MPSCNNBatchNormalizationState) -> Bool](mpscnnbatchnormalizationdatasource/2953129-updategammaandbeta.md)
- [func updateGammaAndBeta(with: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState) -> MPSCNNNormalizationGammaAndBetaState?](mpscnnbatchnormalizationdatasource/2951891-updategammaandbeta.md)
- [func updateMeanAndVariance(with: MPSCNNBatchNormalizationState) -> Bool](mpscnnbatchnormalizationdatasource/3002360-updatemeanandvariance.md)
- [func updateMeanAndVariance(with: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState) -> MPSCNNNormalizationMeanAndVarianceState?](mpscnnbatchnormalizationdatasource/3002361-updatemeanandvariance.md)
- [func variance() -> UnsafeMutablePointer<Float>?](mpscnnbatchnormalizationdatasource/2942592-variance.md)

## Relationships

### Inherits From
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class MPSCNNCrossChannelNormalizationNode](mpscnncrosschannelnormalizationnode.md)
  A representation of a normalization kernel across feature channels.
- [class MPSCNNLocalContrastNormalizationNode](mpscnnlocalcontrastnormalizationnode.md)
  A representation of a local-contrast normalization kernel.
- [class MPSCNNSpatialNormalizationNode](mpscnnspatialnormalizationnode.md)
  A representation of a spatial normalization kernel.
- [class MPSCNNBatchNormalizationGradientNode](mpscnnbatchnormalizationgradientnode.md)
  A representation of a gradient batch normalization kernel.
- [class MPSCNNBatchNormalizationNode](mpscnnbatchnormalizationnode.md)
  A representation of a batch normalization kernel.
- [class MPSCNNInstanceNormalizationGradientNode](mpscnninstancenormalizationgradientnode.md)
  A representation of a gradient instance normalization kernel.
- [protocol MPSCNNInstanceNormalizationDataSource](mpscnninstancenormalizationdatasource.md)
  A protocol that defines methods that an instance normalization uses to initialize scale factors and bias terms.
- [class MPSCNNInstanceNormalizationNode](mpscnninstancenormalizationnode.md)
  A representation of an instance normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradientNode](mpscnnlocalcontrastnormalizationgradientnode.md)
  A representation of a gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalizationGradientNode](mpscnnspatialnormalizationgradientnode.md)
  A representation of a gradient spatial normalization kernel.
- [class MPSCNNNormalizationNode](mpscnnnormalizationnode.md)
  Virtual base class for CNN normalization nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbatchnormalizationdatasource)*