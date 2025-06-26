# MPSImageFeatureChannelFormat

**Framework**: Metal Performance Shaders  
**Kind**: enum

Encodes the representation of a single channel within an image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MPSImageFeatureChannelFormat
```

#### Overview

A pixel in an [`MPSImage`](mpsimage.md) object may have many channels in it, sometimes many more than 4, that exceed the limit of what a [`MTLPixelFormat`](https://developer.apple.com/documentation/Metal/MTLPixelFormat) value can encode. The storage format for a single channel within a pixel can be given by the [`MPSImageFeatureChannelFormat`](mpsimagefeaturechannelformat.md) type. The number of channels is defined by the [`featureChannels`](mpsimage/featurechannels.md) property of an [`MPSImage`](mpsimage.md) object. The size of the pixel is the size of the channel format multiplied by the number of feature channels. No padding is allowed, except to round out to a full byte.

## Topics

### Constants
- [MPSImageFeatureChannelFormat.none](mpsimagefeaturechannelformat/none.md)
- [MPSImageFeatureChannelFormat.unorm8](mpsimagefeaturechannelformat/unorm8.md)
  `uint8_t` type with value `[0,255]` and encoding `[0,1.0]`.
- [MPSImageFeatureChannelFormat.unorm16](mpsimagefeaturechannelformat/unorm16.md)
  `uint16_t` type with value `[0,65535]` and encoding `[0,1.0]`.
- [MPSImageFeatureChannelFormat.float16](mpsimagefeaturechannelformat/float16.md)
  IEEE-754 16-bit floating-point type (half precision). Representable normal range is `+-[2^-14, 65504], 0, INF, NaN`. 11 bits of precision + exponent.
- [MPSImageFeatureChannelFormat.float32](mpsimagefeaturechannelformat/float32.md)
  IEEE-754 32-bit floating-point type (single precision, standard `float` type in C). 24 bits of precision + exponent.
### Enumeration Cases
- [MPSImageFeatureChannelFormat.count](mpsimagefeaturechannelformat/count.md)
### Initializers
- [init?(rawValue: UInt)](mpsimagefeaturechannelformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var exportFromGraph: Bool](mpsnnimagenode/exportfromgraph.md)
- [var format: MPSImageFeatureChannelFormat](mpsnnimagenode/format.md)
- [var handle: (any MPSHandle)?](mpsnnimagenode/handle.md)
- [var imageAllocator: any MPSImageAllocator](mpsnnimagenode/imageallocator.md)
- [var stopGradient: Bool](mpsnnimagenode/stopgradient.md)
- [var synchronizeResource: Bool](mpsnnimagenode/synchronizeresource.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat)*