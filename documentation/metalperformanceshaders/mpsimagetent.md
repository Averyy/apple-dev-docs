# MPSImageTent

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that convolves an image with a tent filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageTent
```

#### Overview

The kernel elements of the filter form a tent shape with increasing sides, for example:

![None](https://docs-assets.developer.apple.com/published/bd0e20af4a43a00dcc34a4da5e09ddfe/media-2556918%402x.png)

Like a box filter, this arrangement allows for much faster algorithms, especially for larger blur radii but with a more pleasing appearance.

The tent blur is a separable filter and the Metal Performance Shaders framework will act accordingly to give the best performance for multi-dimensional blurs.

> **Note**:  The box filter, while fast, may yield square-ish looking blur effects. However, multiple passes of the box filter tend to smooth out with each additional pass. For example, two 3-wide box blurs produces the same effective convolution as a 5-wide tent blur. In effect, addition passes tend to approximate a Gaussian line shape.

## Relationships

### Inherits From
- [MPSImageBox](mpsimagebox.md)
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

- [class MPSImageConvolution](mpsimageconvolution.md)
  A filter that convolves an image with a given kernel of odd width and height.
- [class MPSImageMedian](mpsimagemedian.md)
  A filter that applies a median filter in a square region centered around each pixel in the source image.
- [class MPSImageBox](mpsimagebox.md)
  A filter that convolves an image with a given kernel of odd width and height.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetent)*