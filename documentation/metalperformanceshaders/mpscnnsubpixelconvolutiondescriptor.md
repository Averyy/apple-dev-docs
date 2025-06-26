# MPSCNNSubPixelConvolutionDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

A description of a convolution object that does subpixel upsampling and reshaping.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNSubPixelConvolutionDescriptor
```

## Topics

### Instance Properties
- [var subPixelScaleFactor: Int](mpscnnsubpixelconvolutiondescriptor/subpixelscalefactor.md)

## Relationships

### Inherits From
- [MPSCNNConvolutionDescriptor](mpscnnconvolutiondescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSCNNBinaryConvolution](mpscnnbinaryconvolution.md)
  A convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolution](mpscnnconvolution.md)
  A convolution kernel that convolves the input image with a set of filters, with each producing one feature map in the output image.
- [class MPSCNNDepthWiseConvolutionDescriptor](mpscnndepthwiseconvolutiondescriptor.md)
  A description of a convolution object that does depthwise convolution.
- [class MPSCNNConvolutionTranspose](mpscnnconvolutiontranspose.md)
  A transposed convolution kernel.
- [class MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)
  A gradient convolution kernel.
- [class MPSCNNConvolutionGradientState](mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel’s gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnsubpixelconvolutiondescriptor)*