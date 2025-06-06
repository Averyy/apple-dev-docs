# kVTCompressionPropertyKey_NumberOfPendingFrames

**Framework**: Videotoolbox  
**Kind**: var

The number of pending frames in the compression session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_NumberOfPendingFrames: CFString
```

#### Discussion

This number may decrease asynchronously.

## See Also

- [let kVTCompressionPropertyKey_PixelBufferPoolIsShared: CFString](kvtcompressionpropertykey_pixelbufferpoolisshared.md)
  A Boolean value indicating whether the common pixel buffer pool is shared between the video encoder and the session client.
- [let kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes: CFString](kvtcompressionpropertykey_videoencoderpixelbufferattributes.md)
  The video encoder’s pixel buffer attributes for the compression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_numberofpendingframes)*