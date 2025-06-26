# MPSCNNFullyConnected

**Framework**: Metal Performance Shaders  
**Kind**: class

A fully connected convolution layer, also known as an inner product layer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNFullyConnected
```

#### Overview

A fully connected layer in  a Convolutional Neural Network (CNN) is one where every input channel is connected to every output channel. The kernel width is equal to the width of the source image, and the kernel height is equal to the height of the source image. The width and height of the output is `1 x 1`.

A fully connected layer takes an [`MPSImage`](mpsimage.md) object with dimensions `source.width x source.height x Ni`, convolves it with `Weights[No][source.width][source.height][Ni]`,` `and produces a `1 x 1 x No` output.

Thus, the following conditions must be true:

- `kernelWidth  == source.width`
- `kernelHeight == source.height`
- `clipRect.size.width == 1`
- `clipRect.size.height == 1`

You can think of a fully connected layer as a matrix multiplication where the image is flattened into a vector of length `source.width*source.height*Ni`, and the weights are arranged in a matrix of dimension `No x (source.width*source.height*Ni)` to produce an output vector of length `No`.

The value of the `strideInPixelsX`, [`strideInPixelsY`](mpscnnconvolutiondescriptor/strideinpixelsy.md), and [`groups`](mpscnnconvolution/groups.md) properties must be `1`. The [`offset`](mpscnnkernel/offset.md) property is not applicable and it is ignored. Because the clip rectangle is clamped to the destination image bounds, if the destination is `1 x 1`, you do not need to set the [`clipRect`](mpscnnkernel/cliprect.md) property.

> **Note**:  You can implement a fully connected convolution layer using an [`MPSCNNConvolution`](mpscnnconvolution.md) object by setting the following property values: `offset = (kernelWidth/2,kernelHeight/2)` `clipRect.origin = (ox,oy)` `clipRect.size = (1,1)` `strideInPixelsX = strideInPixelsY = groups = 1` However, using an [`MPSCNNFullyConnected`](mpscnnfullyconnected.md) object directly is better for performance as it lets the Metal Performance Shaders framework choose the most performant implementation method, which may not be possible when you use a general convolution. For example, the framework may internally use matrix multiplication or special reduction kernels for a specific Metal feature set.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnfullyconnected/init(coder:device:).md)
  Initializes a fully connected convolution layer.
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnfullyconnected/init(device:weights:).md)
  Initializes a fully connected convolution layer.
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [init(device: any MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)](mpscnnfullyconnected/init(device:convolutiondescriptor:kernelweights:biasterms:flags:).md)
  Initializes a fully connected convolution layer.
- [class MPSCNNConvolutionDescriptor](mpscnnconvolutiondescriptor.md)
  A description of the attributes of a convolution kernel.
- [enum MPSCNNConvolutionFlags](mpscnnconvolutionflags.md)
  Options used to control how kernel weights are stored and used in the CNN kernels

## Relationships

### Inherits From
- [MPSCNNConvolution](mpscnnconvolution.md)
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

- [class MPSCNNBinaryFullyConnected](mpscnnbinaryfullyconnected.md)
  A fully connected convolution layer with binary weights and optionally binarized input image.
- [class MPSCNNFullyConnectedGradient](mpscnnfullyconnectedgradient.md)
  A gradient fully connected convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnected)*