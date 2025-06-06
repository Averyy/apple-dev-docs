# MPSImageGaussianBlur

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that convolves an image with a Gaussian blur of a given sigma in both the x and y directions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageGaussianBlur : MPSUnaryImageKernel
```

#### Overview

> **Note**: The Gaussian blur utilizes a very fast algorithm that typically runs at approximately half the speed of copy speeds. Notably, it is faster than either the tent or box blur except perhaps for very large filter windows. Mathematically, it is an approximate Gaussian. Some non-Gaussian behavior may be detectable with advanced analytical methods such as FFT. If an analytically clean Gaussian filter is required, use the [`MPSImageConvolution`](mpsimageconvolution.md) filter instead with an appropriate set of weights. The [`MPSImageGaussianBlur`](mpsimagegaussianblur.md) filter is intended to be suitable for all common image processing needs demanding ~10 bits of precision or less.

The Gaussian blur utilizes a very fast algorithm that typically runs at approximately half the speed of copy speeds. Notably, it is faster than either the tent or box blur except perhaps for very large filter windows. Mathematically, it is an approximate Gaussian. Some non-Gaussian behavior may be detectable with advanced analytical methods such as FFT.

If an analytically clean Gaussian filter is required, use the [`MPSImageConvolution`](mpsimageconvolution.md) filter instead with an appropriate set of weights. The [`MPSImageGaussianBlur`](mpsimagegaussianblur.md) filter is intended to be suitable for all common image processing needs demanding ~10 bits of precision or less.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagegaussianblur/2866150-init.md)
### Methods
- [init(device: any MTLDevice, sigma: Float)](mpsimagegaussianblur/1618813-init.md)
  Initializes a Gaussian blur filter.
### Properties
- [var sigma: Float](mpsimagegaussianblur/1618850-sigma.md)
  The sigma value with which the filter was created.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagegaussianblur)*