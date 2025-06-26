# init(source:weights:scaleValue:type:flags:)

**Framework**: Metal Performance Shaders  
**Kind**: init

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(source sourceNode: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)
```

## See Also

- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryfullyconnectednode/init(source:weights:outputbiasterms:outputscaleterms:inputbiasterms:inputscaleterms:type:flags:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryfullyconnectednode/init(source:weights:scalevalue:type:flags:))*