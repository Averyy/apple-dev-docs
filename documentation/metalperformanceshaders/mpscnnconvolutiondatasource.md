# MPSCNNConvolutionDataSource

**Framework**: Metal Performance Shaders  
**Kind**: intf

The protocol that provides convolution filter weights and bias terms.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol MPSCNNConvolutionDataSource
```

## Topics

### Instance Methods
- [func biasTerms() -> UnsafeMutablePointer<Float>?](mpscnnconvolutiondatasource/2867023-biasterms.md)
- [func dataType() -> MPSDataType](mpscnnconvolutiondatasource/2867139-datatype.md)
- [func descriptor() -> MPSCNNConvolutionDescriptor](mpscnnconvolutiondatasource/2867050-descriptor.md)
- [func label() -> String?](mpscnnconvolutiondatasource/2881197-label.md)
- [func load() -> Bool](mpscnnconvolutiondatasource/2867049-load.md)
- [func lookupTableForUInt8Kernel() -> UnsafeMutablePointer<Float>](mpscnnconvolutiondatasource/2867186-lookuptableforuint8kernel.md)
- [func purge()](mpscnnconvolutiondatasource/2867134-purge.md)
- [func rangesForUInt8Kernel() -> UnsafeMutablePointer<vector_float2>](mpscnnconvolutiondatasource/2867145-rangesforuint8kernel.md)
- [func weights() -> UnsafeMutableRawPointer](mpscnnconvolutiondatasource/2867187-weights.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnnconvolutiondatasource/3013778-copy.md)
- [func kernelWeightsDataType() -> MPSDataType](mpscnnconvolutiondatasource/3564466-kernelweightsdatatype.md)
- [func update(with: any MTLCommandBuffer, gradientState: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> MPSCNNConvolutionWeightsAndBiasesState?](mpscnnconvolutiondatasource/2953007-update.md)
- [func update(with: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> Bool](mpscnnconvolutiondatasource/2953009-update.md)
- [func weightsLayout() -> MPSCNNConvolutionWeightsLayout](mpscnnconvolutiondatasource/3325840-weightslayout.md)
- [func weightsQuantizationType() -> MPSCNNWeightsQuantizationType](mpscnnconvolutiondatasource/2976466-weightsquantizationtype.md)

## Relationships

### Inherits From
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondatasource)*