# MPSCNNInstanceNormalizationDataSource

**Framework**: Metal Performance Shaders  
**Kind**: intf

A protocol that defines methods that an instance normalization uses to initialize scale factors and bias terms.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
protocol MPSCNNInstanceNormalizationDataSource
```

## Topics

### Initializers
- [init?(coder: NSCoder)](mpscnninstancenormalizationdatasource/2947957-init.md)
### Instance Properties
- [var numberOfFeatureChannels: Int](mpscnninstancenormalizationdatasource/2947961-numberoffeaturechannels.md)
### Type Properties
- [static var supportsSecureCoding: Bool](mpscnninstancenormalizationdatasource/2947952-supportssecurecoding.md)
### Instance Methods
- [func beta() -> UnsafeMutablePointer<Float>?](mpscnninstancenormalizationdatasource/2953922-beta.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnninstancenormalizationdatasource/3013780-copy.md)
- [func encode(with: NSCoder)](mpscnninstancenormalizationdatasource/2947953-encode.md)
- [func epsilon() -> Float](mpscnninstancenormalizationdatasource/2953925-epsilon.md)
- [func gamma() -> UnsafeMutablePointer<Float>?](mpscnninstancenormalizationdatasource/2953923-gamma.md)
- [func label() -> String?](mpscnninstancenormalizationdatasource/2952998-label.md)
- [func load() -> Bool](mpscnninstancenormalizationdatasource/3088878-load.md)
- [func purge()](mpscnninstancenormalizationdatasource/3088879-purge.md)
- [func updateGammaAndBeta(with: any MTLCommandBuffer, instanceNormalizationStateBatch: [MPSCNNInstanceNormalizationGradientState]) -> MPSCNNNormalizationGammaAndBetaState?](mpscnninstancenormalizationdatasource/2953926-updategammaandbeta.md)
- [func updateGammaAndBeta(withInstanceNormalizationStateBatch: [MPSCNNInstanceNormalizationGradientState]) -> Bool](mpscnninstancenormalizationdatasource/2953931-updategammaandbeta.md)

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
- [protocol MPSCNNBatchNormalizationDataSource](mpscnnbatchnormalizationdatasource.md)
  A protocol that defines methods that a batch normalization state uses to initialize scale factors, bias terms, and batch statistics.
- [class MPSCNNInstanceNormalizationGradientNode](mpscnninstancenormalizationgradientnode.md)
  A representation of a gradient instance normalization kernel.
- [class MPSCNNInstanceNormalizationNode](mpscnninstancenormalizationnode.md)
  A representation of an instance normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradientNode](mpscnnlocalcontrastnormalizationgradientnode.md)
  A representation of a gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalizationGradientNode](mpscnnspatialnormalizationgradientnode.md)
  A representation of a gradient spatial normalization kernel.
- [class MPSCNNNormalizationNode](mpscnnnormalizationnode.md)
  Virtual base class for CNN normalization nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnninstancenormalizationdatasource)*