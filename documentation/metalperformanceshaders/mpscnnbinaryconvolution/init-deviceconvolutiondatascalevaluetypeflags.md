# init(device:convolutionData:scaleValue:type:flags:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a binary convolution kernel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)
```

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnbinaryconvolution/init(coder:device:).md)
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryconvolution/init(device:convolutiondata:outputbiasterms:outputscaleterms:inputbiasterms:inputscaleterms:type:flags:).md)
  Initializes a binary convolution kernel.
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [enum MPSCNNBinaryConvolutionType](mpscnnbinaryconvolutiontype.md)
  Options that defines what operations are used to perform binary convolution.
- [enum MPSCNNBinaryConvolutionFlags](mpscnnbinaryconvolutionflags.md)
  Options used to control binary convolution kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryconvolution/init(device:convolutiondata:scalevalue:type:flags:))*