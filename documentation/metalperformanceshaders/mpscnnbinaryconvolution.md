# MPSCNNBinaryConvolution

**Framework**: Metal Performance Shaders  
**Kind**: cl

A convolution kernel with binary weights and an input image using binary approximations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBinaryConvolution : MPSCNNKernel
```

#### Overview

The [`MPSCNNBinaryConvolution`](mpscnnbinaryconvolution.md) optionally first binarizes the input image and then convolves the result with a set of binary-valued filters, each producing one feature map in the output image (which is a normal image).

The output is computed as follows: 

![out[i, x, y, c] = ( sum_{dx,dy,f} in[i,x+dx, y+dy, f] x B[c,dx,dy,f] ) * scale[c] * beta[i,x,y] + bias[c]](https://docs-assets.developer.apple.com/published/866dd98e74/bd225f43-535a-49b5-aaf0-bb7bc47f6a39.png)

where the   is over the spatial filter kernel window defined by [`kernelWidth`](mpscnnconvolutiondescriptor/1648959-kernelwidth.md) and [`kernelHeight`](mpscnnconvolutiondescriptor/1648904-kernelheight.md),   is over the input feature channel indices within group,  contains the binary weights, interpreted as `{-1, 1}` or `{0, 1}` and  is the `outputScaleTerms` array and bias is the `outputBiasTerms` array. Above  is the image index in batch the sum over input channels  runs through the group indices. The convolution operator ⊗ is defined by [`MPSCNNBinaryConvolutionType`](mpscnnbinaryconvolutiontype.md) passed in at initialization time of the filter:

The input data can be pre-offset and scaled by providing the `inputBiasTerms` and `inputScaleTerms` parameters for the initialization functions and this can be used for example to accomplish batch normalization of the data. The scaling of input values happens before possible beta-image computation. 

The parameter `beta` above is an optional image which is used to compute scaling factors for each spatial position and image index. For the XNOR-Net based networks this is computed as follows: 

![beta[i,x,y] = sum_{dx,dy} A[i, x+dx, y+dy] / (kx * ky)](https://docs-assets.developer.apple.com/published/866dd98e74/9f323d96-169d-441b-9126-33acfff420be.png)

where  are summed over the convolution filter window.

![[ -kx/2, (kx-1)/2], [ -ky/2, (ky-1)/2 ] and A[i,x,y] = sum_{c} abs( in[i,x,y,c] ) / Nc](https://docs-assets.developer.apple.com/published/866dd98e74/6ec9c656-8b23-4d5c-9716-ff947b9efadf.png)

where  is the original input image (in full precision) and  is the number of input channels in the input image. Parameter `beta` is not passed as input and to enable beta-scaling the user can provide [`MPSCNNBinaryConvolutionFlags.useBetaScaling`](mpscnnbinaryconvolutionflags/usebetascaling.md) in the flags parameter in the initialization functions. 

Finally the normal activation neuron is applied and the result is written to the output image. 

> **Note**: [`MPSCNNBinaryConvolution`](mpscnnbinaryconvolution.md) does not currently support [`groups`](mpscnnconvolutiondescriptor/1648849-groups.md) greater than 1.

[`MPSCNNBinaryConvolution`](mpscnnbinaryconvolution.md) does not currently support [`groups`](mpscnnconvolutiondescriptor/1648849-groups.md) greater than 1.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnbinaryconvolution/2867194-init.md)
- [init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryconvolution/2866978-init.md)
  Initializes a binary convolution kernel.
- [init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryconvolution/2866981-init.md)
  Initializes a binary convolution kernel.
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [enum MPSCNNBinaryConvolutionType](mpscnnbinaryconvolutiontype.md)
  Options that defines what operations are used to perform binary convolution.
- [enum MPSCNNBinaryConvolutionFlags](mpscnnbinaryconvolutionflags.md)
  Options used to control binary convolution kernels.
### Instance Properties
- [var inputFeatureChannels: Int](mpscnnbinaryconvolution/2867126-inputfeaturechannels.md)
- [var outputFeatureChannels: Int](mpscnnbinaryconvolution/2866959-outputfeaturechannels.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNConvolution](mpscnnconvolution.md)
  A convolution kernel that convolves the input image with a set of filters, with each producing one feature map in the output image.
- [class MPSCNNDepthWiseConvolutionDescriptor](mpscnndepthwiseconvolutiondescriptor.md)
  A description of a convolution object that does depthwise convolution.
- [class MPSCNNSubPixelConvolutionDescriptor](mpscnnsubpixelconvolutiondescriptor.md)
  A description of a convolution object that does subpixel upsampling and reshaping. 
- [class MPSCNNConvolutionTranspose](mpscnnconvolutiontranspose.md)
  A transposed convolution kernel.
- [class MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)
  A gradient convolution kernel.
- [class MPSCNNConvolutionGradientState](mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel's gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryconvolution)*