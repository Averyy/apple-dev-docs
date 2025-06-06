# edgeMode

**Framework**: Metal Performance Shaders  
**Kind**: instp

The edge mode to use when texture reads stray off the edge of an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var edgeMode: MPSImageEdgeMode { get set }
```

#### Discussion

Most kernel objects can read off the edge of a source image. This can happen because of a negative offset property, because the `offset + clipRect.size` is larger than the source image, or because the filter uses neighboring pixels in its calculations (e.g. convolution filters).

The default value is usually [`MPSImageEdgeMode.zero`](mpsimageedgemode/zero.md), but some kernels default to the [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) value instead if an edge mode of zero is either unsupported or undefined.

## See Also

- [var offset: MPSOffset](mpsunaryimagekernel/1618884-offset.md)
  The position of the destination clip rectangle origin relative to the source buffer.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpsunaryimagekernel/1618859-cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.
- [struct MPSRegion](mpsregion.md)
  A region of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618812-edgemode)*