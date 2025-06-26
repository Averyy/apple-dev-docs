# MPSCNNBatchNormalizationDataSource

**Framework**: Metal Performance Shaders  
**Kind**: protocol

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
protocol MPSCNNBatchNormalizationDataSource : NSCopying, NSObjectProtocol
```

## Topics

### Initializers
- [init?(coder: NSCoder)](mpscnnbatchnormalizationdatasource/init(coder:).md)
### Instance Methods
- [func beta() -> UnsafeMutablePointer<Float>?](mpscnnbatchnormalizationdatasource/beta.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnnbatchnormalizationdatasource/copy(with:device:).md)
- [func encode(with: NSCoder)](mpscnnbatchnormalizationdatasource/encode(with:).md)
- [func epsilon() -> Float](mpscnnbatchnormalizationdatasource/epsilon.md)
- [func gamma() -> UnsafeMutablePointer<Float>?](mpscnnbatchnormalizationdatasource/gamma.md)
- [func label() -> String?](mpscnnbatchnormalizationdatasource/label.md)
- [func load() -> Bool](mpscnnbatchnormalizationdatasource/load.md)
- [func mean() -> UnsafeMutablePointer<Float>?](mpscnnbatchnormalizationdatasource/mean.md)
- [func numberOfFeatureChannels() -> Int](mpscnnbatchnormalizationdatasource/numberoffeaturechannels.md)
- [func purge()](mpscnnbatchnormalizationdatasource/purge.md)
- [func updateGammaAndBeta(with: MPSCNNBatchNormalizationState) -> Bool](mpscnnbatchnormalizationdatasource/updategammaandbeta(with:).md)
- [func updateGammaAndBeta(with: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState) -> MPSCNNNormalizationGammaAndBetaState?](mpscnnbatchnormalizationdatasource/updategammaandbeta(with:batchnormalizationstate:).md)
- [func updateMeanAndVariance(with: MPSCNNBatchNormalizationState) -> Bool](mpscnnbatchnormalizationdatasource/updatemeanandvariance(with:).md)
- [func updateMeanAndVariance(with: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState) -> MPSCNNNormalizationMeanAndVarianceState?](mpscnnbatchnormalizationdatasource/updatemeanandvariance(with:batchnormalizationstate:).md)
- [func variance() -> UnsafeMutablePointer<Float>?](mpscnnbatchnormalizationdatasource/variance.md)
### Type Properties
- [static var supportsSecureCoding: Bool](mpscnnbatchnormalizationdatasource/supportssecurecoding.md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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