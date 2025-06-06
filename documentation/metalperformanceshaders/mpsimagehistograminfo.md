# MPSImageHistogramInfo

**Framework**: Metal Performance Shaders  
**Kind**: struct

The information used to compute the histogram channels of an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MPSImageHistogramInfo
```

## Topics

### Initializers
- [init()](mpsimagehistograminfo/1618769-init.md)
- [init(numberOfHistogramEntries: Int, histogramForAlpha: ObjCBool, minPixelValue: vector_float4, maxPixelValue: vector_float4)](mpsimagehistograminfo/1618832-init.md)
### Instance Properties
- [var histogramForAlpha: ObjCBool](mpsimagehistograminfo/1618840-histogramforalpha.md)
  Specifies whether the histogram for the alpha channel should be computed or not.
- [var maxPixelValue: vector_float4](mpsimagehistograminfo/1618847-maxpixelvalue.md)
  Specifies the maximum pixel value.  Any pixel value greater than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This maximum value is applied to each of the four channels separately.
- [var minPixelValue: vector_float4](mpsimagehistograminfo/1618749-minpixelvalue.md)
  Specifies the minimum pixel value. Any pixel value less than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This minimum value is applied to each of the four channels separately.
- [var numberOfHistogramEntries: Int](mpsimagehistograminfo/1618805-numberofhistogramentries.md)
  Specifies the number of histogram entries () for each channel.

## See Also

- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagehistogram/1618910-init.md)
  Initializes a histogram with specific information.
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](mpsimagehistogram/1618853-encode.md)
  Encodes the filter to a command buffer using a compute command encoder.
- [func histogramSize(forSourceFormat: MTLPixelFormat) -> Int](mpsimagehistogram/1618839-histogramsize.md)
  The amount of space the histogram will take up in the output buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistograminfo)*