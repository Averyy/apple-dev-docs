# VTIsStereoMVHEVCDecodeSupported()

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the system supports MV-HEVC decoding.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func VTIsStereoMVHEVCDecodeSupported() -> Bool
```

```c
extern Boolean VTIsStereoMVHEVCDecodeSupported();
```

#### Return Value

[`true`](../Swift/true.md) if the system supports MV-HEVC decoding; otherwise, [`false`](../Swift/false.md).

#### Discussion

A return value of [`true`](../Swift/true.md) doesn’t guarantee that decoding resources are available at all times.

## See Also

### Decoding Multi-Image Frames
- [typealias VTDecompressionMultiImageCapableOutputHandler](./vtdecompressionmultiimagecapableoutputhandler.md)
  A type alias for callback that the system invokes when it finishes decompressing a frame.
- [VTDecompressionSessionSetMultiImageCallback](./vtdecompressionsessionsetmultiimagecallback.md)
  Provides a callback capable of receiving multiple images for individual frame decoding requests.
- [VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler](./vtdecompressionsessiondecodeframewithmultiimagecapableoutputhandler.md)
  Decompresses a multi-image frame and calls the specified output handler upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtisstereomvhevcdecodesupported())*