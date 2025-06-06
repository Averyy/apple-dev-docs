# primaryOffset

**Framework**: Metal Performance Shaders  
**Kind**: instp

The position of the destination clip rectangle origin relative to the primary source buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var primaryOffset: MPSOffset { get set }
```

#### Discussion

The offset is defined to be the position of the `origin` value of [`clipRect`](mpsbinaryimagekernel/1618879-cliprect.md), in source coordinates.

The default value is `{0, 0, 0}`, indicating that the top left corners of the clip rectangle and the primary source image align.

## See Also

- [var secondaryOffset: MPSOffset](mpsbinaryimagekernel/1618755-secondaryoffset.md)
  The position of the destination clip rectangle origin relative to the secondary source buffer.
- [var primaryEdgeMode: MPSImageEdgeMode](mpsbinaryimagekernel/1618782-primaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the primary source image.
- [var secondaryEdgeMode: MPSImageEdgeMode](mpsbinaryimagekernel/1618848-secondaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the secondary source image.
- [var clipRect: MTLRegion](mpsbinaryimagekernel/1618879-cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618880-primaryoffset)*