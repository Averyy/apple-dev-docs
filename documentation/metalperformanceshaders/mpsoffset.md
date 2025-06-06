# MPSOffset

**Framework**: Metal Performance Shaders  
**Kind**: struct

A signed coordinate with x, y, and z components.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MPSOffset
```

## Topics

### Initializers
- [init()](mpsoffset/1618896-init.md)
- [init(x: Int, y: Int, z: Int)](mpsoffset/1618740-init.md)
### Instance Properties
- [var x: Int](mpsoffset/1618861-x.md)
  The horizontal component of the offset, in pixels.
- [var y: Int](mpsoffset/1618846-y.md)
  The vertical component of the offset, in pixels.
- [var z: Int](mpsoffset/1618881-z.md)
  The depth component of the offset, in pixels.

## See Also

- [var offset: MPSOffset](mpsunaryimagekernel/1618884-offset.md)
  The position of the destination clip rectangle origin relative to the source buffer.
- [var clipRect: MTLRegion](mpsunaryimagekernel/1618859-cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.
- [struct MPSRegion](mpsregion.md)
  A region of an image.
- [var edgeMode: MPSImageEdgeMode](mpsunaryimagekernel/1618812-edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsoffset)*