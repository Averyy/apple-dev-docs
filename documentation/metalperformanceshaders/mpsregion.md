# MPSRegion

**Framework**: Metal Performance Shaders  
**Kind**: struct

A region of an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MPSRegion
```

## Topics

### Initializers
- [init()](mpsregion/1618892-init.md)
- [init(origin: MPSOrigin, size: MPSSize)](mpsregion/1618860-init.md)
### Instance Properties
- [var origin: MPSOrigin](mpsregion/1618897-origin.md)
  The top-left corner of the region.
- [struct MPSOrigin](mpsorigin.md)
  A position in an image used as the source origin.
- [var size: MPSSize](mpsregion/1618858-size.md)
  The size of the region.
- [struct MPSSize](mpssize.md)
  A size of a region in an image.

## See Also

- [var offset: MPSOffset](mpsunaryimagekernel/1618884-offset.md)
  The position of the destination clip rectangle origin relative to the source buffer.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpsunaryimagekernel/1618859-cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.
- [var edgeMode: MPSImageEdgeMode](mpsunaryimagekernel/1618812-edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsregion)*