# MPSImageHistogram

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that computes the histogram of an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageHistogram
```

#### Overview

Typically, you use an [`MPSImageHistogram`](mpsimagehistogram.md) filter to calculate an image’s histogram that is passed to a subsequent filter such as [`MPSImageHistogramEqualization`](mpsimagehistogramequalization.md) or [`MPSImageHistogramSpecification`](mpsimagehistogramspecification.md).

The following listing shows how you can create a histogram filter to calculate the histogram of the [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture), `sourceTexture`. The filter is passed an instance of [`MPSImageHistogramInfo`](mpsimagehistograminfo.md) that specifies information to compute the histogram for the channels of an image. After encoding, `histogramInfoBuffer` contains the histogram information and can be used for further operations such as equalization or specification.

Listing 1. Creating a histogram filter

```swift
var histogramInfo = MPSImageHistogramInfo(
    numberOfHistogramEntries: 256,
    histogramForAlpha: false,
    minPixelValue: vector_float4(0,0,0,0),
    maxPixelValue: vector_float4(1,1,1,1))
     
let calculation = MPSImageHistogram(device: device,
                                    histogramInfo: &histogramInfo)
let bufferLength = calculation.histogramSize(forSourceFormat: sourceTexture.pixelFormat)
let histogramInfoBuffer = device.makeBuffer(length: bufferLength, 
                                            options: [.storageModePrivate])
     
calculation.encode(to: commandBuffer,
                   sourceTexture: sourceTexture,
                   histogram: histogramInfoBuffer,
                   histogramOffset: 0)
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagehistogram/init(coder:device:).md)
### Methods
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagehistogram/init(device:histograminfo:).md)
  Initializes a histogram with specific information.
- [struct MPSImageHistogramInfo](mpsimagehistograminfo.md)
  The information used to compute the histogram channels of an image.
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](mpsimagehistogram/encode(to:sourcetexture:histogram:histogramoffset:).md)
  Encodes the filter to a command buffer using a compute command encoder.
- [func histogramSize(forSourceFormat: MTLPixelFormat) -> Int](mpsimagehistogram/histogramsize(forsourceformat:).md)
  The amount of space the histogram will take up in the output buffer.
### Properties
- [var clipRectSource: MTLRegion](mpsimagehistogram/cliprectsource.md)
  The source rectangle to use when reading data.
- [var zeroHistogram: Bool](mpsimagehistogram/zerohistogram.md)
  Determines whether to zero-initialize the histogram results.
- [var histogramInfo: MPSImageHistogramInfo](mpsimagehistogram/histograminfo.md)
  A structure describing the histogram content.
- [var minPixelThresholdValue: vector_float4](mpsimagehistogram/minpixelthresholdvalue.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
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

- [class MPSImageHistogramEqualization](mpsimagehistogramequalization.md)
  A filter that equalizes the histogram of an image.
- [class MPSImageHistogramSpecification](mpsimagehistogramspecification.md)
  A filter that performs a histogram specification operation on an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram)*