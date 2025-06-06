# MPSCNNBinaryConvolutionType

**Framework**: Metal Performance Shaders  
**Kind**: enum

Options that defines what operations are used to perform binary convolution.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSCNNBinaryConvolutionType : UInt, @unchecked Sendable
```

## Topics

### Enumeration Cases
- [MPSCNNBinaryConvolutionType.AND](mpscnnbinaryconvolutiontype/and.md)
  A convolution type that uses input image binarization and the AND-operation.
- [MPSCNNBinaryConvolutionType.XNOR](mpscnnbinaryconvolutiontype/xnor.md)
  A convolution type that uses input image binarization and the XNOR-operation.
- [MPSCNNBinaryConvolutionType.binaryWeights](mpscnnbinaryconvolutiontype/binaryweights.md)
  A convolution type that operates as a normal convolution, except that the weights are binary values.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryconvolutiontype)*