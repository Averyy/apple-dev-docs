# MPSImageGaussianPyramid

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that convolves an image with a Gaussian pyramid.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageGaussianPyramid : MPSImagePyramid
```

#### Overview

The Gaussian image pyramid kernel is enqueued as an in-place operation using the [`encode(commandBuffer:inPlaceTexture:fallbackCopyAllocator:)`](mpsunaryimagekernel/1618873-encode.md) method. All mip-map levels (after level 1) present in the provided image are filled using the provided filter kernel. The `fallbackCopyAllocator` parameter is not used. The Gaussian image pyramid kernel ignores the [`clipRect`](mpsunaryimagekernel/1618859-cliprect.md) and [`offset`](mpsunaryimagekernel/1618884-offset.md) properties, and fills the entirety of the mip-map levels. Recall the size of the nth mip-map level as:

- `w_n = max(1, floor(w_0 / 2^n))`
- `h_n = max(1, floor(h_0 / 2^n))`

Where `w_0` and `h_0` are the width and height of the 0th level, respectively (i.e. the image dimensions themselves).

The Gaussian image pyramid is constructed as follows:

- First, the 0th level mip-map of the input image is filtered with the specified convolution kernel. The default convolution filter kernel is `k = ww^T`, where `w = [1/16, 1/4, 3/8, 1/4,  1/16 ]^T`. You may also modify this kernel with a `centerWeight` parameter of `a` resulting in `k = ww^T`, where `w = [(1/4 - a/2), 1/4, a, 1/4, (1/4 - a/2) ]^T`, or you may provide a completely custom kernel.
- Afterwards, the image is down-sampled by removing all odd rows and columns, which defines the next level in the Gaussian image pyramid.
- This procedure is continued until every mip-map level present in the image is filled with all the pyramid levels.

> **Note**: Make sure your chosen texture type is compatible with mip-mapping and also supports texture views (i.e. the texture’s usage includes the [`pixelFormatView`](https://developer.apple.com/documentation/metal/mtltextureusage/pixelformatview) option).

## Relationships

### Inherits From
- [MPSImagePyramid](mpsimagepyramid.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagegaussianpyramid)*