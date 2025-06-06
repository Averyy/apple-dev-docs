# Image Filters

**Framework**: Metal Performance Shaders

Apply high-performance filters to, and extract statistical and histogram data from images.

#### Overview

The [`MPSUnaryImageKernel`](mpsunaryimagekernel.md) and [`MPSBinaryImageKernel`](mpsbinaryimagekernel.md) base classes define several properties common to all image kernels:

| [`clipRect`](mpsunaryimagekernel/1618859-cliprect.md) and [`clipRect`](mpsbinaryimagekernel/1618879-cliprect.md) | A clip rectangle is available to all image kernels that write to a destination texture. It describes the sub-rectangle of the destination texture overwritten by the filter. If the clip rectangle is larger than the destination texture, then the intersection between the clip rectangle and the destination texture bounds is used instead. A clip rectangle may be used to avoid doing work to obscured regions of the destination image, or to manage tiling and limit operations to parts of an image—for example, if a user draws a rectangle on the screen and asks your app to just apply the filter there. |
| --- | --- |
| [`offset`](mpsunaryimagekernel/1618884-offset.md), [`primaryOffset`](mpsbinaryimagekernel/1618880-primaryoffset.md), and [`secondaryOffset`](mpsbinaryimagekernel/1618755-secondaryoffset.md) | An offset is available to all image kernels that use a source texture from which pixel data is read. It describes the positioning of the source image relative to the result texture. An offset of `{0, 0, 0}` indicates that the top left pixel of the source texture is the center pixel used to create the top left corner of the destination texture clip rectangle (as a further example, an offset of `{1, 2, 0}` positions the top left corner of the clip rectangle at position `x=1`, `y=2`, and `z=0` of the source image). The offset is the position of the top left corner of the clip rectangle in the source coordinate frame. It can be used for tiling and for translating an image up, down, left, or right by pixel increments. If there is no clip rectangle, then the offset is the top left corner of the region read by the filter. If there are multiple source textures, then the primary offset describes the top left corner of the region read in the primary source texture and the secondary offset describes the top left corner of the region read in the secondary source texture. |
| [`edgeMode`](mpsunaryimagekernel/1618812-edgemode.md), [`primaryEdgeMode`](mpsbinaryimagekernel/1618782-primaryedgemode.md), and [`secondaryEdgeMode`](mpsbinaryimagekernel/1618848-secondaryedgemode.md) | An edge mode describes the behavior of texture reads that stray off the edge of the source image. This can happen if the offset is negative, meaning a read off the top or left edge of the image. This can also happen if the sum of the clip rectangle size and the offset is larger than the source image, meaning a read off the bottom or right edge of the image. Furthermore, it is also possible for image filters to have a kernel window that stretches to examine neighboring pixels beyond the image bounds (such as convolution, morphology, and resampling filters). If there are multiple source textures, then the primary edge mode describes the mode to use with the primary source texture and the secondary edge mode  describes the mode to use with the secondary source texture. |

##### 1674362

Some kernels can operate in place. This means that the same texture is used to hold both the input image and the result image. Operating in place is a great way to save memory, time, and energy. You can perform an in-place operation by using the [`encode(commandBuffer:inPlaceTexture:fallbackCopyAllocator:)`](mpsunaryimagekernel/1618873-encode.md) method.

Unfortunately, it is not always possible for kernels to run in place. Whether a particular kernel can operate in place can vary according to the hardware it is running on, the OS version, and the parameters and properties passed to it. You may not assume that because a kernel works in place today on a particular device that it will do so in the future.

To simplify error handling with failed in-place operation, the [`encode(commandBuffer:inPlaceTexture:fallbackCopyAllocator:)`](mpsunaryimagekernel/1618873-encode.md) method takes an optional [`MPSCopyAllocator`](mpscopyallocator.md) object. It is used to create a new texture when in-place operation is not possible so as to allow the operation to proceed out of place in a reliable fashion instead. When this happens, the input texture is released and replaced with a new texture. To make use of the feature, you will need to write a copy allocator block.

[`Listing 1`](image_filters#1942958.md) shows a minimal copy allocator implementation. For more information, see the [`MPSCopyAllocator`](mpscopyallocator.md) reference.

```swift
let myAllocator: MPSCopyAllocator =
{
    (kernel: MPSKernel, buffer: MTLCommandBuffer, texture: MTLTexture) -> MTLTexture in
    
    let descriptor = MTLTextureDescriptor.texture2DDescriptor(pixelFormat: texture.pixelFormat,
                                                              width: texture.width,
                                                              height: texture.height,
                                                              mipmapped: false)
    
    return buffer.device.makeTexture(descriptor: descriptor)
}
```

##### 2793234

All Metal Performance Shaders image kernels support source and destination textures with the following ordinary and packed pixel formats:  

Some compressed pixel formats can be used as source textures. They cannot be used as destination textures because they cannot be written to. Metal Performance Shaders image kernels support the following compression families:

- PVRTC 
- EAC/ETC
- ASTC

The following Metal Performance Shaders image kernels also support source and destination textures with ordinary signed and unsigned integer pixel formats:

- [`MPSImageTranspose`](mpsimagetranspose.md)
- [`MPSImageIntegral`](mpsimageintegral.md)
- [`MPSImageIntegralOfSquares`](mpsimageintegralofsquares.md)

The ordinary signed and unsigned integer pixel formats supported by these image kernels:

For more information on pixel formats, see [`MTLPixelFormat`](https://developer.apple.com/documentation/metal/mtlpixelformat) and [`Pixel Format Capabilities`](https://developer.apple.comhttps://developer.apple.com/metal/capabilities/).

##### 1674370

```occ
// Blur the input texture (in place if possible) on MTLCommandQueue q, and return the new texture.
// This is a trivial example. It is not necessary or necessarily advised to enqueue a MPSKernel on
// its own MTLCommandBuffer or using its own MTLComputeCommandEncoder. Group work together.
    
// Here we assume that you have already gotten a MTLDevice using MTLCreateSystemDefaultDevice() or
// MTLCopyAllDevices(), used it to create a MTLCommandQueue with MTLDevice.newCommandQueue, and
// similarly made textures with the device as needed.
func myBlurTextureInPlace(inTexture: MTLTexture, blurRadius: Float, queue: MTLCommandQueue)
{
    // Create the usual Metal objects.
    // MPS does not need a dedicated MTLCommandBuffer or MTLComputeCommandEncoder.
    // This is a trivial example. You should reuse the MTL objects you already have, if you have them.
    let device = queue.device;
    let buffer = queue.makeCommandBuffer();
    
    // Create a MPS filter.
    let blur = MPSImageGaussianBlur(device: device, sigma: blurRadius)
    
    // Defaults are okay here for other MPSKernel properties (clipRect, origin, edgeMode).
    
    // Attempt to do the work in place.  Since we provided a copyAllocator as an out-of-place
    // fallback, we don’t need to check to see if it succeeded or not.
    // See the "Minimal MPSCopyAllocator Implementation" code listing for a sample myAllocator.
    let inPlaceTexture = UnsafeMutablePointer<MTLTexture>.allocate(capacity: 1)
    inPlaceTexture.initialize(to: inTexture)
    
    blur.encode(commandBuffer: buffer, 
                inPlaceTexture: inPlaceTexture, 
                fallbackCopyAllocator: myAllocator)
    
    // The usual Metal enqueue process.
    buffer.commit()
    buffer.waitUntilCompleted()
}
```

## Topics

### Morphological Image Filters
- [class MPSImageAreaMax](mpsimageareamax.md)
  A filter that finds the maximum pixel value in a rectangular region centered around each pixel in the source image. 
- [class MPSImageDilate](mpsimagedilate.md)
  A filter that finds the maximum pixel value in a rectangular region by applying a dilation function. 
- [class MPSImageAreaMin](mpsimageareamin.md)
  A filter that finds the minimum pixel value in a rectangular region centered around each pixel in the source image. 
- [class MPSImageErode](mpsimageerode.md)
  A filter that finds the minimum pixel value in a rectangular region by applying an erosion function.
### Convolution Image Filters
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
- [class MPSImagePyramid](mpsimagepyramid.md)
  A base class for creating different kinds of pyramid images.
### Histogram Image Filters
- [class MPSImageHistogram](mpsimagehistogram.md)
  A filter that computes the histogram of an image.
- [class MPSImageHistogramEqualization](mpsimagehistogramequalization.md)
  A filter that equalizes the histogram of an image.
- [class MPSImageHistogramSpecification](mpsimagehistogramspecification.md)
  A filter that performs a histogram specification operation on an image. 
### Image Threshold Filters
- [class MPSImageThresholdBinary](mpsimagethresholdbinary.md)
  A filter that returns a specified value for each pixel with a value greater than a specified threshold or 0 otherwise. 
- [class MPSImageThresholdBinaryInverse](mpsimagethresholdbinaryinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or a specified value otherwise. 
- [class MPSImageThresholdToZero](mpsimagethresholdtozero.md)
  A filter that returns the original value for each pixel with a value greater than a specified threshold or 0 otherwise. 
- [class MPSImageThresholdToZeroInverse](mpsimagethresholdtozeroinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or the original value otherwise. 
- [class MPSImageThresholdTruncate](mpsimagethresholdtruncate.md)
  A filter that clamps the return value to an upper specified value.
### Image Integral Filters
- [class MPSImageIntegral](mpsimageintegral.md)
  A filter that calculates the sum of pixels over a specified region in an image.
- [class MPSImageIntegralOfSquares](mpsimageintegralofsquares.md)
  A filter that calculates the sum of squared pixels over a specified region in an image.
### Image Manipulation Filters
- [class MPSImageConversion](mpsimageconversion.md)
  A filter that performs a conversion of color space, alpha, or pixel format.
- [class MPSImageScale](mpsimagescale.md)
  A filter that resizes and changes the aspect ratio of an image.
- [class MPSImageLanczosScale](mpsimagelanczosscale.md)
  A filter that resizes and changes the aspect ratio of an image using Lanczos resampling. 
- [class MPSImageBilinearScale](mpsimagebilinearscale.md)
  A filter that resizes and changes the aspect ratio of an image using Bilinear resampling.
- [class MPSImageTranspose](mpsimagetranspose.md)
  A filter that transposes an image.
### Image Statistics Filters
- [class MPSImageStatisticsMean](mpsimagestatisticsmean.md)
  A kernel that computes the mean for a given region of an image.
- [class MPSImageStatisticsMeanAndVariance](mpsimagestatisticsmeanandvariance.md)
  A kernel that computes the mean and variance for a given region of an image.
- [class MPSImageStatisticsMinAndMax](mpsimagestatisticsminandmax.md)
  A kernel that computes the minimum and maximum pixel values for a given region of an image.
### Image Reduction Filters
- [class MPSImageReduceRowMax](mpsimagereducerowmax.md)
  A filter that returns the maximum value for each row in an image.
- [class MPSImageReduceRowMin](mpsimagereducerowmin.md)
  A filter that returns the minimum value for each row in an image.
- [class MPSImageReduceRowSum](mpsimagereducerowsum.md)
  A filter that returns the sum of all values for a row in an image.
- [class MPSImageReduceRowMean](mpsimagereducerowmean.md)
  A filter that returns the mean value for each row in an image.
- [class MPSImageReduceColumnMax](mpsimagereducecolumnmax.md)
  A filter that returns the maximum value for each column in an image.
- [class MPSImageReduceColumnMin](mpsimagereducecolumnmin.md)
  A filter that returns the minimum value for each column in an image.
- [class MPSImageReduceColumnSum](mpsimagereducecolumnsum.md)
  A filter that returns the sum of all values for a column in an image.
- [class MPSImageReduceColumnMean](mpsimagereducecolumnmean.md)
  A filter that returns the mean value for each column in an image.
- [class MPSImageReduceUnary](mpsimagereduceunary.md)
  The base class for reduction filters that take a single source as input.
### Image Arithmetic Filters
- [class MPSImageAdd](mpsimageadd.md)
  A filter that returns the element-wise sum of its two input images.
- [class MPSImageSubtract](mpsimagesubtract.md)
  A filter that returns the element-wise difference of its two input images.
- [class MPSImageMultiply](mpsimagemultiply.md)
  A filter that returns the element-wise product of its two input images.
- [class MPSImageDivide](mpsimagedivide.md)
  A filter that returns the element-wise quotient of its two input images.
- [class MPSImageArithmetic](mpsimagearithmetic.md)
  Base class for basic arithmetic nodes
### Euclidean Distance Transform Filter
- [class MPSImageEuclideanDistanceTransform](mpsimageeuclideandistancetransform.md)
  A filter that performs a Euclidean distance transform on an image.
### Fast Guided Filter
- [class MPSImageGuidedFilter](mpsimageguidedfilter.md)
  A filter that performs edge-aware filtering on an image.
### Keypoints
- [class MPSImageFindKeypoints](mpsimagefindkeypoints.md)
  A kernel that is used to find a list of keypoints.
- [struct MPSImageKeypointData](mpsimagekeypointdata.md)
  A structure that specifies keypoint information.
- [struct MPSImageKeypointRangeInfo](mpsimagekeypointrangeinfo.md)
  A structure that specifies information to find the keypoints in an image.
### Image Filter Base Classes
- [class MPSUnaryImageKernel](mpsunaryimagekernel.md)
  A kernel that consumes one texture and produces one texture.
- [class MPSBinaryImageKernel](mpsbinaryimagekernel.md)
  A kernel that consumes two textures and produces one texture.
### Constants
- [MPSRectNoClip](image_filters/mpsrectnoclip.md)
  The default clipping rectangle for a kernel object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/image_filters)*