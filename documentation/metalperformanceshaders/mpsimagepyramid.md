# MPSImagePyramid

**Framework**: Metal Performance Shaders  
**Kind**: class

A base class for creating different kinds of pyramid images.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImagePyramid
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagepyramid/init(coder:device:).md)
### Methods
- [convenience init(device: any MTLDevice)](mpsimagepyramid/init(device:).md)
  Initializes a downwards 5-tap image pyramid with the default filter kernel and device.
- [convenience init(device: any MTLDevice, centerWeight: Float)](mpsimagepyramid/init(device:centerweight:).md)
  Initialize a downwards 5-tap image pyramid with a central weight parameter and device.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, weights: UnsafePointer<Float>)](mpsimagepyramid/init(device:kernelwidth:kernelheight:weights:).md)
  Initialize a downwards n-tap image pyramid with a custom filter kernel and device.
### Properties
- [var kernelWidth: Int](mpsimagepyramid/kernelwidth.md)
  The width of the filter window. Must be an odd number.
- [var kernelHeight: Int](mpsimagepyramid/kernelheight.md)
  The height of the filter window. Must be an odd number.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)
### Inherited By
- [MPSImageGaussianPyramid](mpsimagegaussianpyramid.md)
- [MPSImageLaplacianPyramid](mpsimagelaplacianpyramid.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid)*