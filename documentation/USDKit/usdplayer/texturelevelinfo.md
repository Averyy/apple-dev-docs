# USDPlayer.TextureLevelInfo

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Byte-layout descriptor for a single mip level within a [`USDPlayer.TextureData`](./texturedata.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct TextureLevelInfo
```

## Topics

### Instance Properties
- [let byteCountPerImage: Int](./texturelevelinfo/bytecountperimage.md)
  Total byte size of this mip level.
- [let byteCountPerRow: Int](./texturelevelinfo/bytecountperrow.md)
  Row stride in bytes.
- [let dataOffset: Int](./texturelevelinfo/dataoffset.md)
  Byte offset into [`data`](./texturedata/data.md) where this mip level begins.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/texturelevelinfo)*