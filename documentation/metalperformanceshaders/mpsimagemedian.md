# MPSImageMedian

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that applies a median filter in a square region centered around each pixel in the source image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageMedian
```

#### Overview

An [`MPSImageMedian`](mpsimagemedian.md) filter finds the median color value for each channel within a `kernelDiameter * kernelDiameter` window surrounding the pixel of interest.  It is a common means of noise reduction and also as a smoothing filter with edge preserving qualities.

> **Note**:  The [`MPSImageMedian`](mpsimagemedian.md) filter supports only images with 8 or less bits per channel.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagemedian/init(coder:device:).md)
### Methods
- [init(device: any MTLDevice, kernelDiameter: Int)](mpsimagemedian/init(device:kerneldiameter:).md)
  Initializes a filter for a particular kernel size and device.
- [class func maxKernelDiameter() -> Int](mpsimagemedian/maxkerneldiameter.md)
  Queries the maximum diameter, in pixels, of the filter window supported by the median filter.
- [class func minKernelDiameter() -> Int](mpsimagemedian/minkerneldiameter.md)
  Queries the minimum diameter, in pixels, of the filter window supported by the median filter.
### Properties
- [var kernelDiameter: Int](mpsimagemedian/kerneldiameter.md)
  The diameter, in pixels, of the filter window.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian)*