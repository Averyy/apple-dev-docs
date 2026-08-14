# USDPlayer.TextureLevelInfo

**Framework**: USDKit  
**Kind**: struct

Byte-layout descriptor for a single mip level within a [`USDPlayer.TextureData`](usdplayer/texturedata.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TextureLevelInfo
```

## Topics

### Instance Properties
- [let byteCountPerImage: Int](usdplayer/texturelevelinfo/bytecountperimage.md)
  Total byte size of this mip level.
- [let byteCountPerRow: Int](usdplayer/texturelevelinfo/bytecountperrow.md)
  Row stride in bytes.
- [let dataOffset: Int](usdplayer/texturelevelinfo/dataoffset.md)
  Byte offset into [`data`](usdplayer/texturedata/data.md) where this mip level begins.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/texturelevelinfo)*