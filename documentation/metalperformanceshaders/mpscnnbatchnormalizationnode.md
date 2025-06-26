# MPSCNNBatchNormalizationNode

**Framework**: Metal Performance Shaders  
**Kind**: class

A representation of a batch normalization kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBatchNormalizationNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, dataSource: any MPSCNNBatchNormalizationDataSource)](mpscnnbatchnormalizationnode/init(source:datasource:).md)
### Instance Properties
- [var flags: MPSCNNBatchNormalizationFlags](mpscnnbatchnormalizationnode/flags.md)
- [var trainingStyle: MPSNNTrainingStyle](mpscnnbatchnormalizationnode/trainingstyle.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MPSNNTrainableNode](mpsnntrainablenode.md)
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
- [protocol MPSCNNBatchNormalizationDataSource](mpscnnbatchnormalizationdatasource.md)
  A protocol that defines methods that a batch normalization state uses to initialize scale factors, bias terms, and batch statistics.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbatchnormalizationnode)*