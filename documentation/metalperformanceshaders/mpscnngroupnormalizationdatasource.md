# MPSCNNGroupNormalizationDataSource

**Framework**: Metal Performance Shaders  
**Kind**: intf

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol MPSCNNGroupNormalizationDataSource
```

## Topics

### Initializers
- [init?(coder: NSCoder)](mpscnngroupnormalizationdatasource/3152548-init.md)
### Instance Properties
- [var numberOfFeatureChannels: Int](mpscnngroupnormalizationdatasource/3152550-numberoffeaturechannels.md)
- [var numberOfGroups: Int](mpscnngroupnormalizationdatasource/3152551-numberofgroups.md)
### Type Properties
- [static var supportsSecureCoding: Bool](mpscnngroupnormalizationdatasource/3152552-supportssecurecoding.md)
### Instance Methods
- [func beta() -> UnsafeMutablePointer<Float>?](mpscnngroupnormalizationdatasource/3152543-beta.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnngroupnormalizationdatasource/3152544-copy.md)
- [func encode(with: NSCoder)](mpscnngroupnormalizationdatasource/3152545-encode.md)
- [func epsilon() -> Float](mpscnngroupnormalizationdatasource/3152546-epsilon.md)
- [func gamma() -> UnsafeMutablePointer<Float>?](mpscnngroupnormalizationdatasource/3152547-gamma.md)
- [func label() -> String?](mpscnngroupnormalizationdatasource/3152549-label.md)
- [func updateGammaAndBeta(with: any MTLCommandBuffer, groupNormalizationStateBatch: [MPSCNNGroupNormalizationGradientState]) -> MPSCNNNormalizationGammaAndBetaState?](mpscnngroupnormalizationdatasource/3152553-updategammaandbeta.md)
- [func updateGammaAndBeta(withGroupNormalizationStateBatch: [MPSCNNGroupNormalizationGradientState]) -> Bool](mpscnngroupnormalizationdatasource/3152554-updategammaandbeta.md)

## Relationships

### Inherits From
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalizationdatasource)*