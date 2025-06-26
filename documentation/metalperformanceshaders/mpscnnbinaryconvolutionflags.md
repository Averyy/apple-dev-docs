# MPSCNNBinaryConvolutionFlags

**Framework**: Metal Performance Shaders  
**Kind**: enum

Options used to control binary convolution kernels.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MPSCNNBinaryConvolutionFlags
```

## Topics

### Enumeration Cases
- [MPSCNNBinaryConvolutionFlags.none](mpscnnbinaryconvolutionflags/none.md)
- [MPSCNNBinaryConvolutionFlags.useBetaScaling](mpscnnbinaryconvolutionflags/usebetascaling.md)
### Initializers
- [init?(rawValue: UInt)](mpscnnbinaryconvolutionflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnbinaryconvolution/init(coder:device:).md)
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryconvolution/init(device:convolutiondata:outputbiasterms:outputscaleterms:inputbiasterms:inputscaleterms:type:flags:).md)
  Initializes a binary convolution kernel.
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryconvolution/init(device:convolutiondata:scalevalue:type:flags:).md)
  Initializes a binary convolution kernel.
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [enum MPSCNNBinaryConvolutionType](mpscnnbinaryconvolutiontype.md)
  Options that defines what operations are used to perform binary convolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryconvolutionflags)*