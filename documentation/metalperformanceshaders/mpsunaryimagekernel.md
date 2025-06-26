# MPSUnaryImageKernel

**Framework**: Metal Performance Shaders  
**Kind**: class

A kernel that consumes one texture and produces one texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSUnaryImageKernel
```

## Mentions

- [The MPSKernel Class](the-mpskernel-class.md)

#### Overview

[`MPSUnaryImageKernel`](mpsunaryimagekernel.md) defines shared behavior for most image processing kernels (filters) such as edging modes, clipping, and tiling support for image operations that consumes a single source textures. It is not meant to be used directly, but provides API abstraction and in some cases may allow some level of polymorphic manipulation of image kernel objects.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsunaryimagekernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsunaryimagekernel/init(device:).md)
### Methods
- [func encode(commandBuffer: any MTLCommandBuffer, inPlaceTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsunaryimagekernel/encode(commandbuffer:inplacetexture:fallbackcopyallocator:).md)
  This method attempts to apply a kernel in place on a texture.
- [typealias MPSCopyAllocator](mpscopyallocator.md)
  A block to make a copy of a source texture for filters that can only execute out of place.
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](mpsunaryimagekernel/encode(commandbuffer:sourceimage:destinationimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsunaryimagekernel/encode(commandbuffer:sourcetexture:destinationtexture:).md)
  Encodes a kernel into a command buffer, out of place.
- [func sourceRegion(destinationSize: MTLSize) -> MPSRegion](mpsunaryimagekernel/sourceregion(destinationsize:).md)
  Determines the region of the source texture that will be read for an encode operation.
### Properties
- [var offset: MPSOffset](mpsunaryimagekernel/offset.md)
  The position of the destination clip rectangle origin relative to the source buffer.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpsunaryimagekernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.
- [struct MPSRegion](mpsregion.md)
  A region of an image.
- [var edgeMode: MPSImageEdgeMode](mpsunaryimagekernel/edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSImageAreaMax](mpsimageareamax.md)
- [MPSImageBox](mpsimagebox.md)
- [MPSImageCanny](mpsimagecanny.md)
- [MPSImageConversion](mpsimageconversion.md)
- [MPSImageConvolution](mpsimageconvolution.md)
- [MPSImageDilate](mpsimagedilate.md)
- [MPSImageEuclideanDistanceTransform](mpsimageeuclideandistancetransform.md)
- [MPSImageGaussianBlur](mpsimagegaussianblur.md)
- [MPSImageHistogramEqualization](mpsimagehistogramequalization.md)
- [MPSImageHistogramSpecification](mpsimagehistogramspecification.md)
- [MPSImageIntegral](mpsimageintegral.md)
- [MPSImageIntegralOfSquares](mpsimageintegralofsquares.md)
- [MPSImageLaplacian](mpsimagelaplacian.md)
- [MPSImageMedian](mpsimagemedian.md)
- [MPSImagePyramid](mpsimagepyramid.md)
- [MPSImageReduceUnary](mpsimagereduceunary.md)
- [MPSImageScale](mpsimagescale.md)
- [MPSImageSobel](mpsimagesobel.md)
- [MPSImageStatisticsMean](mpsimagestatisticsmean.md)
- [MPSImageStatisticsMeanAndVariance](mpsimagestatisticsmeanandvariance.md)
- [MPSImageStatisticsMinAndMax](mpsimagestatisticsminandmax.md)
- [MPSImageThresholdBinary](mpsimagethresholdbinary.md)
- [MPSImageThresholdBinaryInverse](mpsimagethresholdbinaryinverse.md)
- [MPSImageThresholdToZero](mpsimagethresholdtozero.md)
- [MPSImageThresholdToZeroInverse](mpsimagethresholdtozeroinverse.md)
- [MPSImageThresholdTruncate](mpsimagethresholdtruncate.md)
- [MPSImageTranspose](mpsimagetranspose.md)
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

- [class MPSBinaryImageKernel](mpsbinaryimagekernel.md)
  A kernel that consumes two textures and produces one texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel)*