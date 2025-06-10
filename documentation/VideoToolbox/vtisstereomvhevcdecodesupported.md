# VTIsStereoMVHEVCDecodeSupported()

**Framework**: Video Toolbox  
**Kind**: func

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the system supports MV-HEVC decoding; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

A return value of [`true`](https://developer.apple.com/documentation/swift/true) doesn’t guarantee that decoding resources are available at all times.

## See Also

- [typealias VTDecompressionMultiImageCapableOutputHandler](vtdecompressionmultiimagecapableoutputhandler.md)
  A type alias for callback that the system invokes when it finishes decompressing a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtisstereomvhevcdecodesupported())*