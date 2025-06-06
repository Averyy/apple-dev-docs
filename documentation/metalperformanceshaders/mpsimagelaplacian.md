# MPSImageLaplacian

**Framework**: Metalperformanceshaders  
**Kind**: cl

An optimized Laplacian filter, provided for ease of use.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageLaplacian : MPSUnaryImageKernel
```

#### Overview

This filter uses an optimized convolution filter with a 3x3 kernel with the following weights:

![](https://docs-assets.developer.apple.com/published/14b057e164/7ed47c4c-c5fa-4b07-b639-47dbf5e55da5.png)

> **Note**: The optimized convolution filter used by the [`MPSImageLaplacian`](mpsimagelaplacian.md) class could also be created by initializing an [`MPSImageConvolution`](mpsimageconvolution.md) object with `kernelWidth=3`, `kernelHeight=3`, and the weights specified above.

## Topics

### Properties
- [var bias: Float](mpsimagelaplacian/1648929-bias.md)
  The value added to a convolved pixel before it is converted back to its intended storage format.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)

## See Also

- [class MPSImageConvolution](mpsimageconvolution.md)
  A filter that convolves an image with a given kernel of odd width and height.
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
- [class MPSImageLaplacianPyramid](mpsimagelaplacianpyramid.md)
  A filter that convolves an image with a Laplacian filter.
- [class MPSImageLaplacianPyramidAdd](mpsimagelaplacianpyramidadd.md)
  A filter that convolves an image with an additive Laplacian pyramid.
- [class MPSImageLaplacianPyramidSubtract](mpsimagelaplacianpyramidsubtract.md)
  A filter that convolves an image with a subtractive Laplacian pyramid.
- [class MPSImagePyramid](mpsimagepyramid.md)
  A base class for creating different kinds of pyramid images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagelaplacian)*