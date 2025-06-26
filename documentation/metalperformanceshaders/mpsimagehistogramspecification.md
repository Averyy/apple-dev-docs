# MPSImageHistogramSpecification

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that performs a histogram specification operation on an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageHistogramSpecification
```

#### Overview

[`MPSImageHistogramSpecification`](mpsimagehistogramspecification.md) is a generalized version of histogram equalization operation. The histogram specification filter converts the image so that its histogram matches the desired histogram.

The process is divided into three steps:

1. Call the [`init(device:histogramInfo:)`](mpsimagehistogramspecification/init(device:histograminfo:).md) method to create a [`MPSImageHistogramSpecification`](mpsimagehistogramspecification.md) object.
2. Call the [`encodeTransform(to:sourceTexture:sourceHistogram:sourceHistogramOffset:desiredHistogram:desiredHistogramOffset:)`](mpsimagehistogramspecification/encodetransform(to:sourcetexture:sourcehistogram:sourcehistogramoffset:desiredhistogram:desiredhistogramoffset:).md) method. This creates a privately held image transform which will convert the distribution of the source histogram to the desired histogram. This process runs on a command buffer when it is committed to a command queue. It must complete before the next step can be run. It may be performed on the same command buffer. The `sourceTexture` argument is used by the method to determine the number of channels and therefore which histogram data in the source histogram buffer to use. The source histogram and desired histogram must have been computed either on the CPU or using the [`MPSImageHistogram`](mpsimagehistogram.md) kernel.
3. Call the [`encode(commandBuffer:sourceTexture:destinationTexture:)`](mpsunaryimagekernel/encode(commandbuffer:sourcetexture:destinationtexture:).md) method to read data from the source texture, apply the equalization transform to it, and write to the destination texture. This step is also done on the GPU on a command queue.

> **Note**:  You can reuse the same specification transform on other images to perform the same transform on those images. (Since their distribution is probably different, they will probably not arrive at the same distribution as the desired histogram.) This filter usually will not be able to work in place.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagehistogramspecification/init(coder:device:).md)
### Methods
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagehistogramspecification/init(device:histograminfo:).md)
  Initializes a histogram with specific information.
- [func encodeTransform(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, sourceHistogram: any MTLBuffer, sourceHistogramOffset: Int, desiredHistogram: any MTLBuffer, desiredHistogramOffset: Int)](mpsimagehistogramspecification/encodetransform(to:sourcetexture:sourcehistogram:sourcehistogramoffset:desiredhistogram:desiredhistogramoffset:).md)
  Encodes the transform function to a command buffer using a compute command encoder. The transform function computes the equalization lookup table.
### Properties
- [var histogramInfo: MPSImageHistogramInfo](mpsimagehistogramspecification/histograminfo.md)
  A structure describing the histogram content.

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

- [Metal Image Filters: Using the image filters provided by the Metal Performance Shaders framework.](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/MetalImageFilters/Introduction/Intro.html#//apple_ref/doc/uid/TP40017535)
- [class MPSImageHistogram](mpsimagehistogram.md)
  A filter that computes the histogram of an image.
- [class MPSImageHistogramEqualization](mpsimagehistogramequalization.md)
  A filter that equalizes the histogram of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramspecification)*