# label()

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func label() -> String?
```

## See Also

- [func biasTerms() -> UnsafeMutablePointer<Float>?](mpscnnconvolutiondatasource/biasterms.md)
- [func dataType() -> MPSDataType](mpscnnconvolutiondatasource/datatype.md)
- [func descriptor() -> MPSCNNConvolutionDescriptor](mpscnnconvolutiondatasource/descriptor.md)
- [func load() -> Bool](mpscnnconvolutiondatasource/load.md)
- [func lookupTableForUInt8Kernel() -> UnsafeMutablePointer<Float>](mpscnnconvolutiondatasource/lookuptableforuint8kernel.md)
- [func purge()](mpscnnconvolutiondatasource/purge.md)
- [func rangesForUInt8Kernel() -> UnsafeMutablePointer<vector_float2>](mpscnnconvolutiondatasource/rangesforuint8kernel.md)
- [func weights() -> UnsafeMutableRawPointer](mpscnnconvolutiondatasource/weights.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnnconvolutiondatasource/copy(with:device:).md)
- [func kernelWeightsDataType() -> MPSDataType](mpscnnconvolutiondatasource/kernelweightsdatatype.md)
- [func update(with: any MTLCommandBuffer, gradientState: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> MPSCNNConvolutionWeightsAndBiasesState?](mpscnnconvolutiondatasource/update(with:gradientstate:sourcestate:).md)
- [func update(with: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> Bool](mpscnnconvolutiondatasource/update(with:sourcestate:).md)
- [func weightsLayout() -> MPSCNNConvolutionWeightsLayout](mpscnnconvolutiondatasource/weightslayout.md)
- [func weightsQuantizationType() -> MPSCNNWeightsQuantizationType](mpscnnconvolutiondatasource/weightsquantizationtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondatasource/label())*