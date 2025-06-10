# MPSImageHistogramEqualization

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that equalizes the histogram of an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageHistogramEqualization : MPSUnaryImageKernel
```

#### Overview

The process is divided into three steps:

1. Call the [`init(device:histogramInfo:)`](mpsimagehistogramequalization/1618856-init.md) method to create a [`MPSImageHistogramEqualization`](mpsimagehistogramequalization.md) object.
2. Call the [`encodeTransform(to:sourceTexture:histogram:histogramOffset:)`](mpsimagehistogramequalization/1618746-encodetransform.md) method. This creates a privately held image transform (i.e. a cumulative distribution function of the histogram) which will be used to equalize the distribution of the histogram of the source image. This process runs on a command buffer when it is committed to a command queue. It must complete before the next step can be run. It may be performed on the same command buffer. The `histogram` argument specifies the histogram buffer which contains the histogram values for the source texture. The `sourceTexture` argument is used by the method to determine the number of channels and therefore which histogram data in the histogram buffer to use. The histogram for the source texture must have been computed either on the CPU or using the [`MPSImageHistogram`](mpsimagehistogram.md) kernel.
3. Call the [`encode(commandBuffer:sourceTexture:destinationTexture:)`](mpsunaryimagekernel/1618741-encode.md) method to read data from the source texture, apply the equalization transform to it, and write to the destination texture. This step is also done on the GPU on a command queue.

> **Note**: You can reuse the same equalization transform on other images to perform the same transform on those images. (Since their distribution is probably different, they will probably not be equalized by it.) This filter usually will not be able to work in place.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagehistogramequalization/2866993-init.md)
### Methods
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagehistogramequalization/1618856-init.md)
  Initializes a histogram with specific information.
- [func encodeTransform(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](mpsimagehistogramequalization/1618746-encodetransform.md)
  Encodes the transform function to a command buffer using a compute command encoder. The transform function computes the equalization lookup table.
### Properties
- [var histogramInfo: MPSImageHistogramInfo](mpsimagehistogramequalization/1618775-histograminfo.md)
  A structure describing the histogram content.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)

## See Also

- [class MPSImageHistogram](mpsimagehistogram.md)
  A filter that computes the histogram of an image.
- [class MPSImageHistogramSpecification](mpsimagehistogramspecification.md)
  A filter that performs a histogram specification operation on an image. 
- [Metal Image Filters: Using the image filters provided by the Metal Performance Shaders framework.](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/MetalImageFilters/Introduction/Intro.html#//apple_ref/doc/uid/TP40017535)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramequalization)*