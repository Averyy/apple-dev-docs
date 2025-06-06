# usage

**Framework**: Metal Performance Shaders  
**Kind**: instp

Options to specify the intended usage of the underlying texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var usage: MTLTextureUsage { get set }
```

#### Discussion

The default value is [`shaderRead`](https://developer.apple.com/documentation/metal/mtltextureusage/shaderread)`|`[`shaderWrite`](https://developer.apple.com/documentation/metal/mtltextureusage/shaderwrite).

## See Also

- [var width: Int](mpsimagedescriptor/1648830-width.md)
  The width of the image.
- [var height: Int](mpsimagedescriptor/1648947-height.md)
  The height of the image.
- [var featureChannels: Int](mpsimagedescriptor/1648918-featurechannels.md)
  The number of feature channels per pixel.
- [var numberOfImages: Int](mpsimagedescriptor/1648846-numberofimages.md)
  The number of images for batch processing.
- [var pixelFormat: MTLPixelFormat](mpsimagedescriptor/1648913-pixelformat.md)
  The pixel format for the underlying texture.
- [var channelFormat: MPSImageFeatureChannelFormat](mpsimagedescriptor/1648818-channelformat.md)
  The storage format to use for each channel in the image.
- [var cpuCacheMode: MTLCPUCacheMode](mpsimagedescriptor/1648930-cpucachemode.md)
  The CPU cache mode of the underlying texture.
- [var storageMode: MTLStorageMode](mpsimagedescriptor/1648955-storagemode.md)
  The storage mode of underlying texture. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648937-usage)*