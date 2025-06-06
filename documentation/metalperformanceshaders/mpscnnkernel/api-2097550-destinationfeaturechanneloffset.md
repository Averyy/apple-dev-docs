# destinationFeatureChannelOffset

**Framework**: Metal Performance Shaders  
**Kind**: instp

The number of channels in the destination image to skip before writing output data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var destinationFeatureChannelOffset: Int { get set }
```

#### Discussion

This is the starting offset in the destination image in the feature channel dimension at which destination output data is written. This allows you to pass a subset of all the channels in an image as the output of a kernel.

For example, suppose a destination image has 24 channels and a kernel outputs 8 channels. If we want channels 8 to 15 of this destination image to be used for the output, we can set the value of the [`destinationFeatureChannelOffset`](mpscnnkernel/2097550-destinationfeaturechanneloffset.md) property to 8.

Note that this offset applies independently to each image when the [`MPSImage`](mpsimage.md) object is a container for multiple images and the [`MPSCNNKernel`](mpscnnkernel.md) object is processing multiple images (i.e., `clipRect.size.depth > 1`).

The default value is `0`. Any other value specified must be a multiple of `4`. If the kernel outputs `N` channels, the destination image  have at least `destinationFeatureChannelOffset + N` channels. Using a destination image with an insufficient number of feature channels results in an error.

For example, if a convolution filter outputs 32 channels, and the destination image has 64 channels, then it is an error to set `destinationFeatureChannelOffset > 32`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/2097550-destinationfeaturechanneloffset)*