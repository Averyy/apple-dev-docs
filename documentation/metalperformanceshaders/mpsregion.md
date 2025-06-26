# MPSRegion

**Framework**: Metal Performance Shaders  
**Kind**: struct

A region of an image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSRegion
```

## Topics

### Fields
- [var origin: MPSOrigin](mpsregion/origin.md)
  The top-left corner of the region.
- [var size: MPSSize](mpsregion/size.md)
  The size of the region.
### Initializers
- [init()](mpsregion/init.md)
- [init(origin: MPSOrigin, size: MPSSize)](mpsregion/init(origin:size:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var offset: MPSOffset](mpsunaryimagekernel/offset.md)
  The position of the destination clip rectangle origin relative to the source buffer.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpsunaryimagekernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.
- [var edgeMode: MPSImageEdgeMode](mpsunaryimagekernel/edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsregion)*