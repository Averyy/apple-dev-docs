# kernelWeightsDataType()

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func kernelWeightsDataType() -> MPSDataType
```

## See Also

- [func biasTerms() -> UnsafeMutablePointer<Float>?](mpscnnconvolutiondatasource/biasterms.md)
- [func dataType() -> MPSDataType](mpscnnconvolutiondatasource/datatype.md)
- [func descriptor() -> MPSCNNConvolutionDescriptor](mpscnnconvolutiondatasource/descriptor.md)
- [func label() -> String?](mpscnnconvolutiondatasource/label.md)
- [func load() -> Bool](mpscnnconvolutiondatasource/load.md)
- [func lookupTableForUInt8Kernel() -> UnsafeMutablePointer<Float>](mpscnnconvolutiondatasource/lookuptableforuint8kernel.md)
- [func purge()](mpscnnconvolutiondatasource/purge.md)
- [func rangesForUInt8Kernel() -> UnsafeMutablePointer<vector_float2>](mpscnnconvolutiondatasource/rangesforuint8kernel.md)
- [func weights() -> UnsafeMutableRawPointer](mpscnnconvolutiondatasource/weights.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnnconvolutiondatasource/copy(with:device:).md)
- [func update(with: any MTLCommandBuffer, gradientState: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> MPSCNNConvolutionWeightsAndBiasesState?](mpscnnconvolutiondatasource/update(with:gradientstate:sourcestate:).md)
- [func update(with: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> Bool](mpscnnconvolutiondatasource/update(with:sourcestate:).md)
- [func weightsLayout() -> MPSCNNConvolutionWeightsLayout](mpscnnconvolutiondatasource/weightslayout.md)
- [func weightsQuantizationType() -> MPSCNNWeightsQuantizationType](mpscnnconvolutiondatasource/weightsquantizationtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondatasource/kernelweightsdatatype())*