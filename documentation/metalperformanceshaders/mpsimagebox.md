# MPSImageBox

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
class MPSImageBox : MPSUnaryImageKernel
```

#### Overview

The kernel elements all have equal weight, achieving a blur effect (each result is the unweighted average of the surrounding pixels). This allows for much faster algorithms, especially for larger blur radii. The box height and width must be odd numbers.

The box blur is a separable filter and the Metal Performance Shaders framework will act accordingly to give best performance for multi-dimensional blurs.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagebox/2866153-init.md)
### Methods
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)](mpsimagebox/1618789-init.md)
  Initializes a box filter.
### Properties
- [var kernelHeight: Int](mpsimagebox/1618739-kernelheight.md)
  The height of the filter window. Must be an odd number.
- [var kernelWidth: Int](mpsimagebox/1618834-kernelwidth.md)
  The width of the filter window. Must be an odd number.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)

## See Also

- [class MPSImageConvolution](mpsimageconvolution.md)
  A filter that convolves an image with a given kernel of odd width and height.
- [class MPSImageMedian](mpsimagemedian.md)
  A filter that applies a median filter in a square region centered around each pixel in the source image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagebox)*