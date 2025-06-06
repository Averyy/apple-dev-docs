# clipRect

**Framework**: Metal Performance Shaders  
**Kind**: instp

An optional clip rectangle to use when writing data. Only the pixels in the clip rectangle will be overwritten.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var clipRect: MTLRegion { get set }
```

#### Discussion

A region that indicates which part of the destination image to overwrite. If the clip rectangle does not lie completely within the destination image, the intersection between the clip rectangle and the destination image bounds is used instead. 

The default value is [`MPSRectNoClip`](mpsrectnoclip.md), indicating that the entire destination image will be overwritten.

The value of `clipRect.origin.z` is the index of the starting destination image in batch processing mode. The value of `clipRect.size.depth` is the number of images to process in batch processing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/1648911-cliprect)*