# MPSImageFeatureChannelFormat.float32

**Framework**: Metal Performance Shaders  
**Kind**: case

IEEE-754 32-bit floating-point type (single precision, standard `float` type in C). 24 bits of precision + exponent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case float32
```

## See Also

- [MPSImageFeatureChannelFormat.none](mpsimagefeaturechannelformat/none.md)
- [MPSImageFeatureChannelFormat.unorm8](mpsimagefeaturechannelformat/unorm8.md)
  `uint8_t` type with value `[0,255]` and encoding `[0,1.0]`.
- [MPSImageFeatureChannelFormat.unorm16](mpsimagefeaturechannelformat/unorm16.md)
  `uint16_t` type with value `[0,65535]` and encoding `[0,1.0]`.
- [MPSImageFeatureChannelFormat.float16](mpsimagefeaturechannelformat/float16.md)
  IEEE-754 16-bit floating-point type (half precision). Representable normal range is `+-[2^-14, 65504], 0, INF, NaN`. 11 bits of precision + exponent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat/float32)*