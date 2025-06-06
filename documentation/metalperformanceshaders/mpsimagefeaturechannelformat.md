# MPSImageFeatureChannelFormat

**Framework**: Metal Performance Shaders  
**Kind**: enum

Encodes the representation of a single channel within an image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSImageFeatureChannelFormat : UInt, @unchecked Sendable
```

#### Overview

A pixel in an [`MPSImage`](mpsimage.md) object may have many channels in it, sometimes many more than 4, that exceed the limit of what a [`MTLPixelFormat`](https://developer.apple.com/documentation/metal/mtlpixelformat) value can encode. The storage format for a single channel within a pixel can be given by the [`MPSImageFeatureChannelFormat`](mpsimagefeaturechannelformat.md) type. The number of channels is defined by the [`featureChannels`](mpsimage/1648901-featurechannels.md) property of an [`MPSImage`](mpsimage.md) object. The size of the pixel is the size of the channel format multiplied by the number of feature channels. No padding is allowed, except to round out to a full byte.

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

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)

## See Also

- [protocol MPSHandle](mpshandle.md)
  The protocol that provides resource identification.
- [protocol MPSImageAllocator](mpsimageallocator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat)*