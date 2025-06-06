# MPSCNNLocalContrastNormalizationNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a local-contrast normalization kernel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLocalContrastNormalizationNode : MPSCNNNormalizationNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode)](mpscnnlocalcontrastnormalizationnode/2866454-init.md)
- [init(source: MPSNNImageNode, kernelSize: Int)](mpscnnlocalcontrastnormalizationnode/2866473-init.md)
### Instance Properties
- [var kernelHeight: Int](mpscnnlocalcontrastnormalizationnode/2866485-kernelheight.md)
- [var kernelWidth: Int](mpscnnlocalcontrastnormalizationnode/2866441-kernelwidth.md)
- [var p0: Float](mpscnnlocalcontrastnormalizationnode/2866510-p0.md)
- [var pm: Float](mpscnnlocalcontrastnormalizationnode/2866404-pm.md)
- [var ps: Float](mpscnnlocalcontrastnormalizationnode/2866500-ps.md)

## Relationships

### Inherits From
- [MPSCNNNormalizationNode](mpscnnnormalizationnode.md)

## See Also

- [class MPSCNNCrossChannelNormalizationNode](mpscnncrosschannelnormalizationnode.md)
  A representation of a normalization kernel across feature channels.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalizationnode)*