# MPSImageEdgeMode

**Framework**: Metal Performance Shaders  
**Kind**: enum

The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSImageEdgeMode : UInt, @unchecked Sendable
```

## Topics

### Constants
- [MPSImageEdgeMode.zero](mpsimageedgemode/zero.md)
  Out-of-bound pixels are set to `(0.0, 0.0, 0.0, 1.0)` for images without an alpha channel or `(0.0, 0.0, 0.0, 0.0)` for images with an alpha channel, as defined by their pixel format.
- [MPSImageEdgeMode.clamp](mpsimageedgemode/clamp.md)
  Out-of-bound pixels are clamped to the nearest edge pixel.
### Enumeration Cases
- [MPSImageEdgeMode.constant](mpsimageedgemode/constant.md)
- [MPSImageEdgeMode.mirror](mpsimageedgemode/mirror.md)
- [MPSImageEdgeMode.mirrorWithEdge](mpsimageedgemode/mirrorwithedge.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)

## See Also

- [var offset: MPSOffset](mpsunaryimagekernel/1618884-offset.md)
  The position of the destination clip rectangle origin relative to the source buffer.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpsunaryimagekernel/1618859-cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.
- [struct MPSRegion](mpsregion.md)
  A region of an image.
- [var edgeMode: MPSImageEdgeMode](mpsunaryimagekernel/1618812-edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedgemode)*