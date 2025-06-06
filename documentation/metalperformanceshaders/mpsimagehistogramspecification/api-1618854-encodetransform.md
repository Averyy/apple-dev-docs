# encodeTransform(to:sourceTexture:sourceHistogram:sourceHistogramOffset:desiredHistogram:desiredHistogramOffset:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

Encodes the transform function to a command buffer using a compute command encoder. The transform function computes the equalization lookup table.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encodeTransform(to commandBuffer: any MTLCommandBuffer, sourceTexture source: any MTLTexture, sourceHistogram: any MTLBuffer, sourceHistogramOffset: Int, desiredHistogram: any MTLBuffer, desiredHistogramOffset: Int)
```

#### Discussion

The transform function will not begin to execute until after the command buffer has been enqueued and committed. This step will need to be repeated with the new [`MPSKernel`](mpskernel.md) object if the [`copy(with:device:)`](mpskernel/1618912-copy.md) or [`copy(with:)`](https://developer.apple.com/documentation/foundation/nscopying/copy(with:)) method is called.

## Parameters

- `commandBuffer`: A valid command buffer.
- `source`: A valid texture containing the source image for the filter.
- `sourceHistogram`: A valid buffer containing the histogram results for the source image. This filter will use these histogram results to generate the cumulative histogram for equalizing the image.  The histogram results per channel are stored together. The number of channels for which histogram results are stored is determined by the number of channels in the image. If the   value of the   property is   and the source image is RGBA, then only histogram results for RGB channels are stored.
- `sourceHistogramOffset`: The byte offset into the source histogram buffer where the histogram starts. Must conform to alignment requirements for the   parameter of the   method.
- `desiredHistogram`: A valid buffer containing the desired histogram results for the source image. The histogram results per channel are stored together. The number of channels for which histogram results are stored is determined by the number of channels in the image. If the   value of the   property is   and the source image is RGBA, then only histogram results for RGB channels are stored.
- `desiredHistogramOffset`: The byte offset into the desired histogram buffer where the histogram starts. Must conform to alignment requirements for the   parameter of the   method.

## See Also

- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagehistogramspecification/1618907-init.md)
  Initializes a histogram with specific information.
- [func setBufferOffset(Int, index: Int)](../metal/mtlcomputecommandencoder/setbufferoffset(_:index:).md)
  Changes where the data begins in a buffer already bound to the buffer argument table.
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](../metal/mtlcomputecommandencoder/setbuffer(_:offset:index:).md)
  Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramspecification/1618854-encodetransform)*