# secondaryEdgeMode

**Framework**: Metal Performance Shaders  
**Kind**: instp

The edge mode to use when texture reads stray off the edge of the secondary source image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var secondaryEdgeMode: MPSImageEdgeMode { get set }
```

#### Discussion

Most kernel objects can read off the edge of a source image. This can happen because of a negative offset property, because the `offset + clipRect.size` is larger than the source image, or because the filter uses neighboring pixels in its calculations (e.g. convolution filters).

The default value is usually [`MPSImageEdgeMode.zero`](mpsimageedgemode/zero.md), but some kernels default to the [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) value instead if an edge mode of zero is either unsupported or undefined.

## See Also

- [var primaryOffset: MPSOffset](mpsbinaryimagekernel/1618880-primaryoffset.md)
  The position of the destination clip rectangle origin relative to the primary source buffer.
- [var secondaryOffset: MPSOffset](mpsbinaryimagekernel/1618755-secondaryoffset.md)
  The position of the destination clip rectangle origin relative to the secondary source buffer.
- [var primaryEdgeMode: MPSImageEdgeMode](mpsbinaryimagekernel/1618782-primaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the primary source image.
- [var clipRect: MTLRegion](mpsbinaryimagekernel/1618879-cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618848-secondaryedgemode)*