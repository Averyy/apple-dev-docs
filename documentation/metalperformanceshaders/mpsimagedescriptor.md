# MPSImageDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

A description of the attributes used to create an [`MPSImage`](mpsimage.md).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageDescriptor : NSObject
```

#### Overview

You use an [`MPSImageDescriptor`](mpsimagedescriptor.md) to describe and create the properties of an [`MPSImage`](mpsimage.md) such as its size, pixel format and CPU cache mode.

## Topics

### Methods
- [init(channelFormat: MPSImageFeatureChannelFormat, width: Int, height: Int, featureChannels: Int)](mpsimagedescriptor/1648819-init.md)
  Creates an image descriptor for a single image.
- [init(channelFormat: MPSImageFeatureChannelFormat, width: Int, height: Int, featureChannels: Int, numberOfImages: Int, usage: MTLTextureUsage)](mpsimagedescriptor/1648893-init.md)
  Creates an image descriptor for an image container with options to set texture usage and batch size (number of images).
### Properties
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
- [var usage: MTLTextureUsage](mpsimagedescriptor/1648937-usage.md)
  Options to specify the intended usage of the underlying texture.
### Instance Methods
- [func copy(with: NSZone?) -> Self](mpsimagedescriptor/3020686-copy.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor)*