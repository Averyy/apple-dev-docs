# kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes

**Framework**: Videotoolbox  
**Kind**: var

The video encoder’s pixel buffer attributes for the compression session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes: CFString
```

#### Discussion

You can use these attributes to create a pixel buffer pool for source pixel buffers.

## See Also

- [let kVTCompressionPropertyKey_NumberOfPendingFrames: CFString](kvtcompressionpropertykey_numberofpendingframes.md)
  The number of pending frames in the compression session.
- [let kVTCompressionPropertyKey_PixelBufferPoolIsShared: CFString](kvtcompressionpropertykey_pixelbufferpoolisshared.md)
  A Boolean value indicating whether the common pixel buffer pool is shared between the video encoder and the session client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_videoencoderpixelbufferattributes)*