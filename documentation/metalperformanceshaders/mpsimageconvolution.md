# MPSImageConvolution

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that convolves an image with a given kernel of odd width and height.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageConvolution : MPSUnaryImageKernel
```

#### Overview

Filter width and height can be either 3, 5, 7 or 9. If there are multiple channels in the source image, each channel is processed independently.

A  convolution filter may perform better when done in two passes. . A convolution filter is separable if the ratio of filter values between all rows is constant over the whole row. For example, this edge detection filter:

![](https://docs-assets.developer.apple.com/published/abfee686ac/VectorMatrix01_2x_a03a022f-6d2f-43f5-ba8f-3711489c406a.png)

Can instead be separated into the product of two vectors, like so:

![](https://docs-assets.developer.apple.com/published/abfee686ac/VectorMatrix02_2x_e5a28187-8ff1-4754-bb5b-29973040ade9.png)

And consequently can be done as two, one-dimensional convolution passes back to back on the same image. In this way, the number of multiplies (ignoring the fact that we could skip zeros here) is reduced from `3*3=9` to `3+3=6`. There are similar savings for addition. For large filters, the savings can be profound.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimageconvolution/2866148-init.md)
### Methods
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, weights: UnsafePointer<Float>)](mpsimageconvolution/1618902-init.md)
  Initializes a convolution filter.
### Properties
- [var kernelHeight: Int](mpsimageconvolution/1618842-kernelheight.md)
  The height of the filter window. Must be an odd number.
- [var kernelWidth: Int](mpsimageconvolution/1618868-kernelwidth.md)
  The width of the filter window. Must be an odd number.
- [var bias: Float](mpsimageconvolution/1618841-bias.md)
  The value added to a convolved pixel before it is converted back to its intended storage format.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)

## See Also

- [class MPSImageMedian](mpsimagemedian.md)
  A filter that applies a median filter in a square region centered around each pixel in the source image.
- [class MPSImageBox](mpsimagebox.md)
  A filter that convolves an image with a given kernel of odd width and height.
- [class MPSImageTent](mpsimagetent.md)
  A filter that convolves an image with a tent filter.
- [class MPSImageGaussianBlur](mpsimagegaussianblur.md)
  A filter that convolves an image with a Gaussian blur of a given sigma in both the x and y directions.
- [class MPSImageGaussianPyramid](mpsimagegaussianpyramid.md)
  A filter that convolves an image with a Gaussian pyramid.
- [class MPSImageSobel](mpsimagesobel.md)
  A filter that convolves an image with the Sobel operator.
- [class MPSImageLaplacian](mpsimagelaplacian.md)
  An optimized Laplacian filter, provided for ease of use.
- [class MPSImageLaplacianPyramid](mpsimagelaplacianpyramid.md)
  A filter that convolves an image with a Laplacian filter.
- [class MPSImageLaplacianPyramidAdd](mpsimagelaplacianpyramidadd.md)
  A filter that convolves an image with an additive Laplacian pyramid.
- [class MPSImageLaplacianPyramidSubtract](mpsimagelaplacianpyramidsubtract.md)
  A filter that convolves an image with a subtractive Laplacian pyramid.
- [class MPSImagePyramid](mpsimagepyramid.md)
  A base class for creating different kinds of pyramid images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconvolution)*